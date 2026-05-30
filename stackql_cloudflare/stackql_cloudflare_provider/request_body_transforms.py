"""Attach `request.transform` blocks to write-method resource entries whose
request bodies contain array- or object-typed properties.

Why: stackql's `naive` requestBodyTranslate algorithm builds a body map
out of the SET clause, keeping every value as the Go type stackql
parsed it as. For string-typed schema fields that round-trips through
`json.Marshal` correctly. For array- or object-typed fields, the SET
literal is kept as a Go string and `json.Marshal` emits it
string-wrapped on the wire:

    SET rules = '[{...}]'   ->   {"rules": "[{...}]"}   (rejected)

Cloudflare correctly rejects the string-wrapped form with HTTP 400:
`invalid JSON: 'rules' cannot be a string`. This affects every write
endpoint with at least one array or object property in its body schema
(~400 operations across the provider, including rulesets, dns records,
load balancers, page rules, workers bindings, etc.).

The fix is a per-method `request.transform` block that rebuilds the
body, treating each array- or object-typed property with the dual-mode
"if string then splat verbatim, else toJson" pattern (handling both the
raw SET literal AND the post-decode parsed slice/map). Scalar
properties get plain `toJson` for proper escaping. Properties that
weren't SET are skipped via `{{ if .X }}` so the wire body matches
exactly what the user asked for.

The template uses `kindOf`, `eq`, `toJson` plus standard Go template
builtins (`if`, `else`, variable rebinding) - all available under
`golang_template_json_v0.3.0` per any-sdk.

This step runs after `generate-provider` because the resource method
entries (where `request` lives) are written by the generator.
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

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
_COMPLEX_TYPES = ("array", "object")


def _resolve_ref(ref: str, schemas: Dict[str, Any]) -> Optional[dict]:
    prefix = "#/components/schemas/"
    if not ref.startswith(prefix):
        return None
    return schemas.get(ref[len(prefix):])


def _prop_type(prop: Any, schemas: Dict[str, Any], seen: Optional[Set[int]] = None) -> str:
    """Return the OpenAPI primitive type of a property, following one or
    two $ref hops if needed. 'unknown' if it can't be determined."""
    if not isinstance(prop, dict):
        return "unknown"
    if "type" in prop and prop["type"]:
        return prop["type"]
    ref = prop.get("$ref")
    if isinstance(ref, str):
        if seen is None:
            seen = set()
        rid = id(ref)
        if rid in seen:
            return "unknown"
        seen.add(rid)
        target = _resolve_ref(ref, schemas)
        if isinstance(target, dict):
            return _prop_type(target, schemas, seen)
    # Schemas that have `properties` but no `type` are by convention objects.
    if isinstance(prop.get("properties"), dict):
        return "object"
    if isinstance(prop.get("items"), dict):
        return "array"
    return "unknown"


def _is_read_only(prop: Any, schemas: Dict[str, Any]) -> bool:
    """A property is readOnly if it carries `readOnly: true` directly, or
    its $ref target does. Used to skip readOnly fields from write-body
    transforms: even if a user accidentally SETs them, they should not
    be sent to the server (which would reject with `unknown field`)."""
    if not isinstance(prop, dict):
        return False
    if prop.get("readOnly") is True:
        return True
    ref = prop.get("$ref")
    if isinstance(ref, str):
        target = _resolve_ref(ref, schemas)
        if isinstance(target, dict) and target.get("readOnly") is True:
            return True
    return False


def _classify_body_props(schema: Any, schemas: Dict[str, Any]) -> List[Tuple[str, str]]:
    """Return [(prop_name, classification), ...] for a request body schema,
    where classification is one of: 'complex' (array/object/$ref-to-either),
    'scalar' (string/number/integer/boolean), or 'unknown' (skip).

    readOnly properties are filtered out: even though they appear in the
    schema (so the docgen Fields table can show them on the response
    side), they must not be sent on write requests.

    We follow exactly one $ref hop on the top-level schema in case the
    whole body is a $ref to a component schema.
    """
    if not isinstance(schema, dict):
        return []
    # Top-level $ref: follow it once.
    if "$ref" in schema and isinstance(schema["$ref"], str):
        target = _resolve_ref(schema["$ref"], schemas)
        if isinstance(target, dict):
            schema = target
    props = schema.get("properties") or {}
    if not isinstance(props, dict):
        return []
    out: List[Tuple[str, str]] = []
    for name, p in props.items():
        if _is_read_only(p, schemas):
            continue
        t = _prop_type(p, schemas)
        if t in _COMPLEX_TYPES:
            out.append((name, "complex"))
        elif t in ("string", "number", "integer", "boolean"):
            out.append((name, "scalar"))
        else:
            out.append((name, "unknown"))
    return out


