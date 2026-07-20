"""Rewrite resource methods whose request body is `application/octet-stream`.

Why: stackql's `naive` requestBodyTranslate (and the generated
request.transform blocks) both assume a JSON request body built from the
SET clause. A handful of Cloudflare endpoints (KV value PUT, Workers AI
binary-input models, DLP dataset uploads) take the raw request body as
an opaque octet-stream payload instead - there are no named body
properties to translate, the whole body IS the value.

For each such method this pass:

1. Injects a wrapper schema into the service's `components/schemas`:

       stackqlWorkersKvValueBody:
         type: object
         required: [value]
         properties:
           value: <original body schema or $ref>

   The `stackql` prefix marks it as synthesised for stackql (it does not
   exist in the upstream spec).

2. Drops the `config.requestBodyTranslate.algorithm = naive` block from
   the resource method (naive translation would JSON-encode the body map
   `{"value": "..."}` instead of sending the raw payload).

3. Attaches a `request` block that presents a single required `value`
   column to the planner (via `schema_override`) and splats it verbatim
   onto the wire as the raw octet-stream body:

       request:
         mediaType: application/octet-stream
         required:
           - value
         schema_override:
           $ref: '#/components/schemas/stackqlWorkersKvValueBody'
         transform:
           type: golang_template_json_v0.1.0
           body: '{{ .value }}'

Callers then write e.g.:

    REPLACE cloudflare.kv.values
    SET data__value = '0.10.557'
    WHERE account_id = '...' AND namespace_id = '...' AND key_name = '...';

Note the `data__` prefix is mandatory for these methods - with naive
translation removed, body columns are only addressable via `data__`.
The companion docs pass (`octet_stream_docs.py`) rewrites the doc
examples accordingly.

This step runs after `request_body_transforms.py` in the
`generate-provider` post-pass chain. Idempotent.
"""
from __future__ import annotations

import argparse
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
SOURCE_DIR = PKG_DIR.parent / "provider-dev" / "source"

_WRITE_VERBS = ("put", "post", "patch")
_OCTET_STREAM = "application/octet-stream"
_SCHEMA_REF_PREFIX = "#/components/schemas/"


def _pascal(s: str) -> str:
    out = "".join(part[:1].upper() + part[1:] for part in s.replace("-", "_").split("_") if part)
    return out or "Body"


def _wrapper_schema_name(body_schema: dict, op: dict) -> str:
    """Deterministic name for the injected wrapper schema, always
    `stackql`-prefixed. From the body $ref name if present, else from the
    operationId."""
    ref = body_schema.get("$ref")
    if isinstance(ref, str) and ref.startswith(_SCHEMA_REF_PREFIX):
        base = ref[len(_SCHEMA_REF_PREFIX):]
    else:
        base = op.get("operationId") or "octet_stream"
    return "stackql" + _pascal(base) + "Body"


