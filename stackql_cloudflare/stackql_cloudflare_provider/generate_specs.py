"""CLI: split the upstream Cloudflare OpenAPI spec into per-service yamls
that mirror the Cloudflare Python SDK's resources/ hierarchy, normalize
polymorphism, and write the results under provider-dev/source/.

Usage:
    python -m stackql_cloudflare_provider.generate_specs              # all services
    python -m stackql_cloudflare_provider.generate_specs -s zones     # one service
    python -m stackql_cloudflare_provider.generate_specs --refresh    # re-download spec
"""
from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
import urllib.request
from pathlib import Path

import yaml

from .canonical_params import normalize_path_params
from .fanout import fanout_dual_scope_paths
from .normalize import normalize_schemas, normalize_inline, fix_required_without_properties
from .rename import rename_schemas_to_camel, rename_path_params_to_snake
from .sdk_index import build_sdk_index, build_path_to_service_index
from .split import (
    _service_filename,
    assign_paths_to_services,
    build_service_spec,
)


logger = logging.getLogger(__name__)


# Resolved relative to repo root: <repo>/stackql_cloudflare/
PKG_DIR = Path(__file__).resolve().parent
PROVIDER_DEV_DIR = PKG_DIR.parent / "provider-dev"
REPO_ROOT = PKG_DIR.parent.parent
SDK_ROOT = REPO_ROOT / "src" / "cloudflare"
STATS_YML = REPO_ROOT / ".stats.yml"

DOWNLOADS_DIR = PROVIDER_DEV_DIR / "downloads"
SOURCE_DIR = PROVIDER_DEV_DIR / "source"


def _read_stats_url() -> str:
    text = STATS_YML.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    url = data.get("openapi_spec_url")
    if not url:
        raise RuntimeError(f"No openapi_spec_url in {STATS_YML}")
    return url


def _download_spec(url: str, dest: Path) -> None:
    logger.info("Downloading Cloudflare OpenAPI spec from %s", url)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as resp, dest.open("wb") as out:
        shutil.copyfileobj(resp, out)
    logger.info("Saved %s (%.1f MB)", dest, dest.stat().st_size / (1024 * 1024))


def _load_spec(refresh: bool) -> dict:
    dest = DOWNLOADS_DIR / "cloudflare-openapi.json"
    legacy = DOWNLOADS_DIR / "cloudflare-openapi.yaml"
    if not dest.exists() and legacy.exists():
        # The stainless URL serves JSON despite the .yml suffix; keep both names.
        dest = legacy
    if refresh or not dest.exists():
        url = _read_stats_url()
        _download_spec(url, dest)
    logger.info("Loading spec from %s", dest)
    text = dest.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return yaml.safe_load(text)


def _flatten_descriptions(spec: dict) -> int:
    """Flatten multi-line `description` / `summary` strings into a single
    line, so downstream docgen doesn't convert each `\\n` to `<br />`.

    Why: docgen's helpers.js `sanitizeHtml` runs `.replace(/\\n/g, '<br />')`
    on every description before injecting it into table cells. That works
    for a one-paragraph description but produces a wall of `<br />` tags
    when the description is multi-paragraph (e.g. /zones/{id}/purge_cache
    has a 40-line description). The HTML5 minifier then complains about
    each `<br></br>` close-tag pair in the rendered output.

    Our solution: collapse to single-line at the source. We lose multi-
    paragraph rendering in the description body, but gain a clean build.
    Headings (`### Section`) become `**Section**:` so the visual emphasis
    survives but doesn't break the inline flow.

    Returns the count of fields touched.
    """
    import re as _re
    n = 0

    def flatten(text: str) -> str:
        if not isinstance(text, str) or not text.strip():
            return text
        # Drop markdown headings - their `###` markers don't make sense
        # inline. Convert them to bold-emphasised inline labels.
        out = _re.sub(r"^\s*#{1,6}\s+(.+?)\s*$", r"**\1:**", text, flags=_re.MULTILINE)
        # Collapse all runs of whitespace (incl. \r\n, \n, tabs) to a
        # single space.
        out = _re.sub(r"\s+", " ", out)
        return out.strip()

    def walk(node, parent_key=None):
        nonlocal n
        if isinstance(node, dict):
            for k, v in list(node.items()):
                if k in ("description", "summary") and isinstance(v, str):
                    new = flatten(v)
                    if new != v:
                        node[k] = new
                        n += 1
                else:
                    walk(v, k)
        elif isinstance(node, list):
            for item in node:
                walk(item, parent_key)

    walk(spec)
    return n


