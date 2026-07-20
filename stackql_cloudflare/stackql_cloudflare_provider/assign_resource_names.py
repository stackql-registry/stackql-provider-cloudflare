"""CLI: walk every provider-dev/source/*.yaml and ensure each operation has a
row in provider-dev/config/all_services.csv with sensible default StackQL
resource/method/verb/object_key values.

Identity key is `filename::path::verb`. If a row already exists for an
operation, the user's edits to the four `stackql_*` columns are preserved
verbatim. New operations get auto-defaults that you can later refine.

Default heuristics:
    stackql_resource_name -> snake_case of x-stackql-sdk.resource_chain[-1]
                              when present, else the deepest meaningful path
                              segment, else the service name.
    stackql_method_name   -> x-stackql-sdk.method (the Python SDK method
                              name), else the snake_cased operationId.
    stackql_verb          -> Mapped from the (sdk_method, http_method) pair:
                                list           -> select
                                get            -> select
                                create/post    -> insert
                                update/patch   -> update
                                replace/put    -> replace
                                delete         -> delete
                                everything else POST -> exec
    stackql_object_key    -> $.result  for SELECT methods named *list* (the
                              Cloudflare API wraps array responses in
                              `result`). Empty otherwise.
"""
from __future__ import annotations

import argparse
import csv
import logging
import re
import sys
from collections import Counter, OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import yaml


logger = logging.getLogger(__name__)


PKG_DIR = Path(__file__).resolve().parent
PROVIDER_DEV_DIR = PKG_DIR.parent / "provider-dev"
SOURCE_DIR = PROVIDER_DEV_DIR / "source"
CONFIG_DIR = PROVIDER_DEV_DIR / "config"
CSV_PATH = CONFIG_DIR / "all_services.csv"

CSV_COLUMNS = [
    "filename",
    "path",
    "operationId",
    "formatted_op_id",
    "verb",
    "response_object",
    "tags",
    "formatted_tags",
    "stackql_resource_name",
    "stackql_method_name",
    "stackql_verb",
    "stackql_object_key",
    "op_description",
]

VERBS = ("get", "put", "post", "delete", "patch", "options", "head")

_SNAKE_RE_1 = re.compile(r"([a-z0-9])([A-Z])")
_SNAKE_RE_2 = re.compile(r"[^A-Za-z0-9]+")


def to_snake(s: str) -> str:
    if not s:
        return ""
    s = _SNAKE_RE_1.sub(r"\1_\2", s)
    s = _SNAKE_RE_2.sub("_", s).strip("_").lower()
    return s


@dataclass
class OpRow:
    filename: str
    path: str
    operationId: str
    formatted_op_id: str
    verb: str
    response_object: str
    tags: str
    formatted_tags: str
    stackql_resource_name: str
    stackql_method_name: str
    stackql_verb: str
    stackql_object_key: str
    op_description: str
    # Transient - not written to CSV; consumed by the disambiguator.
    required_sig: Tuple[str, ...] = ()

    def key(self) -> Tuple[str, str, str]:
        return (self.filename, self.path, self.verb)

    def as_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {c: getattr(self, c) for c in CSV_COLUMNS}
        # Carry the required-param signature through the dict pipeline so the
        # disambiguator (which works on dicts after CSV merge) can use it.
        d["_required_sig"] = self.required_sig
        return d


def _response_ref(op: dict) -> str:
    """Pluck the schema name out of the first non-empty success response."""
    responses = op.get("responses") or {}
    for code in ("200", "201", "202", "204"):
        r = responses.get(code) or responses.get(int(code))
        if not isinstance(r, dict):
            continue
        for mt in (r.get("content") or {}).values():
            sch = (mt or {}).get("schema") or {}
            ref = sch.get("$ref")
            if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
                return ref.split("/")[-1]
    return ""


def _default_resource_name(
    service: str,
    op: dict,
    path: str,
) -> str:
    xs = op.get("x-stackql-sdk") or {}
    chain = xs.get("resource_chain") or []
    if chain:
        return to_snake(chain[-1])
    # Fallback: derive from the last static path segment (not a {placeholder}).
    static_segments = [seg for seg in path.strip("/").split("/") if not seg.startswith("{")]
    if static_segments:
        last = static_segments[-1]
        if last != service:
            return to_snake(last)
    return to_snake(service)


def _path_ends_with_param(path: str) -> bool:
    last = path.rstrip("/").split("/")[-1] if path else ""
    return last.startswith("{") and last.endswith("}")


# Map non-JSON success media types to a short snake_case suffix used in the
# method name when we wrap the response into a `contents` column.
_BINARY_MEDIA_SUFFIX = {
    "application/pdf":          "pdf",
    "application/octet-stream": "blob",
    "application/zip":          "zip",
    "application/x-gzip":       "gz",
    "application/x-tar":        "tar",
    "image/png":                "png",
    "image/jpeg":               "jpeg",
    "image/jpg":                "jpg",
    "image/gif":                "gif",
    "image/svg+xml":            "svg",
    "image/webp":               "webp",
    "text/plain":               "text",
    "text/csv":                 "csv",
    "text/html":                "html",
    "text/xml":                 "xml",
    "application/xml":          "xml",
    "application/vnd.ms-excel": "xlsx",
    "text/markdown":            "markdown",
    # Cloudflare uses this synthetic media type for raw worker scripts.
    "string":                   "raw",
    # SCIM responses are JSON-shaped but use a non-standard media type.
    "application/scim+json":    "scim",
}