def _find_octet_stream_ops(source_spec: dict) -> Dict[Tuple[str, str], Tuple[str, dict]]:
    """Return {(path, verb): (wrapper_name, body_schema)} for every
    write-verb op whose request body is application/octet-stream."""
    out: Dict[Tuple[str, str], Tuple[str, dict]] = {}
    for path, item in (source_spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for verb in _WRITE_VERBS:
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            content = ((op.get("requestBody") or {}).get("content") or {})
            mt_spec = content.get(_OCTET_STREAM)
            if not isinstance(mt_spec, dict):
                continue
            schema = mt_spec.get("schema") or {"type": "string", "format": "binary"}
            out[(path, verb)] = (_wrapper_schema_name(schema, op), schema)
    return out


def _op_ref_to_path_verb(op_ref: str) -> Tuple[str, str]:
    parts = op_ref.split("/")
    verb = parts[-1]
    encoded = "/".join(parts[2:-1])
    path = encoded.replace("~1", "/")
    return path, verb


def _build_wrapper_schema(body_schema: dict) -> dict:
    """The synthetic single-column body schema presented to the planner."""
    value_schema: Any
    ref = body_schema.get("$ref")
    if isinstance(ref, str):
        value_schema = {"$ref": ref}
    else:
        value_schema = dict(body_schema)
    return {
        "type": "object",
        "required": ["value"],
        "properties": {
            "value": value_schema,
        },
    }


def _rebuild_method(m: dict, wrapper_name: str) -> dict:
    """Return the method dict with naive requestBodyTranslate removed and
    the octet-stream request block attached, preserving a stable key
    order (config, operation, request, response, everything else)."""
    config = m.get("config")
    if isinstance(config, dict):
        rbt = config.get("requestBodyTranslate")
        if isinstance(rbt, dict) and rbt.get("algorithm") == "naive":
            config = {k: v for k, v in config.items() if k != "requestBodyTranslate"}
    request = {
        "mediaType": _OCTET_STREAM,
        "required": ["value"],
        "schema_override": {"$ref": _SCHEMA_REF_PREFIX + wrapper_name},
        "transform": {
            "type": "golang_template_json_v0.1.0",
            "body": "{{ .value }}",
        },
    }
    out: dict = {}
    if config:
        out["config"] = config
    if "operation" in m:
        out["operation"] = m["operation"]
    out["request"] = request
    if "response" in m:
        out["response"] = m["response"]
    for k, v in m.items():
        if k not in ("config", "operation", "request", "response"):
            out[k] = v
    return out


def process_service_file(generated_path: Path, source_path: Path) -> Dict[str, int]:
    source_spec = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    if not isinstance(source_spec, dict):
        return {"methods": 0}
    targets = _find_octet_stream_ops(source_spec)
    if not targets:
        return {"methods": 0}

    generated_spec = yaml.safe_load(generated_path.read_text(encoding="utf-8"))
    if not isinstance(generated_spec, dict):
        return {"methods": 0}

    components = generated_spec.setdefault("components", {})
    schemas = components.setdefault("schemas", {})
    resources = components.get("x-stackQL-resources") or {}
    method_count = 0

    for r_name, r in resources.items():
        methods = r.get("methods") or {}
        for m_name in list(methods):
            m = methods[m_name]
            op_ref = ((m.get("operation") or {}).get("$ref") or "")
            if not op_ref:
                continue
            try:
                p, v = _op_ref_to_path_verb(op_ref)
            except Exception:
                continue
            target = targets.get((p, v))
            if not target:
                continue
            wrapper_name, body_schema = target
            already = (m.get("request") or {}).get("mediaType") == _OCTET_STREAM
            schemas.setdefault(wrapper_name, _build_wrapper_schema(body_schema))
            methods[m_name] = _rebuild_method(m, wrapper_name)
            if not already:
                method_count += 1
            logger.debug("%s: %s.%s -> octet-stream request via %s%s",
                         generated_path.name, r_name, m_name, wrapper_name,
                         " (already applied)" if already else "")

    if method_count:
        with generated_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(generated_spec, f, sort_keys=False, default_flow_style=False, width=1000)

    return {"methods": method_count}


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider-dir", default=str(PROVIDER_DIR),
                        help=f"Provider root containing services/. Default: {PROVIDER_DIR}")
    parser.add_argument("--source-dir", default=str(SOURCE_DIR),
                        help=f"Source yamls dir (for body schema lookup). Default: {SOURCE_DIR}")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    services_dir = Path(args.provider_dir) / "services"
    source_dir = Path(args.source_dir)
    if not services_dir.exists():
        logger.error("services/ dir not found at %s. Run `npm run generate-provider` first.", services_dir)
        return 1
    if not source_dir.exists():
        logger.error("source/ dir not found at %s.", source_dir)
        return 1

    total_methods = 0
    touched_files = 0
    for generated_path in sorted(services_dir.glob("*.yaml")):
        source_path = source_dir / generated_path.name
        if not source_path.exists():
            continue
        stats = process_service_file(generated_path, source_path)
        if stats["methods"]:
            touched_files += 1
            total_methods += stats["methods"]
            logger.info("%s: rewrote %d octet-stream request methods",
                        generated_path.name, stats["methods"])

    logger.info("Rewrote %d octet-stream request methods across %d files.",
                total_methods, touched_files)
    return 0


if __name__ == "__main__":
    sys.exit(main())