def _inline_parameter_refs(spec: dict) -> None:
    """Make every operation's `parameters` list fully self-contained:

    1. Inline any {'$ref': '#/components/parameters/X'} reference.
    2. Merge path-item-level `parameters` into each operation's list, so
       every operation owns its own complete parameter set.
    3. Drop the (now-redundant) path-item-level parameters array.

    We dedupe merged parameters by (name, in) - operation-level parameters
    take precedence over the path-item-level inheritance per OpenAPI 3.0.
    `components/parameters` is dropped wholesale by the splitter once every
    reference is inlined.
    """
    import copy as _copy
    components_parameters = (spec.get("components") or {}).get("parameters") or {}
    prefix = "#/components/parameters/"

    def resolve(p):
        if isinstance(p, dict) and isinstance(p.get("$ref"), str) and p["$ref"].startswith(prefix):
            name = p["$ref"][len(prefix):]
            target = components_parameters.get(name)
            if isinstance(target, dict):
                return _copy.deepcopy(target)
        return p

    for path, item in spec.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        # Resolve any path-item-level parameters first.
        shared = item.get("parameters") or []
        shared_resolved = [resolve(p) for p in shared if isinstance(p, dict)]
        for verb in ("get", "put", "post", "delete", "patch", "options", "head"):
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            op_params = op.get("parameters") or []
            op_resolved = [resolve(p) for p in op_params if isinstance(p, dict)]
            # Operation-level params win on (name, in) collisions.
            seen = {(p.get("name"), p.get("in")) for p in op_resolved}
            merged = list(op_resolved)
            for sp in shared_resolved:
                key = (sp.get("name"), sp.get("in"))
                if key not in seen:
                    merged.append(_copy.deepcopy(sp))
                    seen.add(key)
            if merged:
                op["parameters"] = merged
        # Drop the path-item-level parameters array now that it's been merged.
        if "parameters" in item:
            del item["parameters"]


def _inline_response_and_request_body_refs(spec: dict) -> None:
    """Walk every operation and inline any:
      - {'$ref': '#/components/responses/X'} (whole response object)
      - {'$ref': '#/components/requestBodies/X'} (whole requestBody object)
    Per the splitter we only carry components/schemas and securitySchemes
    forward into each service spec, so these refs would otherwise dangle.
    Schema-level $refs inside the response/requestBody are left alone - they
    point at components/schemas, which the splitter does include transitively.
    """
    import copy as _copy
    comps = spec.get("components") or {}
    components_responses = comps.get("responses") or {}
    components_request_bodies = comps.get("requestBodies") or {}
    resp_prefix = "#/components/responses/"
    rb_prefix = "#/components/requestBodies/"

    if not components_responses and not components_request_bodies:
        return

    def maybe_inline_response(node):
        if isinstance(node, dict) and isinstance(node.get("$ref"), str) and node["$ref"].startswith(resp_prefix):
            name = node["$ref"][len(resp_prefix):]
            target = components_responses.get(name)
            if isinstance(target, dict):
                return _copy.deepcopy(target)
        return node

    def maybe_inline_request_body(node):
        if isinstance(node, dict) and isinstance(node.get("$ref"), str) and node["$ref"].startswith(rb_prefix):
            name = node["$ref"][len(rb_prefix):]
            target = components_request_bodies.get(name)
            if isinstance(target, dict):
                return _copy.deepcopy(target)
        return node

    for path, item in spec.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        for verb in ("get", "put", "post", "delete", "patch", "options", "head"):
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            # responses block
            responses = op.get("responses") or {}
            if isinstance(responses, dict):
                for code, resp in list(responses.items()):
                    responses[code] = maybe_inline_response(resp)
            # requestBody
            rb = op.get("requestBody")
            if rb is not None:
                op["requestBody"] = maybe_inline_request_body(rb)