def _binary_response_suffix(op: dict) -> Optional[str]:
    """If the operation's first 2xx response is a non-JSON / binary media
    type, return a short snake_case suffix suitable for appending to the
    method name (e.g. 'pdf', 'png', 'blob'). Otherwise return None."""
    responses = op.get("responses") or {}
    for code, resp in responses.items():
        if not str(code).startswith("2") or not isinstance(resp, dict):
            continue
        content = resp.get("content") or {}
        if not content:
            return None
        mt_name = next(iter(content.keys()))
        if mt_name in _JSON_MEDIA_TYPES:
            return None
        suffix = _BINARY_MEDIA_SUFFIX.get(mt_name)
        if suffix:
            return suffix
        # Fallback: derive from the media type itself.
        # `image/foo` -> `foo`; `application/foo` -> `foo`; etc.
        try:
            tail = mt_name.split("/", 1)[1]
            tail = tail.split(";", 1)[0]
            tail = tail.replace("+", "_").replace("-", "_").replace(".", "_")
            return to_snake(tail) or "blob"
        except Exception:
            return "blob"
    return None


def _default_method_name(op: dict, path: str, verb: str) -> str:
    xs = op.get("x-stackql-sdk") or {}
    sdk_method = (xs.get("method") or "").lower()

    # Binary / non-JSON download endpoints: name them <leaf>_<mediatype>
    # so it's obvious from the SQL surface that you're pulling a binary
    # body. E.g. /reports/{id}/pdf returning application/pdf -> `report_pdf`.
    bin_suffix = _binary_response_suffix(op)
    if bin_suffix:
        segs = [s for s in path.strip("/").split("/") if not s.startswith("{")]
        # Strip the trailing scope/version segments to find a noun.
        leaf = ""
        for s in reversed(segs):
            if s not in ("download", "content", "blob", "raw", "export"):
                leaf = s
                break
        if not leaf and segs:
            leaf = segs[-1]
        if leaf:
            # Singularise common plurals so the method name reads naturally.
            sing = leaf
            if sing.endswith("ies"):
                sing = sing[:-3] + "y"
            elif sing.endswith("ses") or sing.endswith("xes") or sing.endswith("zes"):
                sing = sing[:-2]
            elif sing.endswith("s") and not sing.endswith("ss"):
                sing = sing[:-1]
            return to_snake(f"{sing}_{bin_suffix}")
        return f"download_{bin_suffix}"

    # Disambiguate list-vs-get based on path shape: a GET that ends in a
    # path parameter is fetching a single item ("get"), one that doesn't
    # is fetching a collection ("list"). This prevents resource.method
    # collisions when the SDK uses `list` for both.
    if verb == "get":
        if _path_ends_with_param(path):
            return "get"
        return sdk_method if sdk_method in ("list",) else "list"

    if sdk_method:
        return to_snake(sdk_method)

    # Otherwise: snake_case of operationId, stripped of any service prefix.
    op_id = op.get("operationId") or ""
    if op_id:
        op_id = op_id.replace("/", "_").replace("-", "_")
        return to_snake(op_id)

    # Last resort: <verb>_<resource>.
    static_segments = [seg for seg in path.strip("/").split("/") if not seg.startswith("{")]
    leaf = static_segments[-1] if static_segments else verb
    return to_snake(f"{verb}_{leaf}")


# SDK method names that signal a true lifecycle / RPC operation - not a
# CRUD verb. `exec` is the last resort: keep this list narrow. Words that
# can legitimately *create* a record (run inference, generate a token,
# submit a report) deliberately do NOT belong here - they map to `insert`
# when they take a JSON request body and return a projectable JSON result.
_ACTION_SDK_METHODS = frozenset({
    "activate", "approve", "cancel", "clear", "deactivate", "deny",
    "disable", "enable", "expire", "flush", "invalidate", "lock",
    "purge", "reboot", "refresh", "reject", "release", "renew",
    "reset", "restart", "restore", "resume", "retire", "retry",
    "rerun", "revoke", "rollback", "rotate", "start", "stop",
    "suspend", "trigger", "unlock",
})


# Path-leaf segments that mark a true lifecycle / RPC endpoint. Only checked
# on the *last* static segment of the path - not anywhere in the middle -
# so `/accounts/{id}/ai/run/{model}` doesn't match because the leaf is the
# model name (a noun). `/zones/{id}/purge_cache` does match because the
# leaf is the action verb.
_ACTION_LEAVES = frozenset({
    "activate", "activation_check", "approve", "cancel", "clear",
    "deactivate", "deny", "disable", "enable", "expire", "flush",
    "invalidate", "lock", "purge", "purge_cache", "purge_everything",
    "reboot", "refresh", "reject", "release", "renew", "reset",
    "restart", "restore", "resume", "retire", "retry", "rerun",
    "revoke", "rollback", "rotate", "start", "stop", "suspend",
    "trigger", "unlock",
})


def _path_static_segments(path: str) -> List[str]:
    return [s for s in path.strip("/").split("/")
            if s and not (s.startswith("{") and s.endswith("}"))]


def _path_leaf_is_action(path: str) -> bool:
    """True only when the *last* static segment of the path is a known
    lifecycle/action word. We deliberately do NOT check mid-path segments:
    `/accounts/{id}/ai/run/{model}` has `run` in the middle but the leaf is
    the model name, so this is an insert (run inference, get result), not
    an action.
    """
    segs = _path_static_segments(path)
    if not segs:
        return False
    leaf = segs[-1].lower().replace("-", "_")
    if leaf in _ACTION_LEAVES:
        return True
    # Compound action leaves like "revoke_tokens" or "purge_everything".
    head = leaf.split("_", 1)[0]
    if "_" in leaf and head in _ACTION_LEAVES:
        return True
    return False


