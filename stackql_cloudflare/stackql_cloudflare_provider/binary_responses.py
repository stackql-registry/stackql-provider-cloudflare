"""Wrap non-JSON-projectable responses so StackQL can SELECT them.

Cloudflare exposes a number of endpoints that return binary payloads or
plain-text bodies - PDFs, PNG screenshots, raw script content, LOA
documents, CSV exports, etc. These have response media types like
`application/pdf`, `image/png`, `application/octet-stream`, `text/plain`,
or Cloudflare's synthetic `string` type. Without intervention StackQL
either refuses to project the response (no JSON schema) or errors at
DESCRIBE time.

This module post-processes the generated provider yamls and:

  1. Detects operations whose 2xx response is non-JSON / opaque.
  2. Rewrites the operation's response definition itself to:
        responses:
          '200':
            content:
              <original-mediaType>:
                schema:
                  type: object
                  properties:
                    contents:
                      type: string
     This makes the schema "look like" a JSON object with a single
     `contents` column.
  3. Attaches a stackql `response.transform` to the corresponding
     resource method that pulls the raw body into a one-row table with
     the same column shape via a Go template.

Result: callers can run

    SELECT contents FROM cloudflare.<service>.<resource>
    WHERE <required params> ...;

and get the raw payload as a string column.

This step runs after `generate-provider` because the resource method
entries (where `response` lives) are written by the generator.
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


logger = logging.getLogger(__name__)


# YAML 1.1 truthy/falsy barewords. PyYAML emits YAML 1.2, where these are
# plain strings - but the Go go-openapi3 library used by stackql parses YAML
# 1.1, where unquoted `y`/`n`/`on`/`off`/etc decode to booleans. That trips
# unmarshaling for `required: [..., y, ...]` style lists. Force-quote them.
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


# Media types we treat as "raw binary or plain-text". Anything in this set
# (or anything that isn't JSON) on a 2xx response triggers the wrap.
_JSON_MEDIA_TYPES = ("application/json", "application/json; charset=utf-8")


def _success_response(op: dict) -> Tuple[str, dict, str, dict]:
    """Return (code, response, media_type, content_entry) for the first 2xx
    response. Empty strings/dicts if missing."""
    for code, resp in (op.get("responses") or {}).items():
        if not str(code).startswith("2"):
            continue
        if not isinstance(resp, dict):
            return "", {}, "", {}
        content = resp.get("content") or {}
        if not content:
            return code, resp, "", {}
        # Prefer the first declared media type.
        mt_name = next(iter(content.keys()))
        return code, resp, mt_name, content[mt_name] or {}
    return "", {}, "", {}


def _is_binary_response(op: dict) -> Optional[str]:
    """Return the non-JSON media type if the operation's success response
    is binary/raw; else None."""
    _, _, mt, mt_entry = _success_response(op)
    if not mt:
        return None
    if mt in _JSON_MEDIA_TYPES:
        return None
    # If the schema is already a projectable JSON object via the wrap we've
    # applied previously, skip.
    sch = (mt_entry or {}).get("schema") or {}
    if isinstance(sch, dict) and sch.get("properties", {}).get("contents") and sch.get("type") == "object":
        return None
    return mt


def _wrap_op_response(op: dict, mediaType: str) -> None:
    """Mutate the operation in place so its 2xx response declares a
    `{contents: string}` JSON-shaped wrapper schema under the original
    media type."""
    for code, resp in (op.get("responses") or {}).items():
        if not str(code).startswith("2"):
            continue
        if not isinstance(resp, dict):
            continue
        resp["content"] = {
            mediaType: {
                "schema": {
                    "type": "object",
                    "properties": {
                        "contents": {"type": "string"},
                    },
                },
            },
        }
        return


def _method_response_transform(media_type: str) -> Dict[str, Any]:
    """Build the stackql `response` block that wraps the raw body into a
    one-row table with a single `contents` column."""
    return {
        "mediaType": media_type,
        "openAPIDocKey": "200",
        "overrideMediaType": "application/json",
        "transform": {
            "body": "[{\"contents\": {{ toJson . }}}]",
            "type": "golang_template_text_v0.3.0",
        },
    }


def _op_ref_to_path_verb(op_ref: str) -> Tuple[str, str]:
    """Decode a `#/paths/<encoded>/<verb>` ref into (path, verb)."""
    parts = op_ref.split("/")
    verb = parts[-1]
    encoded = "/".join(parts[2:-1])
    path = encoded.replace("~1", "/")
    return path, verb


def process_service_file(yaml_path: Path) -> Dict[str, int]:
    """Walk one service yaml and wrap every method whose underlying operation
    has a non-JSON success response. Mutates the file in place."""
    spec = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(spec, dict):
        return {"ops": 0, "methods": 0}

    paths = spec.get("paths") or {}
    resources = ((spec.get("components") or {}).get("x-stackQL-resources") or {})

    op_count = 0
    method_count = 0

    # Pass 1: discover which (path, verb) tuples need wrapping, mutate
    # the op's response schema in-place.
    needs_wrap: Dict[Tuple[str, str], str] = {}
    for path, item in paths.items():
        if not isinstance(item, dict):
            continue
        for verb in ("get", "put", "post", "delete", "patch"):
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            mt = _is_binary_response(op)
            if mt:
                _wrap_op_response(op, mt)
                needs_wrap[(path, verb)] = mt
                op_count += 1

    # Pass 2: attach the response.transform to any resource method whose
    # operation $ref points at a wrapped op.
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
            mt = needs_wrap.get((p, v))
            if not mt:
                continue
            m["response"] = _method_response_transform(mt)
            method_count += 1

    if op_count or method_count:
        with yaml_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(spec, f, sort_keys=False, default_flow_style=False, width=1000)

    return {"ops": op_count, "methods": method_count}


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider-dir", default=str(PROVIDER_DIR),
                        help=f"Provider root containing services/. Default: {PROVIDER_DIR}")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    services_dir = Path(args.provider_dir) / "services"
    if not services_dir.exists():
        logger.error("services/ dir not found at %s. Run `npm run generate-provider` first.", services_dir)
        return 1

    total_ops = 0
    total_methods = 0
    touched_files = 0
    for yaml_path in sorted(services_dir.glob("*.yaml")):
        stats = process_service_file(yaml_path)
        if stats["ops"] or stats["methods"]:
            touched_files += 1
            total_ops += stats["ops"]
            total_methods += stats["methods"]
            logger.debug("%s: wrapped %d ops, %d methods", yaml_path.name, stats["ops"], stats["methods"])

    logger.info("Wrapped %d binary responses across %d files (%d resource methods got response.transform).",
                total_ops, touched_files, total_methods)
    return 0


if __name__ == "__main__":
    sys.exit(main())