def _build_transform_body(props: List[Tuple[str, str]]) -> Optional[str]:
    """Build the Go template body string. Returns None if no complex props
    are present (no transform needed - naive translation is correct).

    The template iterates over schema-declared properties (not over the
    body map), so unknown / experimental SET keys won't appear in the
    output. That's intentional: it keeps the wire body strictly within
    the schema contract and prevents users from accidentally re-sending
    readOnly fields like `id`/`version`/`last_updated`.
    """
    # If there's no complex (array/object) property, the naive translator
    # already produces correct JSON - no transform needed.
    if not any(c == "complex" for _, c in props):
        return None

    lines = ["{"]
    lines.append('{{- $sep := "" -}}')
    for name, kind in props:
        if kind == "unknown":
            # Skip - we don't know how to serialise it safely.
            continue
        # Each property is guarded by `{{ if .name }}` so absent SET keys
        # don't appear in the body. We rebind $sep to "," after the first
        # emission to manage commas.
        if kind == "complex":
            value_expr = (
                '{{ if eq (kindOf .' + name + ') "string" }}'
                '{{ .' + name + ' }}'
                '{{ else }}'
                '{{ toJson .' + name + ' }}'
                '{{ end }}'
            )
        else:  # scalar
            value_expr = '{{ toJson .' + name + ' }}'
        lines.append(
            '{{- if .' + name + ' }}{{ $sep }}"' + name + '": ' + value_expr +
            '{{- $sep = "," -}}{{ end }}'
        )
    lines.append("}")
    return "\n".join(lines) + "\n"


def _op_ref_to_path_verb(op_ref: str) -> Tuple[str, str]:
    parts = op_ref.split("/")
    verb = parts[-1]
    encoded = "/".join(parts[2:-1])
    path = encoded.replace("~1", "/")
    return path, verb


def _build_path_verb_to_body_props(source_spec: dict) -> Dict[Tuple[str, str], List[Tuple[str, str]]]:
    """For one source service spec, return a (path, verb) -> [(prop, kind)] map
    for every write-verb op that has a JSON request body."""
    schemas = (source_spec.get("components") or {}).get("schemas") or {}
    out: Dict[Tuple[str, str], List[Tuple[str, str]]] = {}
    for path, item in (source_spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for verb in _WRITE_VERBS:
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            rb = op.get("requestBody") or {}
            content = rb.get("content") or {}
            # Prefer application/json; fall back to first content type if absent.
            mt_spec = content.get("application/json") or next(iter(content.values()), None)
            if not isinstance(mt_spec, dict):
                continue
            schema = mt_spec.get("schema") or {}
            props = _classify_body_props(schema, schemas)
            if props:
                out[(path, verb)] = props
    return out


def process_service_file(generated_path: Path, source_path: Path) -> Dict[str, int]:
    """Walk one generated service yaml and attach request.transform blocks
    to any write-method whose body has at least one array/object property.
    Mutates in place."""
    source_spec = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    if not isinstance(source_spec, dict):
        return {"methods": 0}
    path_verb_to_props = _build_path_verb_to_body_props(source_spec)
    if not path_verb_to_props:
        return {"methods": 0}

    generated_spec = yaml.safe_load(generated_path.read_text(encoding="utf-8"))
    if not isinstance(generated_spec, dict):
        return {"methods": 0}

    resources = ((generated_spec.get("components") or {}).get("x-stackQL-resources") or {})
    method_count = 0

    for r_name, r in resources.items():
        methods = r.get("methods") or {}
        for m_name, m in methods.items():
            op_ref = ((m.get("operation") or {}).get("$ref") or "")
            if not op_ref:
                continue
            try:
                p, v = _op_ref_to_path_verb(op_ref)
            except Exception:
                continue
            if v not in _WRITE_VERBS:
                continue
            props = path_verb_to_props.get((p, v))
            if not props:
                continue
            body = _build_transform_body(props)
            if body is None:
                continue
            # Don't clobber a pre-existing request block (e.g. hand-edited).
            if "request" in m:
                continue
            m["request"] = {
                "mediaType": "application/json",
                "transform": {
                    "type": "golang_template_json_v0.3.0",
                    "body": body,
                },
            }
            method_count += 1

    if method_count:
        with generated_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(generated_spec, f, sort_keys=False, default_flow_style=False, width=1000)

    return {"methods": method_count}


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider-dir", default=str(PROVIDER_DIR),
                        help=f"Provider root containing services/. Default: {PROVIDER_DIR}")
    parser.add_argument("--source-dir", default=str(SOURCE_DIR),
                        help=f"Source yamls dir (for schema lookup). Default: {SOURCE_DIR}")
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
            logger.debug("No source spec for %s - skipping.", generated_path.name)
            continue
        stats = process_service_file(generated_path, source_path)
        if stats["methods"]:
            touched_files += 1
            total_methods += stats["methods"]
            logger.debug("%s: attached request.transform to %d methods", generated_path.name, stats["methods"])

    logger.info("Attached request.transform to %d write methods across %d files.",
                total_methods, touched_files)
    return 0


if __name__ == "__main__":
    sys.exit(main())