_JSON_MEDIA_TYPES = ("application/json", "application/json; charset=utf-8")


def _has_projectable_success_body(op: dict) -> bool:
    """Return True if the operation's first 2xx response can plausibly be
    projected into table columns.

    Required conditions:
      - At least one 2xx response exists.
      - The success response declares an `application/json` content type
        (other media types - text/plain, image/*, application/pdf,
        application/scim+json, the synthetic `string` Cloudflare uses for
        raw script bodies, application/octet-stream, etc. - aren't
        relational).
      - The success schema has a `$ref`, `properties`, or `items`. A bare
        scalar schema (`type: string` / `integer` / etc.) cannot become
        columns.
    """
    responses = op.get("responses") or {}
    for code, resp in responses.items():
        if not str(code).startswith("2"):
            continue
        if not isinstance(resp, dict):
            return False
        content = resp.get("content") or {}
        if not content:
            return False
        json_mt = None
        for mt_name in _JSON_MEDIA_TYPES:
            if mt_name in content:
                json_mt = content[mt_name]
                break
        if json_mt is None:
            return False
        sch = (json_mt or {}).get("schema") or {}
        if not isinstance(sch, dict):
            return False
        if sch.get("$ref"):
            return True
        if sch.get("properties"):
            return True
        if sch.get("items"):
            return True
        # A `type: object` schema with no `properties` is opaque - treat as
        # non-projectable. Bare scalars likewise.
        return False
    return False


def _refine_stackql_verb(op: dict, http_verb: str, response_object: str, path: str = "") -> str:
    """Map a (verb, sdk_method, path) tuple to a stackql verb.

    Lifecycle / action operations -> `exec`. The signal is the path's *last*
    static segment: if it's an action verb (start/stop/purge_cache/run/...) or
    any segment along the path is a known action verb, the operation is an
    action regardless of HTTP method.

    Operations whose success response is not a projectable JSON object/array
    (non-JSON media type, scalar body, empty content) -> `exec`, since
    stackql can't model them as columns. This means a GET that returns
    `text/plain` becomes an exec method (still callable by name) rather
    than a SELECT that always errors at DESCRIBE time.
    """
    xs = op.get("x-stackql-sdk") or {}
    sdk_method = (xs.get("method") or "").lower()

    if http_verb == "get":
        # Binary / non-JSON GETs get wrapped at provider-generation time
        # into a `{contents: string}` JSON shape so they're selectable as
        # a single-row, single-column table. Keep them as SELECT here.
        if _binary_response_suffix(op):
            return "select"
        # SELECT needs a projectable JSON object/array - if the body is an
        # opaque object with no properties / scalar / empty, downgrade to
        # exec so users can still call the endpoint by name without
        # DESCRIBE erroring at SQL plan time.
        if not _has_projectable_success_body(op):
            return "exec"
        return "select"
    if http_verb == "delete":
        return "delete"
    if http_verb == "patch":
        # PATCH whose SDK method is a true lifecycle verb (e.g. `clear`,
        # `cancel`) maps to exec; same if the path's leaf segment is a
        # lifecycle action. Everything else is `update`.
        if sdk_method in _ACTION_SDK_METHODS or _path_leaf_is_action(path):
            return "exec"
        return "update"
    if http_verb == "put":
        # PUT into a path whose leaf is a lifecycle action (e.g.
        # /activation_check, /purge_cache) or whose SDK method name is a
        # lifecycle verb -> exec. Otherwise PUT maps to `replace` per HTTP
        # semantics. We keep PUT=replace even when the SDK names the
        # method `update` so that paired PATCH+PUT on the same path
        # (PATCH=update, PUT=replace) don't both collapse onto the same
        # stackql verb.
        if sdk_method in _ACTION_SDK_METHODS or _path_leaf_is_action(path):
            return "exec"
        return "replace"
    if http_verb == "post":
        # POSTs map to `insert` by default - any POST that takes a body and
        # returns a JSON result is creating something (a resource, an
        # inference result, a generated token, etc.). The only POSTs that
        # become `exec` are true lifecycle ops: a SDK method named for an
        # action verb (`start`, `stop`, `cancel`, ...), or a path whose
        # leaf segment is a lifecycle action (`/purge_cache`,
        # `/activation_check`).
        if sdk_method in _ACTION_SDK_METHODS:
            return "exec"
        if _path_leaf_is_action(path):
            return "exec"
        return "insert"
    return "exec"


def _resolve_schema_ref(sch: dict, schemas: dict) -> dict:
    """Follow at most one level of $ref into the schemas table."""
    ref = sch.get("$ref")
    if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
        target = schemas.get(ref[len("#/components/schemas/"):])
        if isinstance(target, dict):
            return target
    return sch


