"""Fix response shapes for resources whose SELECT would yield no columns.

Driven by `provider-dev/config/select_response_fixes.yaml`. Targets
operations whose upstream 200 response is untyped (`{type: object}`
items), a scalar array, a dynamic-keyed object, a raw text body, or
missing entirely - all of which make DESCRIBE return zero columns and
the meta-route test flag the resource as non-selectable.

Fix kinds (see the config header for full semantics): item_schema,
scalar_rows, result_to_contents, array_items_contents, contents,
add_200_contents. All except item_schema rewrite the op's 200 schema to
match the transform output, attach a `response.transform` to every
resource method referencing the op (binary_responses.py pattern), and
drop the method's objectKey.

Runs after `ai_task_families.py` in the generate-provider chain.
Idempotent - fixes overwrite deterministically.
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
CONFIG_PATH = PKG_DIR.parent / "provider-dev" / "config" / "select_response_fixes.yaml"

_SCHEMA_REF_PREFIX = "#/components/schemas/"
# Text transforms receive the RAW response body string - only `{{ . }}` /
# `{{ toJson . }}` make sense there. Kinds that access `.result` need the
# json transform type, which parses the body first (verified live:
# text-type `.result` access errors out and produces an empty body).
_TEXT_TRANSFORM = "golang_template_text_v0.3.0"
_JSON_TRANSFORM = "golang_template_json_v0.3.0"
_JSON_KINDS = ("scalar_rows", "result_to_contents", "array_items_contents")


def _row_schema(props: Dict[str, Any]) -> dict:
    return {"type": "object", "properties": props}


def _transform_for(kind: str, column: str) -> str:
    if kind == "scalar_rows":
        return ('[{{ range $i, $v := .result }}{{ if $i }},{{ end }}'
                '{"' + column + '": {{ toJson $v }}}{{ end }}]')
    if kind == "result_to_contents":
        return '[{"contents": {{ toJson .result }}}]'
    if kind == "array_items_contents":
        return ('[{{ range $i, $v := .result }}{{ if $i }},{{ end }}'
                '{"contents": {{ toJson $v }}}{{ end }}]')
    # contents / add_200_contents
    return '[{"contents": {{ toJson . }}}]'


def _deref_inline(schema: Any, schemas: Dict[str, Any]) -> Any:
    """Resolve a top-level $ref to a deep copy so shared component
    schemas are never mutated."""
    hops = 0
    while isinstance(schema, dict) and "$ref" in schema and hops < 3:
        target = schemas.get(schema["$ref"][len(_SCHEMA_REF_PREFIX):]) \
            if schema["$ref"].startswith(_SCHEMA_REF_PREFIX) else None
        if target is None:
            return schema
        schema = copy.deepcopy(target)
        hops += 1
    return schema


def _methods_for_op(resources: dict, path: str, verb: str) -> List[Tuple[str, str, dict]]:
    out = []
    for r_name, r in resources.items():
        for m_name, m in (r.get("methods") or {}).items():
            op_ref = ((m.get("operation") or {}).get("$ref") or "")
            parts = op_ref.split("/")
            if len(parts) > 3 and parts[-1] == verb:
                p = "/".join(parts[2:-1]).replace("~1", "/")
                if p == path:
                    out.append((r_name, m_name, m))
    return out


def apply_fix(spec: dict, fix: dict) -> bool:
    path, verb, kind = fix["path"], fix["verb"], fix["kind"]
    column = fix.get("column", "contents")
    op = (spec.get("paths", {}).get(path) or {}).get(verb)
    if not isinstance(op, dict):
        logger.warning("op not found: %s %s", verb.upper(), path)
        return False
    schemas = (spec.get("components") or {}).get("schemas") or {}
    responses = op.setdefault("responses", {})
    r200 = responses.setdefault("200", {"description": "OK"})

    if kind == "item_schema":
        content = (r200.get("content") or {}).get("application/json")
        if not isinstance(content, dict):
            logger.warning("item_schema: no 200 json content for %s %s", verb, path)
            return False
        env = _deref_inline(content.get("schema") or {}, schemas)
        result = (env.get("properties") or {}).get("result")
        if not isinstance(result, dict):
            logger.warning("item_schema: no result property for %s %s", verb, path)
            return False
        result = _deref_inline(result, schemas)
        result["items"] = copy.deepcopy(fix["schema"])
        result["type"] = "array"
        env.setdefault("properties", {})["result"] = result
        content["schema"] = env
        return True

    # All remaining kinds: rewrite the 200 schema to the transform's row
    # shape and attach the transform on every referencing method.
    row_props = {column: {"type": "string"}} if kind == "scalar_rows" else {"contents": {"type": "string"}}
    if kind == "scalar_rows" and "column_description" in fix:
        row_props[column]["description"] = fix["column_description"]
    r200["content"] = {"application/json": {"schema": _row_schema(row_props)}}

    resources = ((spec.get("components") or {}).get("x-stackQL-resources") or {})
    hit = False
    for r_name, m_name, m in _methods_for_op(resources, path, verb):
        ttype = _JSON_TRANSFORM if kind in _JSON_KINDS else _TEXT_TRANSFORM
        m["response"] = {
            "mediaType": "application/json",
            "openAPIDocKey": "200",
            "overrideMediaType": "application/json",
            "transform": {"body": _transform_for(kind, column), "type": ttype},
        }
        hit = True
        logger.debug("%s: %s.%s <- %s", path, r_name, m_name, kind)
    if not hit:
        logger.warning("no resource method references %s %s", verb.upper(), path)
    return hit


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

    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    fixes = config.get("fixes") or []
    by_service: Dict[str, List[dict]] = {}
    for f in fixes:
        by_service.setdefault(f["service"], []).append(f)

    services_dir = Path(args.provider_dir) / "services"
    total = 0
    for svc, svc_fixes in sorted(by_service.items()):
        svc_path = services_dir / f"{svc}.yaml"
        if not svc_path.exists():
            logger.warning("service yaml missing: %s", svc_path)
            continue
        spec = yaml.safe_load(svc_path.read_text(encoding="utf-8"))
        applied = sum(1 for f in svc_fixes if apply_fix(spec, f))
        if applied:
            with svc_path.open("w", encoding="utf-8") as fh:
                yaml.safe_dump(spec, fh, sort_keys=False, default_flow_style=False, width=1000)
            logger.info("%s: applied %d/%d fixes", svc, applied, len(svc_fixes))
            total += applied
    logger.info("Applied %d response fixes.", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
