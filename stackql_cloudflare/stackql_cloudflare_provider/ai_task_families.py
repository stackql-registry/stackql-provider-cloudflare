"""Collapse the per-model Workers AI run resources into task-family
resources.

The upstream spec exposes ~98 per-model operations
(`POST /accounts/{account_id}/ai/run/@cf/<vendor>/<model>`) which the
generator turns into ~99 single-method resources - overwhelming the `ai`
service and all non-selectable. It also exposes a generic
`POST /accounts/{account_id}/ai/run/{model_name}` operation which works
with slash-containing model names (verified live through stackql - the
value substitutes literally into the URL).

This pass, driven by `provider-dev/config/ai_task_families.yaml`:

1. Rewrites the generic run operation's 200 response to a typed union
   envelope (`stackqlAiRunResponseEnvelope`): `result` carries the union
   of all object-mode families' result fields, plus a top-level
   `contents` column used by the contents-mode families.
2. Creates one resource per task family (`cloudflare.ai.text_generation`,
   `cloudflare.ai.text_embeddings`, ...) with a single `run` SELECT
   method riding the generic operation:
   - `request.schema_override` -> `stackqlAi<Family>RunInput`, the union
     of the member models' request-body properties. WHERE params bind to
     these with unprefixed names (SELECT semantics - `data__` does not
     apply to SELECT).
   - a `request.transform` that serialises exactly the SET/WHERE-provided
     properties (same dual-mode complex/scalar pattern as
     `request_body_transforms.py`).
   - object-mode families project `objectKey: $.result` (typed columns);
     contents-mode families wrap the raw response as a `contents` column
     (binary or non-object results).
3. Points the generic `ai.run` resource's `run` method at the same
   machinery and adds a select mapping - it remains the escape hatch for
   models not yet listed in any family.
4. Deletes the member models' per-model paths and resources from the
   generated ai.yaml. Component schemas are left in place (still
   referenced by the synthesised input schemas).

Models whose only input is a raw octet-stream body (whisper, resnet,
detr) are excluded: binary WHERE values are impractical, so they keep
their per-model insert resources (handled by `octet_stream_requests.py`).

Runs after `octet_stream_requests.py` in the generate-provider chain.
Idempotent: if the member paths are already gone (pass previously
applied), families are left as they are.
"""
from __future__ import annotations

import argparse
import copy
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


logger = logging.getLogger(__name__)


_YAML_1_1_BOOL_LITERALS = frozenset({
    "y", "Y", "yes", "Yes", "YES",
    "n", "N", "no", "No", "NO",
    "true", "True", "TRUE",
    "false", "False", "FALSE",
    "on", "On", "ON",
    "off", "Off", "OFF",
})


def _represent_str_yaml11_safe(dumper, data):
    style = "'" if data in _YAML_1_1_BOOL_LITERALS else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


yaml.SafeDumper.add_representer(str, _represent_str_yaml11_safe)


PKG_DIR = Path(__file__).resolve().parent
PROVIDER_DIR = (
    PKG_DIR.parent
    / "provider-dev" / "openapi" / "src" / "cloudflare" / "v00.00.00000"
)
CONFIG_PATH = PKG_DIR.parent / "provider-dev" / "config" / "ai_task_families.yaml"

GENERIC_PATH = "/accounts/{account_id}/ai/run/{model_name}"
GENERIC_OP_REF = "#/paths/~1accounts~1{account_id}~1ai~1run~1{model_name}/post"
ENVELOPE_SCHEMA = "stackqlAiRunResponseEnvelope"
_SCHEMA_REF_PREFIX = "#/components/schemas/"
_COMPLEX_TYPES = ("array", "object")


def _pascal(s: str) -> str:
    return "".join(p[:1].upper() + p[1:] for p in s.replace("-", "_").split("_") if p)


def _model_path(model: str) -> str:
    return "/accounts/{account_id}/ai/run/" + model


def _resolve_ref(ref: str, schemas: Dict[str, Any]) -> Optional[dict]:
    if not ref.startswith(_SCHEMA_REF_PREFIX):
        return None
    return schemas.get(ref[len(_SCHEMA_REF_PREFIX):])


def _prop_kind(prop: Any, schemas: Dict[str, Any]) -> str:
    """'complex' | 'scalar' | 'unknown' - one or two $ref hops allowed."""
    seen = 0
    while isinstance(prop, dict) and "$ref" in prop and seen < 3:
        prop = _resolve_ref(prop["$ref"], schemas) or {}
        seen += 1
    if not isinstance(prop, dict):
        return "unknown"
    t = prop.get("type")
    if t in _COMPLEX_TYPES:
        return "complex"
    if t in ("string", "number", "integer", "boolean"):
        return "scalar"
    if isinstance(prop.get("properties"), dict):
        return "complex"
    if isinstance(prop.get("items"), dict):
        return "complex"
    return "unknown"