def _find_array_key(sch: dict, schemas: dict, ignore: frozenset = frozenset()) -> str:
    """Given a top-level response schema, return the JSON path (dotted, no
    leading `$`) to the array payload.

    Cloudflare's V4 envelope variants we handle:

      1. `{result: [...]}`                         -> "result"
      2. `{result: {<payload_array_key>: [...]}}`  -> "result.<payload_array_key>"
         (e.g. abuse_reports list: `result.reports`,
          pages logs: `result.data`)
      3. `{items: [...]}` / `{data: [...]}`
         / `{records: [...]}`                      -> "items" / "data" / "records"

    Envelope metadata (errors, messages, result_info, info) is ignored.
    """
    if not isinstance(sch, dict):
        return ""
    sch = _resolve_schema_ref(sch, schemas)
    props = sch.get("properties") or {}
    if not isinstance(props, dict):
        return ""

    # Case 1 + 2: there's a `result` property.
    result_node = props.get("result")
    if isinstance(result_node, dict):
        result_resolved = _resolve_schema_ref(result_node, schemas)
        if result_resolved.get("type") == "array":
            # Case 1: result is a list - the array is the payload.
            return "result"
        # Case 2: result is itself an object. Two sub-cases to distinguish:
        #   (a) result is a "wrapper" - it has an inner array of rows
        #       plus some report-wide metadata siblings (e.g. dns reports:
        #       result.{data:[...], rows, totals, query, ...}, or pages
        #       logs: result.{data:[...], total, includes_container_logs}).
        #       The actual rows live at result.<arrayKey>.
        #   (b) result IS the row itself - it has a mix of scalar/object
        #       properties describing one entity (e.g. /user returns one
        #       user object with {id, email, username, betas:[...], ...}).
        #       The array property `betas` is a *field* of the row, not
        #       the row collection.
        # Distinguishing signal: pick the inner-array path ONLY when the
        # array's name is in a known wrapper-key allowlist. These are
        # the names that, in practice, signal "this is the list of rows":
        #   - `items`, `data`, `records`, `results`, `rows`
        #   - resource-name-pluralised aliases observed across Cloudflare:
        #     `reports`, `emails`, `mitigations`, `schemas`, `hosts`,
        #     `hostnames`, `accounts`, `members`, `tokens`
        # Anything else (e.g. `betas`, `urls`, `keys`) we treat as a row
        # property and project the parent result object instead.
        inner_props = result_resolved.get("properties") or {}
        if isinstance(inner_props, dict) and inner_props:
            row_collection_keys = {
                "items", "data", "records", "results", "rows",
            }
            inner_arrays = [
                k for k, v in inner_props.items()
                if isinstance(v, dict)
                and _resolve_schema_ref(v, schemas).get("type") == "array"
                and k not in ignore
            ]
            non_array_props = [
                k for k, v in inner_props.items()
                if k not in ignore
                and not (isinstance(v, dict) and _resolve_schema_ref(v, schemas).get("type") == "array")
            ]
            # Wrapper pattern: ONE inner array with no non-array siblings.
            # Descend regardless of array name (covers result.reports,
            # result.emails, result.mitigations, etc. - the "name matches
            # the parent path's resource" cases).
            if len(inner_arrays) == 1 and len(non_array_props) == 0:
                return f"result.{inner_arrays[0]}"
            # Wrapper-with-metadata pattern: any inner array with a known
            # row-collection name (`data`, `items`, `records`, ...) -
            # descend even if there are sibling metadata fields. Catches
            # /dns_analytics/report and similar.
            for k in inner_arrays:
                if k in row_collection_keys:
                    return f"result.{k}"
            # Otherwise treat result itself as the row (singleton entity).
            return "result"
        # Result has no properties - check if it's a $ref we couldn't
        # resolve (last-ditch), else give up.
        if result_resolved.get("$ref"):
            return "result"

    # Case 3: top-level array-typed envelopes (no `result`).
    array_props = [
        k for k, v in props.items()
        if isinstance(v, dict) and v.get("type") == "array" and k not in ignore
    ]
    for preferred in ("items", "data", "records"):
        if preferred in array_props:
            return preferred
    return array_props[0] if array_props else ""


def _find_object_envelope_key(sch: dict, schemas: dict) -> str:
    """For single-item GETs whose response is wrapped in Cloudflare's V4
    envelope (`{result: {...payload...}, success, errors, messages}`),
    return the key that holds the payload. Returns "" if the response
    isn't envelope-shaped.

    A schema is "envelope-shaped" iff it's a top-level object with a
    `result` property AND at least one of the standard envelope siblings
    (`success`, `errors`, `messages`, `result_info`).
    """
    if not isinstance(sch, dict):
        return ""
    sch = _resolve_schema_ref(sch, schemas)
    props = sch.get("properties") or {}
    if not isinstance(props, dict):
        return ""
    if "result" not in props:
        return ""
    envelope_siblings = {"success", "errors", "messages", "result_info"}
    if envelope_siblings.isdisjoint(props.keys()):
        return ""
    return "result"


_OBJECT_KEY_IGNORE_PROPS = frozenset({
    # These are envelope metadata that appear alongside the real list payload
    # on Cloudflare's V4 responses - never the actual list of business
    # objects, even when they happen to be arrays.
    "errors", "messages", "result_info", "info",
})


def _walk_dotted_key(top_sch: dict, schemas: dict, dotted: str) -> Optional[dict]:
    """Walk `top_sch.properties[seg1].properties[seg2]...` where dotted is
    `seg1.seg2...`. Returns the leaf schema (resolved through any $ref)
    or None if the walk dead-ends."""
    node = _resolve_schema_ref(top_sch, schemas)
    for seg in dotted.split("."):
        if not isinstance(node, dict):
            return None
        if node.get("type") == "array" and isinstance(node.get("items"), dict):
            node = _resolve_schema_ref(node["items"], schemas)
        props = node.get("properties") or {}
        if seg not in props:
            return None
        node = _resolve_schema_ref(props[seg], schemas)
    return node