def _normalize_paths_inline(spec: dict) -> None:
    """Apply polymorphism flattening to inline schemas inside paths (parameters,
    request bodies, response bodies)."""
    schemas = spec.get("components", {}).get("schemas", {})
    for path, item in spec.get("paths", {}).items():
        for verb in ("get", "put", "post", "delete", "patch", "options", "head"):
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            for param in op.get("parameters", []) or []:
                if "schema" in param:
                    param["schema"] = normalize_inline(param["schema"], schemas)
            rb = op.get("requestBody")
            if isinstance(rb, dict):
                for mt in rb.get("content", {}).values():
                    if "schema" in mt:
                        mt["schema"] = normalize_inline(mt["schema"], schemas)
            for resp in op.get("responses", {}).values():
                if not isinstance(resp, dict):
                    continue
                for mt in resp.get("content", {}).values():
                    if "schema" in mt:
                        mt["schema"] = normalize_inline(mt["schema"], schemas)


_LIST_ENVELOPE_KEYS = ("result", "items", "data", "records")


def _hoist_inline_list_items(spec: dict) -> int:
    """Find component schemas whose envelope (`result`/`items`/`data`/`records`)
    holds `items: { type: object, properties: {...} }` inline, hoist that
    inline object into `components/schemas` with a synthesized name, and
    replace the inline definition with a `$ref`.

    Why: downstream `@stackql/provider-utils.docgen` follows `result.items.$ref`
    to derive the columns rendered in each resource's Fields table. If
    `items` is an inline object schema, no `$ref` exists and the Fields
    table is empty.

    Returns the count of inline item-schemas hoisted.
    """
    import copy as _copy
    schemas = (spec.get("components") or {}).get("schemas") or {}
    if not schemas:
        return 0

    n = 0
    # Snapshot the names we iterate over; we mutate `schemas` in the loop.
    for outer_name in list(schemas.keys()):
        outer = schemas[outer_name]
        if not isinstance(outer, dict):
            continue
        props = outer.get("properties") or {}
        if not isinstance(props, dict):
            continue
        for env_key in _LIST_ENVELOPE_KEYS:
            env = props.get(env_key)
            if not isinstance(env, dict):
                continue
            items = env.get("items")
            # Skip if there's no items or it's already a ref.
            if not isinstance(items, dict):
                continue
            if "$ref" in items:
                continue
            # Only hoist inline OBJECT schemas (with properties or items of their own).
            if not items.get("properties") and not items.get("items"):
                continue
            # Synthesize a stable name: outer name + envelope + "_item".
            base = f"{outer_name}_{env_key}_item"
            new_name = base
            i = 2
            while new_name in schemas:
                new_name = f"{base}_{i}"
                i += 1
            # Hoist.
            schemas[new_name] = _copy.deepcopy(items)
            env["items"] = {"$ref": f"#/components/schemas/{new_name}"}
            n += 1

    return n


# YAML 1.1 truthy/falsy barewords. PyYAML emits YAML 1.2, where these are
# plain strings - but the Go go-openapi3 library used by stackql parses YAML
# 1.1, where unquoted `y`/`n`/`on`/`off`/etc decode to booleans. That trips
# unmarshaling for any `required: [- x, - y, - ...]` list that contains one.
# Force-quote them on the way out.
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


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False, width=1000)