def _union_body_props(spec: dict, member_paths: List[str]) -> "Dict[str, Any]":
    """Merge request-body JSON schema properties across member ops.
    First definition wins on name conflicts. Returns {name: schema}."""
    schemas = (spec.get("components") or {}).get("schemas") or {}
    out: Dict[str, Any] = {}
    for p in member_paths:
        op = (spec.get("paths", {}).get(p) or {}).get("post")
        if not isinstance(op, dict):
            continue
        body = (((op.get("requestBody") or {}).get("content") or {})
                .get("application/json") or {}).get("schema") or {}
        if "$ref" in body:
            body = _resolve_ref(body["$ref"], schemas) or {}
        for name, prop in (body.get("properties") or {}).items():
            if name not in out:
                out[name] = copy.deepcopy(prop)
    return out


def _build_transform_body(props: List[Tuple[str, str]]) -> str:
    """Go template serialising exactly the provided properties (complex
    props with the string-vs-parsed dual mode, scalars via toJson).
    Unlike request_body_transforms, always returns a template - SELECT
    body building relies on it."""
    lines = ["{"]
    lines.append('{{- $sep := "" -}}')
    for name, kind in props:
        if kind == "unknown":
            continue
        if kind == "complex":
            value_expr = (
                '{{ if eq (kindOf .' + name + ') "string" }}'
                '{{ .' + name + ' }}'
                '{{ else }}'
                '{{ toJson .' + name + ' }}'
                '{{ end }}'
            )
        else:
            value_expr = '{{ toJson .' + name + ' }}'
        lines.append(
            '{{- if .' + name + ' }}{{ $sep }}"' + name + '": ' + value_expr +
            '{{- $sep = "," -}}{{ end }}'
        )
    lines.append("}")
    return "\n".join(lines) + "\n"


def _build_envelope_schema(config: dict) -> dict:
    result_props: Dict[str, Any] = {
        "model": {"type": "string", "description": "Echo of the model name, where reported."},
    }
    for fam, meta in (config.get("families") or {}).items():
        for name, schema in (meta.get("result_fields") or {}).items():
            result_props.setdefault(name, schema)
    return {
        "type": "object",
        "description": "Union response envelope for Workers AI run operations (synthesised by stackql).",
        "properties": {
            "result": {"type": "object", "properties": result_props},
            "success": {"type": "boolean"},
            "errors": {"type": "array", "items": {"type": "object"}},
            "messages": {"type": "array", "items": {"type": "string"}},
            "contents": {"type": "string",
                         "description": "Raw response payload (binary or non-object results), used by contents-mode families."},
        },
    }


def _family_method(mode: str, input_schema_name: str, transform_body: str) -> dict:
    m: dict = {
        "config": {"requestBodyTranslate": {"algorithm": "naive"}},
        "operation": {"$ref": GENERIC_OP_REF},
        "request": {
            "mediaType": "application/json",
            "schema_override": {"$ref": _SCHEMA_REF_PREFIX + input_schema_name},
            "transform": {"type": "golang_template_json_v0.3.0", "body": transform_body},
        },
    }
    if mode == "object":
        m["response"] = {
            "mediaType": "application/json",
            "openAPIDocKey": "200",
            "objectKey": "$.result",
        }
    else:  # contents
        m["response"] = {
            "mediaType": "application/json",
            "openAPIDocKey": "200",
            "overrideMediaType": "application/json",
            "transform": {"body": '[{"contents": {{ toJson . }}}]',
                          "type": "golang_template_text_v0.3.0"},
        }
    return m