def _key_is_usable(top_sch: dict, schemas: dict, dotted: str) -> bool:
    """Check that the leaf schema at `dotted` has projectable properties.

    A key is "unusable" when the leaf resolves to:
      - {type: object} with no properties (opaque blob)
      - {type: unknown}, {type: string} (scalar)
      - missing (walk dead-end)
      - array whose items have no properties

    The CSV row should leave stackql_object_key empty in those cases - it's
    better to surface the envelope columns and let the user dig with
    JSON_EXTRACT than to project an empty/opaque row.
    """
    leaf = _walk_dotted_key(top_sch, schemas, dotted)
    if leaf is None:
        return False
    if leaf.get("type") == "array" and isinstance(leaf.get("items"), dict):
        leaf = _resolve_schema_ref(leaf["items"], schemas)
    return bool(leaf.get("properties"))


def _default_object_key(
    op: dict,
    http_verb: str,
    sdk_method: str,
    schemas: dict,
    path: str = "",
) -> str:
    """Find the JSON path to the list payload for a SELECT-like operation.

    Only applies to *list* operations - those whose path doesn't end in a
    path parameter (so the operation returns a collection rather than a
    single item). For single-item GETs we return "" so stackql treats the
    top-level response as the row.

    Cloudflare's V4 envelope wraps array results in `$.result`, but some
    endpoints (notably newer ones under /cni/, /pipelines/, ...) use
    `$.items`. We introspect the actual response schema, skipping any
    envelope-metadata properties (`errors`, `messages`, etc.) that are
    arrays but never the business payload.
    """
    if http_verb != "get":
        return ""

    responses = op.get("responses") or {}
    is_single_item = _path_ends_with_param(path)
    for code in ("200", "201"):
        r = responses.get(code) or responses.get(int(code))
        if not isinstance(r, dict):
            continue
        for mt in (r.get("content") or {}).values():
            sch = (mt or {}).get("schema") or {}
            if is_single_item:
                # Single-item GET: look for the V4 envelope's payload key
                # (typically `result`) so stackql projects the payload
                # rather than the envelope's metadata columns.
                key = _find_object_envelope_key(sch, schemas)
            else:
                # List GET: look for the array-typed payload key.
                key = _find_array_key(sch, schemas, ignore=_OBJECT_KEY_IGNORE_PROPS)
            if key:
                # Usability gate: only emit the key if the leaf schema has
                # projectable properties. An opaque {type: object} or
                # {type: unknown} payload makes the Fields table empty
                # and stackql's column projection useless - better to fall
                # back to the envelope and let the caller JSON_EXTRACT.
                if _key_is_usable(sch, schemas, key):
                    return f"$.{key}"
    # Fallback: if the SDK calls this `list` but we couldn't introspect a
    # schema (e.g. response uses non-JSON content), default to $.result.
    if sdk_method == "list":
        return "$.result"
    return ""


def _format_op_id(op_id: str, fallback_verb: str = "", fallback_path: str = "") -> str:
    """Normalise an upstream operationId to a stable snake-cased version.
    If no operationId was provided upstream, synthesize one from the verb +
    path so each operation has a unique, stable identifier."""
    if op_id:
        return op_id.replace("/", "_").replace("-", "_")
    if not fallback_verb and not fallback_path:
        return ""
    segs = [s.strip("{}") for s in fallback_path.strip("/").split("/") if s]
    return to_snake("_".join([fallback_verb] + segs))


def _required_param_signature(op: dict) -> Tuple[str, ...]:
    """Return a stable, sortable tuple of (in:name) for every required param
    on this operation. Used by the disambiguator to detect StackQL-level
    ambiguity (two methods on the same resource+verb with the same required
    set look like duplicates from a SQL WHERE-clause planner perspective)."""
    out = []
    for p in (op.get("parameters") or []):
        if not isinstance(p, dict):
            continue
        if not p.get("required"):
            continue
        name = p.get("name") or ""
        where = p.get("in") or ""
        if name:
            out.append(f"{where}:{name}")
    return tuple(sorted(out))


def build_row_from_op(
    filename: str,
    path: str,
    verb: str,
    op: dict,
    service: str,
    schemas: dict | None = None,
) -> OpRow:
    op_id = op.get("operationId") or ""
    tags = op.get("tags") or []
    response_obj = _response_ref(op)
    description = (op.get("summary") or op.get("description") or "").strip().splitlines()
    description = description[0] if description else ""

    xs = op.get("x-stackql-sdk") or {}
    sdk_method = (xs.get("method") or "").lower()

    resource_name = _default_resource_name(service, op, path)
    resource_name = _safe_resource_name(resource_name, path)
    method_name = _default_method_name(op, path, verb)
    stackql_verb = _refine_stackql_verb(op, verb, response_obj, path=path)
    object_key = _default_object_key(op, verb, sdk_method, schemas or {}, path=path)
    required_sig = _required_param_signature(op)

    return OpRow(
        filename=filename,
        path=path,
        operationId=op_id,
        formatted_op_id=_format_op_id(op_id, fallback_verb=verb, fallback_path=path),
        verb=verb,
        response_object=response_obj,
        tags=",".join(tags),
        formatted_tags=",".join(to_snake(t) for t in tags),
        stackql_resource_name=resource_name,
        stackql_method_name=method_name,
        stackql_verb=stackql_verb,
        stackql_object_key=object_key,
        op_description=description,
        required_sig=required_sig,
    )