def generate(only_service: str | None = None, refresh: bool = False, clean: bool = False) -> int:
    spec = _load_spec(refresh=refresh)
    schemas = spec.get("components", {}).get("schemas", {})
    logger.info("Loaded spec: %d paths, %d schemas", len(spec.get("paths", {})), len(schemas))

    logger.info("Fanning out dual-scope /{accounts_or_zones}/{account_or_zone_id}/... paths into separate /accounts and /zones paths...")
    added = fanout_dual_scope_paths(spec)
    logger.info("  fan-out added %d new paths", added)
    logger.info("Flattening multi-line description/summary strings to single line...")
    n = _flatten_descriptions(spec)
    logger.info("  flattened %d description/summary fields", n)
    logger.info("Inlining components/parameters $refs into each operation...")
    _inline_parameter_refs(spec)
    logger.info("Inlining components/responses and components/requestBodies $refs into each operation...")
    _inline_response_and_request_body_refs(spec)
    logger.info("Renaming path parameters to snake_case (path templates + parameters[].name)...")
    n = rename_path_params_to_snake(spec)
    logger.info("  renamed %d path-param occurrences", n)
    logger.info("Renaming component schemas to camelCase (with $ref rewrites)...")
    n = rename_schemas_to_camel(spec)
    logger.info("  renamed %d schema names", n)
    # Re-read schemas after rename - the dict was rebuilt.
    schemas = spec.get("components", {}).get("schemas", {})
    logger.info("Normalizing component schemas (flatten allOf, collapse oneOf/anyOf, strip additionalProperties)...")
    normalize_schemas(schemas)
    logger.info("Normalizing inline path schemas...")
    _normalize_paths_inline(spec)
    logger.info("Dropping `required` from objects with no `properties`...")
    fix_required_without_properties(spec)
    logger.info("Hoisting inline result.items objects to named component schemas...")
    n = _hoist_inline_list_items(spec)
    logger.info("  hoisted %d inline list-item schemas", n)
    logger.info("Normalising canonical path parameters (account_id, zone_id, etc.)...")
    n = normalize_path_params(spec)
    logger.info("  normalised %d path parameters", n)

    logger.info("Indexing SDK at %s ...", SDK_ROOT)
    sdk_ops = build_sdk_index(SDK_ROOT)
    sdk_idx = build_path_to_service_index(sdk_ops)
    logger.info("Indexed %d SDK call sites, %d unique (verb,path) pairs", len(sdk_ops), len(sdk_idx))

    logger.info("Assigning paths to services...")
    by_service, unmatched = assign_paths_to_services(spec, sdk_ops)
    logger.info("Assigned to %d services. %d paths fell back to URL-prefix heuristic.",
                len(by_service), len(unmatched))
    if unmatched and logger.isEnabledFor(logging.DEBUG):
        for p in unmatched[:30]:
            logger.debug("  unmapped path: %s", p)

    if clean and SOURCE_DIR.exists():
        for f in SOURCE_DIR.glob("*.yaml"):
            f.unlink()

    base_info = spec.get("info", {})
    servers = spec.get("servers") or [{"url": "https://api.cloudflare.com/client/v4"}]
    security_schemes = spec.get("components", {}).get("securitySchemes", {})

    written = 0
    for service, paths in sorted(by_service.items()):
        if only_service and service != only_service:
            continue
        out = build_service_spec(
            service=service,
            paths=paths,
            schemas=schemas,
            base_info=base_info,
            servers=servers,
            security_schemes=security_schemes,
            sdk_idx=sdk_idx,
        )
        out_path = SOURCE_DIR / _service_filename(service)
        _write_yaml(out_path, out)
        written += 1
        logger.info("Wrote %s (%d paths, %d schemas)",
                    out_path.relative_to(PROVIDER_DEV_DIR),
                    len(paths),
                    len(out["components"]["schemas"]))

    logger.info("Done. Wrote %d service specs to %s", written, SOURCE_DIR)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-s", "--service", help="Only generate this service")
    parser.add_argument("--refresh", action="store_true", help="Re-download the upstream OpenAPI spec")
    parser.add_argument("--clean", action="store_true", help="Delete all existing source/*.yaml before generating")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    return generate(only_service=args.service, refresh=args.refresh, clean=args.clean)


if __name__ == "__main__":
    sys.exit(main())