def process(provider_dir: Path, config_path: Path) -> int:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    families: Dict[str, dict] = config.get("families") or {}
    if not families:
        logger.error("No families defined in %s", config_path)
        return 1

    gen_path = provider_dir / "services" / "ai.yaml"
    spec = yaml.safe_load(gen_path.read_text(encoding="utf-8"))
    paths = spec.get("paths") or {}
    components = spec.setdefault("components", {})
    schemas = components.setdefault("schemas", {})
    resources = components.setdefault("x-stackQL-resources", {})

    if GENERIC_PATH not in paths:
        logger.error("Generic run path %s not found in generated ai.yaml", GENERIC_PATH)
        return 1

    # 1. Envelope schema + generic op response rewrite.
    schemas[ENVELOPE_SCHEMA] = _build_envelope_schema(config)
    generic_op = paths[GENERIC_PATH]["post"]
    generic_op.setdefault("responses", {}).setdefault("200", {})["content"] = {
        "application/json": {"schema": {"$ref": _SCHEMA_REF_PREFIX + ENVELOPE_SCHEMA}}
    }

    # Map member path -> (resource, method) so we can drop them.
    path_to_res: Dict[str, Tuple[str, str]] = {}
    for r_name, r in resources.items():
        for m_name, m in (r.get("methods") or {}).items():
            op_ref = ((m.get("operation") or {}).get("$ref") or "")
            parts = op_ref.split("/")
            if len(parts) > 3 and parts[-1] == "post":
                p = "/".join(parts[2:-1]).replace("~1", "/")
                path_to_res[p] = (r_name, m_name)

    fam_count = 0
    dropped_paths = 0
    dropped_resources = 0
    all_union_props: Dict[str, Any] = {}

    for fam, meta in families.items():
        member_paths = [_model_path(m) for m in (meta.get("members") or [])]
        present = [p for p in member_paths if p in paths]
        if not present:
            if fam in resources:
                logger.debug("%s: members already collapsed - leaving existing resource", fam)
                continue
            logger.warning("%s: no member paths found and no existing resource - skipping", fam)
            continue

        union = _union_body_props(spec, present)
        for k, v in union.items():
            all_union_props.setdefault(k, copy.deepcopy(v))
        input_name = "stackqlAi" + _pascal(fam) + "RunInput"
        schemas[input_name] = {
            "type": "object",
            "description": f"Union of request properties across the {fam} member models (synthesised by stackql).",
            "properties": union,
        }
        prop_kinds = [(n, _prop_kind(p, schemas)) for n, p in union.items()]
        transform_body = _build_transform_body(prop_kinds)

        resources[fam] = {
            "id": f"cloudflare.ai.{fam}",
            "name": fam,
            "title": meta.get("title") or fam,
            "methods": {"run": _family_method(meta.get("mode") or "object", input_name, transform_body)},
            "sqlVerbs": {
                "select": [{"$ref": f"#/components/x-stackQL-resources/{fam}/methods/run"}],
                "insert": [], "update": [], "delete": [], "replace": [],
            },
        }
        fam_count += 1

        # Drop member paths + their per-model resources.
        for p in present:
            res_method = path_to_res.get(p)
            if res_method:
                r_name, m_name = res_method
                r = resources.get(r_name)
                if r and r_name != fam:
                    (r.get("methods") or {}).pop(m_name, None)
                    if not r.get("methods"):
                        resources.pop(r_name, None)
                        dropped_resources += 1
            paths.pop(p, None)
            dropped_paths += 1

    # 3. Generic ai.run escape hatch: same input/transform machinery,
    # union of ALL family props, typed envelope select.
    run_res = resources.get("run")
    if run_res and all_union_props:
        input_name = "stackqlAiRunInput"
        schemas[input_name] = {
            "type": "object",
            "description": "Union of request properties across all Workers AI run models (synthesised by stackql).",
            "properties": all_union_props,
        }
        prop_kinds = [(n, _prop_kind(p, schemas)) for n, p in all_union_props.items()]
        m = run_res.get("methods", {}).get("run")
        if m is not None:
            m["config"] = {"requestBodyTranslate": {"algorithm": "naive"}}
            m["request"] = {
                "mediaType": "application/json",
                "schema_override": {"$ref": _SCHEMA_REF_PREFIX + input_name},
                "transform": {"type": "golang_template_json_v0.3.0",
                              "body": _build_transform_body(prop_kinds)},
            }
            m["response"] = {
                "mediaType": "application/json",
                "openAPIDocKey": "200",
                "objectKey": "$.result",
            }
            # run is select-only: keeping the same method under insert too
            # would render duplicate INSERT/SELECT doc examples for one op.
            verbs = run_res.setdefault("sqlVerbs", {})
            verbs["select"] = [
                {"$ref": "#/components/x-stackQL-resources/run/methods/run"}
            ]
            verbs["insert"] = []

    if fam_count:
        with gen_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(spec, f, sort_keys=False, default_flow_style=False, width=1000)

    logger.info("Created %d family resources; dropped %d per-model paths and %d per-model resources.",
                fam_count, dropped_paths, dropped_resources)
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider-dir", default=str(PROVIDER_DIR))
    parser.add_argument("--config", default=str(CONFIG_PATH))
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    provider_dir = Path(args.provider_dir)
    config_path = Path(args.config)
    if not (provider_dir / "services" / "ai.yaml").exists():
        logger.error("ai.yaml not found under %s. Run `npm run generate-provider` first.", provider_dir)
        return 1
    if not config_path.exists():
        logger.error("Config not found: %s", config_path)
        return 1
    return process(provider_dir, config_path)


if __name__ == "__main__":
    sys.exit(main())