def enumerate_source_ops() -> Iterable[OpRow]:
    """Yield every operation across all source/*.yaml files in stable order."""
    for yf in sorted(SOURCE_DIR.glob("*.yaml")):
        spec = yaml.safe_load(yf.read_text(encoding="utf-8")) or {}
        service = yf.stem
        schemas = ((spec.get("components") or {}).get("schemas") or {})
        for path, item in (spec.get("paths") or {}).items():
            if not isinstance(item, dict):
                continue
            for verb in VERBS:
                op = item.get(verb)
                if not isinstance(op, dict):
                    continue
                yield build_row_from_op(yf.name, path, verb, op, service, schemas=schemas)


def _read_existing_csv() -> "OrderedDict[Tuple[str, str, str], Dict[str, str]]":
    """Return existing rows keyed by (filename, path, verb)."""
    out: "OrderedDict[Tuple[str, str, str], Dict[str, str]]" = OrderedDict()
    if not CSV_PATH.exists():
        return out
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row.get("filename", ""), row.get("path", ""), row.get("verb", ""))
            out[key] = row
    return out


_PRESERVE_COLUMNS = (
    "stackql_resource_name",
    "stackql_method_name",
    "stackql_verb",
    "stackql_object_key",
)


# StackQL's SQL parser (https://github.com/stackql/stackql-parser) treats
# these words as reserved tokens that *must not* appear unquoted in the
# resource segment of a FROM / SHOW / DESCRIBE clause. (Method names
# never reach the SQL parser - they're FQRN-resolved before the SQL
# parse - so we don't filter them.)
#
# Empirically confirmed against stackql to break at the resource level.
# Keep this list narrow: only add entries that the parser actually rejects.
_RESERVED_RESOURCE_NAMES = frozenset({
    "tree",
    "stream",
    "release",
    "full",
    "analyze",
})


def _pluralise(name: str) -> str:
    """Simple English pluralisation good enough for the reserved-word
    workaround. Handles a few common irregulars; otherwise appends `s`."""
    if not name:
        return name
    irregular = {
        "analyze": "analyses",
        "analysis": "analyses",
        "release": "releases",
        "full": "fulls",
        "stream": "streams",
        "tree": "trees",
    }
    if name in irregular:
        return irregular[name]
    if name.endswith("s"):
        return name
    if name.endswith("y") and name[-2:-1] not in "aeiou":
        return name[:-1] + "ies"
    if name.endswith(("ch", "sh", "x", "z", "s")):
        return name + "es"
    return name + "s"


def _safe_resource_name(name: str, path: str) -> str:
    """If `name` is a known reserved word, return its pluralised form so it
    can appear unquoted in StackQL FROM / SHOW clauses. Otherwise return
    `name` unchanged."""
    if name in _RESERVED_RESOURCE_NAMES:
        return _pluralise(name)
    return name


def _path_segments(path: str) -> List[str]:
    return [s for s in path.strip("/").split("/") if s]


def _is_param(seg: str) -> bool:
    return seg.startswith("{") and seg.endswith("}")


