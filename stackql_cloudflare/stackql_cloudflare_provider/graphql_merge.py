"""Shim Cloudflare GraphQL operations into the final-output stackql provider.

GraphQL operations are not derivable from Cloudflare's upstream OpenAPI spec
(which is REST-only). They are hand-authored under
`provider-dev/source-graphql/`:

  manifest.yaml          - one entry per operation (field, scope, service,
                           resource, method, spec, optional replaces_rest)
  ops/<name>.yaml        - the per-op spec: parameters, GraphQL query
                           template, response.transform, post-transform
                           row_schema

This module runs as a post-pass after `npm run generate-provider` and
shims each manifest entry into the matching final-output service yaml at
  provider-dev/openapi/src/cloudflare/v00.00.00000/services/<service>.yaml

Specifically it:
  1. Synthesises an OpenAPI path `/graphql/<resource>` with a POST
     operation carrying the x-stackQL-graphQL extension, parameters,
     and a post-transform response schema.
  2. Adds a x-stackQL-resources resource entry pointing at that path,
     with the response.transform attached and method marked
     `x-stackql-protocol: graphql`.

REST endpoints listed in a manifest entry's `replaces_rest` block are
stripped by `strip_superseded_rest.py` (a pre-pass that runs at the top
of `generate-provider.mjs`), so they never reach the downstream
provider or docs. This module does not touch them.

Idempotent: re-running the merge replaces any previously-shimmed paths
and resource methods cleanly. Detection is by the `x-stackql-protocol`
marker on the resource method (and synthetic `/graphql/...` path keys).
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


# YAML 1.1 truthy/falsy barewords (same dumper guard as the other passes).
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
PROVIDER_DEV = PKG_DIR.parent / "provider-dev"
SOURCE_GRAPHQL = PROVIDER_DEV / "source-graphql"
SERVICES_DIR = (
    PROVIDER_DEV / "openapi" / "src" / "cloudflare" / "v00.00.00000" / "services"
)

CLOUDFLARE_GRAPHQL_URL = "https://api.cloudflare.com/client/v4/graphql"

# DEBUG: when set via --webhook-url, every shimmed operation's
# x-stackQL-graphQL.url points here instead of Cloudflare. The body
# stackql actually sent is then visible in the webhook capture page.
# Remove the override (re-merge without the flag) once debugging is done.
_DEBUG_URL_OVERRIDE: Optional[str] = None

# Identifies a shimmed-in GraphQL method. Placed on the resource method
# block AND the OpenAPI operation extension. The post-docgen sanitiser
# greps for it.
PROTOCOL_MARKER_KEY = "x-stackql-protocol"
PROTOCOL_MARKER_VAL = "graphql"


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _dump_yaml(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False, width=1000)


def _synthetic_path(resource: str) -> str:
    """Synthetic OpenAPI path key for a GraphQL resource.

    OpenAPI 3 requires (path, verb) uniqueness; all our GraphQL ops POST
    to the same wire URL, so we use a synthetic path that embeds the
    resource name. The leading `/graphql/` segment makes them grep-able
    and identifies them as not-REST without affecting the actual HTTP
    call (the real URL lives in x-stackQL-graphQL.url).
    """
    return f"/graphql/{resource}"


def _path_ref(path: str) -> str:
    """Encode an OpenAPI path for use in a $ref (slashes become ~1)."""
    return path.replace("/", "~1")


def _scope_filter(scope: str, param_name: str = "zone_tag") -> Tuple[str, str]:
    """Return (viewer_wrapper_open, viewer_wrapper_close) for a scope.

    Not currently used (ops author the full query template themselves),
    but reserved for a future templating convenience.
    """
    if scope == "zone":
        return (
            f'viewer {{ zones(filter: {{ zoneTag: "{{{{ .{param_name} }}}}" }}, limit: 1) {{',
            "} }",
        )
    return (
        f'viewer {{ accounts(filter: {{ accountTag: "{{{{ .{param_name} }}}}" }}, limit: 1) {{',
        "} }",
    )


# Debug toggle: when True, every shimmed op gets a trivial transform
# that wraps the entire upstream response in one row + one `raw` column.
# Pinpoints whether the issue is the transform body, the dispatch, or
# Cloudflare returning unexpected data. Set via --naked CLI flag.
_NAKED_RESPONSE: bool = False


def _naked_transform(resource: str) -> dict:
    """Always-safe debug transform: wraps the whole upstream response
    into one row with a single `raw` JSON-string column. No path walking,
    no null traversal - if the upstream is reachable at all, this
    produces a row."""
    return {
        "type": "golang_template_json_v0.3.0",
        "body": (
            "{\n"
            f'  "data": {{\n'
            f'    "{resource}": [\n'
            "      { \"raw\": {{ toJson . | toJson }} }\n"
            "    ]\n"
            "  }\n"
            "}\n"
        ),
    }


def _naked_row_schema() -> dict:
    return {
        "type": "object",
        "properties": {
            "raw": {"type": "string"},
        },
    }


def _build_cursor(spec: dict) -> dict:
    """Build the x-stackQL-graphQL.cursor block for one operation.

    If the op spec declares a `cursor:` block, pass it through verbatim.
    The any-sdk cursor strategies (per stackql PR #658 / any-sdk
    pkg/graphql/graphql.go) are:

      cursor_after  (default; classic Relay `after:` cursor)
      keyset        (Cloudflare-style: `_gt` / `_geq` filter on sort key)
      offset        (offset/limit style)
      page_info     (Relay-strict; reads `hasNextPage` from response)

    Expected per-strategy fields in the op spec's cursor block:

      strategy: cursor_after | keyset | offset | page_info
      jsonPath: <path-to-cursor-value>     (required for after/keyset/page_info)
      format: <Go text/template>           (required for keyset; optional otherwise)
      terminateOnJsonPath: <path>          (required for page_info)
      pageSize: <int>                      (optional; offset only)

    If the spec omits `cursor:`, fall back to a single-page sentinel
    (`$.result[*].__no_cursor`) - any-sdk treats a failed jsonpath
    lookup as EOF, so iteration terminates after page 1. This is the
    behavior every op shipped with before pagination support landed.
    """
    cursor_spec = spec.get("cursor")
    if cursor_spec:
        return cursor_spec
    return {"jsonPath": "$.result[*].__no_cursor"}


def _build_operation(entry: dict, spec: dict) -> dict:
    """Build the OpenAPI operation block for one GraphQL op.

    Goes under paths[/graphql/<resource>].post.

    Response shape mirrors Cloudflare's REST envelope convention so the
    docusaurus Fields table can resolve the row's column list:

      - The transform reshapes Cloudflare's nested response into
        `{ "result": [ ...flat rows... ] }`.
      - `responseSelection.jsonPath` AND `response.objectKey` are the
        same string: `$.result[*]`.
      - The OpenAPI response schema walks `result -> array -> items`
        with `items.properties` listing the flat row columns. Docgen's
        Fields table follows the same `result.items` path it walks for
        REST resources, so columns render correctly.

    Handles Cloudflare's two-level array nesting (`viewer.zones[*].
    <field>[*]`) by flattening in the transform; PaesslerAG/jsonpath
    does not return a flat slice across two `[*]` projections.
    """
    resource = entry["resource"]
    # The path stackql uses to project rows AND introspect the schema.
    # MUST match response.objectKey on the resource method (see
    # _build_resource_method) for any-sdk to wire them up consistently.
    raw_path = "$.result[*]"
    item_schema = _naked_row_schema() if _NAKED_RESPONSE else spec["row_schema"]
    response_schema = {
        "type": "object",
        "properties": {
            "result": {
                "type": "array",
                "items": item_schema,
            },
        },
    }
    return {
        "operationId": f"graphql-{resource}-{entry['method']}",
        "summary": spec.get("description", entry["field"]).split(".")[0],
        "description": spec.get("description", ""),
        # The x-stackQL-graphQL extension is what any-sdk's loader keys
        # off to route this operation through the GraphQL acquire path
        # instead of the REST one.
        "x-stackQL-graphQL": {
            "url": _DEBUG_URL_OVERRIDE or CLOUDFLARE_GRAPHQL_URL,
            "httpVerb": "POST",
            "responseSelection": {
                "jsonPath": raw_path,
            },
            "cursor": _build_cursor(spec),
            "query": spec["query"],
        },
        PROTOCOL_MARKER_KEY: PROTOCOL_MARKER_VAL,
        "parameters": spec["parameters"],
        "responses": {
            "200": {
                "description": "Response",
                "content": {
                    "application/json": {
                        "schema": response_schema,
                    },
                },
            },
        },
    }


def _legacy_raw_response_schema_unused(entry: dict) -> dict:
    """Kept temporarily as reference for the no-transform debug schema;
    not called. Will be removed after the trevorblades pattern is
    confirmed end-to-end against the live API.
    """
    viewer_wrapper = "zones" if entry["scope"] == "zone" else "accounts"
    return {
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "viewer": {
                        "type": "object",
                        "properties": {
                            viewer_wrapper: {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        entry["field"]: {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "dimensions": {"type": "object"},
                                                    "sum": {"type": "object"},
                                                    "count": {"type": "integer"},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


def _build_resource_method(entry: dict, spec: dict) -> dict:
    """Build the x-stackQL-resources method block for one GraphQL op.

    `objectKey: $.result` (no [*]) matches the docgen `getHttpRespBody`
    simple-objectKey branch, which walks `schema.properties.result.items.properties`
    to populate the Fields table. The any-sdk GraphQL acquire path
    reads from `responseSelection.jsonPath` (in the operation), not this
    field, so runtime row projection is unaffected by the [*] difference.
    """
    synth = _synthetic_path(entry["resource"])
    resource = entry["resource"]
    transform = _naked_transform(resource) if _NAKED_RESPONSE else spec["transform"]
    return {
        "operation": {"$ref": f"#/paths/{_path_ref(synth)}/post"},
        "response": {
            "mediaType": "application/json",
            "openAPIDocKey": "200",
            "objectKey": "$.result",
            "transform": transform,
        },
        PROTOCOL_MARKER_KEY: PROTOCOL_MARKER_VAL,
    }


def _ensure_resource(
    resources: dict, entry: dict, service: str, spec: dict
) -> dict:
    """Get or create the x-stackQL-resources entry for `resource`.

    Returns the resource dict so the caller can attach a method to it.
    """
    res_name = entry["resource"]
    if res_name in resources:
        return resources[res_name]
    title_default = res_name.replace("_", " ").title()
    resources[res_name] = {
        "id": f"cloudflare.{service}.{res_name}",
        "name": res_name,
        "title": spec.get("title", title_default),
        "methods": {},
        "sqlVerbs": {"select": [], "insert": [], "update": [], "delete": [], "replace": []},
    }
    return resources[res_name]


def _attach_sqlverb(resource: dict, method_name: str, verb: str = "select") -> None:
    """Add a $ref entry to sqlVerbs[<verb>] if not already present."""
    res_id = resource["id"]
    res_short = res_id.split(".")[-1]  # local resource name
    ref = {
        "$ref": (
            f"#/components/x-stackQL-resources/{res_short}/methods/{method_name}"
        )
    }
    bucket = resource["sqlVerbs"].setdefault(verb, [])
    for existing in bucket:
        if existing.get("$ref") == ref["$ref"]:
            return
    bucket.append(ref)


def _strip_previous_shims(service_doc: dict) -> Tuple[int, int]:
    """Remove any previously-shimmed GraphQL paths and resource methods.

    Identifies them by:
      - paths whose key starts with '/graphql/'
      - resource methods carrying x-stackql-protocol: graphql

    Returns (paths_removed, methods_removed).
    """
    paths_removed = 0
    methods_removed = 0
    paths = service_doc.get("paths") or {}
    for k in list(paths.keys()):
        if k.startswith("/graphql/"):
            del paths[k]
            paths_removed += 1
    resources = (
        service_doc.get("components", {})
        .get("x-stackQL-resources", {})
    )
    for res_name, res in list(resources.items()):
        methods = res.get("methods") or {}
        for method_name, method_body in list(methods.items()):
            if method_body.get(PROTOCOL_MARKER_KEY) == PROTOCOL_MARKER_VAL:
                del methods[method_name]
                methods_removed += 1
                # Also strip any sqlVerbs $refs pointing at this method
                ref_path = (
                    f"#/components/x-stackQL-resources/{res_name}/methods/{method_name}"
                )
                for verb_name, refs in (res.get("sqlVerbs") or {}).items():
                    res["sqlVerbs"][verb_name] = [
                        r for r in refs if r.get("$ref") != ref_path
                    ]
        # Drop resources that became empty (no methods left and were
        # created solely by a previous graphql shim).
        if not res.get("methods"):
            del resources[res_name]
    return paths_removed, methods_removed


def _load_manifest() -> List[dict]:
    manifest_path = SOURCE_GRAPHQL / "manifest.yaml"
    if not manifest_path.exists():
        return []
    data = _load_yaml(manifest_path) or {}
    return data.get("operations") or []


def _load_spec(spec_rel: str) -> dict:
    return _load_yaml(SOURCE_GRAPHQL / spec_rel)


def merge() -> int:
    operations = _load_manifest()
    if not operations:
        logger.info("No GraphQL operations declared in manifest; nothing to do.")
        return 0

    logger.info("Loaded %d GraphQL operations from manifest", len(operations))

    # Group by service so each final-output yaml is loaded once.
    by_service: Dict[str, List[dict]] = {}
    for op in operations:
        by_service.setdefault(op["service"], []).append(op)

    total_paths = 0
    total_methods = 0
    services_touched = 0

    for service, ops in sorted(by_service.items()):
        service_path = SERVICES_DIR / f"{service}.yaml"
        if not service_path.exists():
            logger.error(
                "Target service yaml does not exist: %s (referenced by ops %s)",
                service_path,
                [o["field"] for o in ops],
            )
            return 1

        doc = _load_yaml(service_path)
        if not isinstance(doc, dict):
            logger.error("Service yaml %s is not a mapping", service_path)
            return 1

        # Idempotency: strip anything we previously shimmed.
        stripped_paths, stripped_methods = _strip_previous_shims(doc)
        if stripped_paths or stripped_methods:
            logger.debug(
                "  pre-clean: removed %d previous paths and %d previous methods from %s",
                stripped_paths,
                stripped_methods,
                service_path.name,
            )

        # Ensure required containers exist.
        doc.setdefault("paths", {})
        components = doc.setdefault("components", {})
        resources = components.setdefault("x-stackQL-resources", {})

        for entry in ops:
            spec = _load_spec(entry["spec"])

            # 1. Synthetic path + OpenAPI operation
            synth = _synthetic_path(entry["resource"])
            op_block = _build_operation(entry, spec)
            doc["paths"][synth] = {"post": op_block}
            total_paths += 1

            # 2. x-stackQL-resources resource method
            resource = _ensure_resource(resources, entry, service, spec)
            resource["methods"][entry["method"]] = _build_resource_method(entry, spec)
            _attach_sqlverb(resource, entry["method"], "select")
            total_methods += 1

            logger.info(
                "  shimmed %s -> cloudflare.%s.%s.%s",
                entry["field"],
                service,
                entry["resource"],
                entry["method"],
            )

        _dump_yaml(service_path, doc)
        services_touched += 1
        logger.info("Wrote %s", service_path.relative_to(PROVIDER_DEV))

    logger.info(
        "Done. Shimmed %d operations (%d paths, %d resource methods) across %d service(s).",
        len(operations),
        total_paths,
        total_methods,
        services_touched,
    )
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "--webhook-url",
        default=None,
        help=(
            "Debug aid: override the GraphQL endpoint URL on every "
            "shimmed operation. Use a webhook.site bin to capture the "
            "exact request body stackql sends and diff it against a "
            "known-working curl invocation. Remove the flag (re-merge) "
            "once debugging is complete."
        ),
    )
    parser.add_argument(
        "--naked",
        action="store_true",
        help=(
            "Debug aid: replace each op's transform with a trivial one "
            "that emits the entire upstream response as a single `raw` "
            "string column on one row. Use to confirm dispatch + reach "
            "Cloudflare independent of any transform-body bugs."
        ),
    )
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    if args.webhook_url:
        global _DEBUG_URL_OVERRIDE
        _DEBUG_URL_OVERRIDE = args.webhook_url
        logger.warning("DEBUG MODE: routing GraphQL ops to %s", args.webhook_url)
    if args.naked:
        global _NAKED_RESPONSE
        _NAKED_RESPONSE = True
        logger.warning("DEBUG MODE: naked response mode (raw column only)")
    return merge()


if __name__ == "__main__":
    sys.exit(main())