def _disambiguate_collisions(
    rows: List[Dict[str, str]],
    preserved_keys: "Dict[Tuple[str, str, str], Dict[str, str]]",
) -> None:
    """Walk through rows grouped by (filename, resource_name, method_name).

    For any group with >1 row:

      - If the colliding rows have *different* required-param signatures
        (e.g. /accounts/{account_id}/... vs /zones/{zone_id}/...), keep the
        resource name and rename the *method* on each. StackQL's planner can
        route a SQL WHERE clause to the right method based on required-param
        signature, so multiple methods under the same resource and sqlVerb
        are fine - the YAML map just needs unique method-name keys.

      - If they share the same signature, fall back to renaming the resource
        by prepending parent path segments (the old behavior).

    Rows that came from the previous CSV with a non-default resource name
    are left alone - the user's edit is assumed intentional.
    """
    # Group by collision key.
    groups: Dict[Tuple[str, str, str], List[Dict[str, str]]] = {}
    for r in rows:
        key = (r["filename"], r["stackql_resource_name"], r["stackql_method_name"])
        groups.setdefault(key, []).append(r)

    changed = 0
    for (filename, resource, method), rs in groups.items():
        if len(rs) == 1:
            continue

        # Branch A: when colliding rows have *distinct* required-param
        # signatures, we can keep the resource name and rename only the
        # method on each. The first-segment of the path is a natural
        # discriminator (typically `accounts` vs `zones`).
        #
        # Partition by signature. Rows whose signature is unique within
        # the group get a method-rename; rows whose signature is shared
        # with another row in the same group fall through to branch B
        # (resource-rename).
        sig_counts: Counter = Counter(tuple(r.get("_required_sig") or ()) for r in rs)
        renamable = [r for r in rs if sig_counts[tuple(r.get("_required_sig") or ())] == 1]
        unrenamable = [r for r in rs if sig_counts[tuple(r.get("_required_sig") or ())] > 1]
        if len(renamable) >= 2:
            for r in renamable:
                row_key = (r["filename"], r["path"], r["verb"])
                preserved = preserved_keys.get(row_key)
                if preserved and (preserved.get("stackql_method_name") or "").strip() not in ("", method):
                    continue
                segs = [s for s in _path_segments(r["path"]) if not _is_param(s)]
                discriminator = segs[0] if segs else ""
                if discriminator and discriminator != method:
                    singular = discriminator[:-1] if discriminator.endswith("s") else discriminator
                    r["stackql_method_name"] = to_snake(f"{method}_by_{singular}")
                    changed += 1
        # If branch A handled every collision (no rows with duplicate sigs),
        # we're done with this group.
        if not unrenamable:
            taken = Counter((r["stackql_resource_name"], r["stackql_method_name"]) for r in rs)
            if all(v == 1 for v in taken.values()):
                continue
        # Otherwise fall through to branch B for the unrenamable rows. To
        # avoid re-renaming the branch-A rows, point branch B's group at
        # only the unrenamable subset.
        rs = unrenamable if unrenamable else rs

        # Branch B: same signature OR method-rename didn't disambiguate -
        # fall back to prepending parent path segments into the resource name.
        # Try prepending one parent segment at a time. Stop when names are unique
        # within the colliding subset or we run out of segments.
        for depth in range(1, 10):
            assigned: Dict[Tuple[str, str], Dict[str, str]] = {}
            still_colliding = False
            for r in rs:
                row_key = (r["filename"], r["path"], r["verb"])
                preserved = preserved_keys.get(row_key)
                if preserved and (preserved.get("stackql_resource_name") or "").strip() not in ("", resource):
                    # User chose a custom name; leave it.
                    continue
                segs = [s for s in _path_segments(r["path"]) if not _is_param(s)]
                # Keep the original leaf at the end; prepend up to `depth` parents.
                if not segs:
                    continue
                leaf = segs[-1]
                parents = segs[:-1]
                prefix = parents[-depth:] if depth <= len(parents) else parents
                candidate = "_".join(prefix + [leaf]) if prefix else leaf
                candidate = to_snake(candidate)
                assigned[(candidate, r["stackql_method_name"])] = r
                r["_candidate_resource"] = candidate
            # Check whether all assigned candidates are unique within this group.
            taken: Counter_t = {}
            for r in rs:
                cand = r.get("_candidate_resource") or r["stackql_resource_name"]
                taken[(cand, r["stackql_method_name"])] = taken.get((cand, r["stackql_method_name"]), 0) + 1
            if all(v == 1 for v in taken.values()):
                # Commit candidates.
                for r in rs:
                    if "_candidate_resource" in r:
                        if r["_candidate_resource"] != r["stackql_resource_name"]:
                            changed += 1
                        r["stackql_resource_name"] = r.pop("_candidate_resource")
                still_colliding = False
                break
            else:
                still_colliding = True
                # Clear candidates and try a deeper prefix.
                for r in rs:
                    r.pop("_candidate_resource", None)
        if still_colliding:
            # Try appending the trailing parameter name (or static segment) to
            # break the tie. This catches /foo/{dimension} vs /foo/user_agent.
            assigned: Dict[Tuple[str, str], Dict[str, str]] = {}
            for r in rs:
                segs = _path_segments(r["path"])
                tail = segs[-1] if segs else ""
                tail_clean = tail.strip("{}").replace("-", "_")
                base = r["stackql_resource_name"]
                cand = to_snake(f"{base}_{tail_clean}") if tail_clean and tail_clean != base else base
                r["_candidate_resource"] = cand
            taken: Counter_t = {}
            for r in rs:
                key2 = (r["_candidate_resource"], r["stackql_method_name"])
                taken[key2] = taken.get(key2, 0) + 1
            if all(v == 1 for v in taken.values()):
                for r in rs:
                    if r["_candidate_resource"] != r["stackql_resource_name"]:
                        changed += 1
                    r["stackql_resource_name"] = r.pop("_candidate_resource")
            else:
                # Final fallback: append a short hash of the path so we at least get unique names.
                import hashlib
                for r in rs:
                    r.pop("_candidate_resource", None)
                    h = hashlib.sha1(r["path"].encode()).hexdigest()[:6]
                    r["stackql_resource_name"] = f"{r['stackql_resource_name']}_{h}"
                    changed += 1

    # Second pass: detect any *global* (resource, method) collision that survived
    # the per-group disambiguation - two originally-different groups may have
    # been renamed to the same target. Fall through to the tail-segment +
    # hash strategy on those.
    global_groups: Dict[Tuple[str, str, str], List[Dict[str, str]]] = {}
    for r in rows:
        gkey = (r["filename"], r["stackql_resource_name"], r["stackql_method_name"])
        global_groups.setdefault(gkey, []).append(r)
    for (filename, resource, method), rs in global_groups.items():
        if len(rs) <= 1:
            continue
        for r in rs:
            segs = _path_segments(r["path"])
            tail = segs[-1].strip("{}").replace("-", "_") if segs else ""
            if tail and tail != resource:
                r["stackql_resource_name"] = to_snake(f"{resource}_{tail}")
                changed += 1
        # If a hash fallback is still needed, apply it.
        taken: Dict[Tuple[str, str], int] = {}
        for r in rs:
            taken[(r["stackql_resource_name"], r["stackql_method_name"])] = (
                taken.get((r["stackql_resource_name"], r["stackql_method_name"]), 0) + 1
            )
        if any(v > 1 for v in taken.values()):
            import hashlib
            for r in rs:
                h = hashlib.sha1(r["path"].encode()).hexdigest()[:6]
                r["stackql_resource_name"] = f"{r['stackql_resource_name']}_{h}"
                changed += 1

    # Third pass: detect StackQL-level signature collisions. Within a single
    # service file, if two operations share (resource, stackql_verb,
    # required-param-signature), StackQL's planner can't disambiguate them
    # from a SQL WHERE clause. Skip `exec` (multiple exec methods with the
    # same signature are allowed - they're called by name). Rename the
    # colliding rows by prefixing parent path segments into the resource
    # name until all colliding rows have distinct resource names.
    sig_groups: Dict[Tuple[str, str, str, Tuple[str, ...]], List[Dict[str, Any]]] = {}
    for r in rows:
        if (r.get("stackql_verb") or "").lower() == "exec":
            continue
        sig = r.get("_required_sig") or ()
        sig_groups.setdefault(
            (r["filename"], r["stackql_resource_name"], r["stackql_verb"], tuple(sig)),
            [],
        ).append(r)

    for (filename, resource, sql_verb, sig), rs in sig_groups.items():
        if len(rs) <= 1:
            continue
        # Skip any row whose resource name was preserved from the user's prior
        # edit - their explicit choice wins.
        mutable: List[Dict[str, Any]] = []
        for r in rs:
            row_key = (r["filename"], r["path"], r["verb"])
            preserved = preserved_keys.get(row_key)
            if preserved and (preserved.get("stackql_resource_name") or "").strip() not in ("", resource):
                continue
            mutable.append(r)
        if len(mutable) <= 1:
            continue
        renamed = False
        for depth in range(1, 10):
            for r in mutable:
                segs = [s for s in _path_segments(r["path"]) if not _is_param(s)]
                if not segs:
                    r["_candidate_resource"] = r["stackql_resource_name"]
                    continue
                leaf = segs[-1]
                parents = segs[:-1]
                prefix = parents[-depth:] if depth <= len(parents) else parents
                cand = "_".join(prefix + [leaf]) if prefix else leaf
                r["_candidate_resource"] = to_snake(cand)
            seen = set(r["_candidate_resource"] for r in mutable)
            if len(seen) == len(mutable):
                for r in mutable:
                    if r["_candidate_resource"] != r["stackql_resource_name"]:
                        r["stackql_resource_name"] = r["_candidate_resource"]
                        changed += 1
                    r.pop("_candidate_resource", None)
                renamed = True
                break
        if not renamed:
            # Hash fallback so we always exit with distinct names.
            import hashlib
            for r in mutable:
                r.pop("_candidate_resource", None)
                h = hashlib.sha1(r["path"].encode()).hexdigest()[:6]
                r["stackql_resource_name"] = f"{r['stackql_resource_name']}_{h}"
                changed += 1

    if changed:
        logger.info("Disambiguated %d colliding rows via path-prefixed resource names", changed)


# Type alias for clarity.
Counter_t = Dict[Tuple[str, str], int]


def write_csv(rows: List[Dict[str, str]]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reset", action="store_true",
                        help="Reset all four stackql_* columns to their defaults, discarding manual edits.")
    parser.add_argument("--strict", action="store_true",
                        help="Exit non-zero if any source operation has no existing mapping row in the "
                             "CSV. Default rows ARE still written for the new operations, so review "
                             "them (tighten resource/method/verb if needed) and re-run.")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    existing = _read_existing_csv()
    logger.info("Loaded %d existing rows from %s", len(existing), CSV_PATH)

    out_rows: List[Dict[str, str]] = []
    seen: set = set()
    added = updated = preserved = 0

    for row in enumerate_source_ops():
        key = row.key()
        seen.add(key)
        new = row.as_dict()
        prev = existing.get(key)
        if prev is None:
            added += 1
            # Surface the auto-assignment so users notice new operations
            # showing up across upstream-spec refreshes and can review the
            # defaults if they want to tighten them.
            logger.info(
                "new op found %s %s %s -> resource=%s method=%s verb=%s",
                row.filename, row.verb.upper(), row.path,
                row.stackql_resource_name, row.stackql_method_name, row.stackql_verb,
            )
            out_rows.append(new)
            continue
        merged = dict(new)
        if not args.reset:
            for col in _PRESERVE_COLUMNS:
                if (prev.get(col) or "").strip():
                    merged[col] = prev[col]
            preserved += 1
        else:
            updated += 1
        out_rows.append(merged)

    # Disambiguate resource/method collisions within each service by prefixing
    # the colliding rows' resource names with parent path segments. Skip rows
    # whose stackql_resource_name was explicitly overridden by the user (we
    # consider this signaled by the row being preserved).
    _disambiguate_collisions(out_rows, existing if not args.reset else {})

    removed_keys = set(existing.keys()) - seen
    if removed_keys:
        logger.warning("%d rows in CSV no longer have a matching operation; they will be dropped.",
                       len(removed_keys))
        for k in list(removed_keys)[:10]:
            logger.warning("  dropped: %s", k)

    # Stable ordering: filename then path then verb.
    out_rows.sort(key=lambda r: (r["filename"], r["path"], r["verb"]))
    write_csv(out_rows)
    logger.info("Wrote %d rows to %s (new=%d preserved=%d reset=%d dropped=%d)",
                len(out_rows), CSV_PATH, added, preserved, updated, len(removed_keys))
    if args.strict and added:
        logger.error(
            "--strict: %d operation(s) had no mapping row in the CSV. Default rows were "
            "written (grep the log above for 'new op found') - review and curate the "
            "stackql_resource_name / stackql_method_name / stackql_verb / stackql_object_key "
            "columns, then re-run.", added)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
