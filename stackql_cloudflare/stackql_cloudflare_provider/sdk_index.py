"""Walk the Cloudflare Python SDK source tree and build an index of
(http_method, path) -> (service, resource, sdk_method).

The SDK files contain calls like:
    self._post("/zones", ...)
    self._get_api_list("/zones", ...)
    self._get(path_template("/zones/{zone_id}", zone_id=zone_id), ...)
    self._delete(path_template("/zones/{zone_id}", ...), ...)
    self._patch(path_template("/zones/{zone_id}", ...), ...)
    self._put(path_template("/zones/{zone_id}", ...), ...)

We use the Python AST module to walk every .py file under src/cloudflare/resources/
and extract every (method, path) tuple along with the containing class method and
the file location, which tells us the service and resource it belongs to.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Maps the SDK helper method to the HTTP verb.
_HTTP_HELPERS = {
    "_get": "get",
    "_get_api_list": "get",
    "_post": "post",
    "_put": "put",
    "_patch": "patch",
    "_delete": "delete",
}


@dataclass
class SdkOperation:
    service: str           # Top-level SDK service (e.g. "zones", "workers")
    resource_chain: List[str]  # Path within the service (e.g. ["holds"], or [] for top-level)
    sdk_method: str        # SDK method name (e.g. "list", "get", "create", "delete", "edit")
    http_method: str       # get/post/put/patch/delete
    path: str              # OpenAPI path string with {placeholders}
    source_file: Path
    line: int


def _extract_path_from_call(node: ast.Call) -> Optional[str]:
    """Pull a static path string out of a call's first positional arg.

    Handles:
        self._get("/foo")
        self._get(path_template("/foo/{id}", id=id))
        self._get(f"/foo/{id}")
    """
    if not node.args:
        return None
    arg = node.args[0]
    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
        return arg.value
    if isinstance(arg, ast.Call):
        # path_template("/foo/{id}", id=id)
        if (
            isinstance(arg.func, ast.Name)
            and arg.func.id == "path_template"
            and arg.args
            and isinstance(arg.args[0], ast.Constant)
            and isinstance(arg.args[0].value, str)
        ):
            return arg.args[0].value
    if isinstance(arg, ast.JoinedStr):
        # f-string fallback: stitch together the constant parts; this is best-effort.
        parts: List[str] = []
        for v in arg.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                parts.append(v.value)
            elif isinstance(v, ast.FormattedValue):
                if isinstance(v.value, ast.Name):
                    parts.append("{" + v.value.id + "}")
                else:
                    return None
            else:
                return None
        return "".join(parts)
    return None


def _walk_method_for_http_calls(method: ast.FunctionDef) -> List[Tuple[str, str, int]]:
    """Return list of (http_method, path, line) for every self._* http helper call
    found inside `method`."""
    found: List[Tuple[str, str, int]] = []
    for node in ast.walk(method):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and func.value.id == "self"
            and func.attr in _HTTP_HELPERS
        ):
            continue
        path = _extract_path_from_call(node)
        if path is None:
            continue
        found.append((_HTTP_HELPERS[func.attr], path, node.lineno))
    return found


def _resource_chain_for(file_path: Path, resources_root: Path) -> Tuple[str, List[str]]:
    """Given e.g. resources/zones/holds.py, return ('zones', ['holds']).
    Given resources/zones/zones.py, return ('zones', []).
    Given resources/workers/scripts/scripts.py, return ('workers', ['scripts']).
    """
    rel = file_path.relative_to(resources_root)
    parts = list(rel.parts)
    # parts[-1] is the .py file; strip extension
    leaf = parts[-1][:-3] if parts[-1].endswith(".py") else parts[-1]
    parents = parts[:-1]

    if not parents:
        # Module file directly under resources/ - e.g. resources/__init__.py - ignore.
        return leaf, []

    service = parents[0]
    # The "main" file for a service is named after the deepest directory it sits in.
    # e.g. resources/zones/zones.py -> top-level of zones
    # e.g. resources/zones/holds.py -> zones/holds
    # e.g. resources/workers/scripts/scripts.py -> top-level of workers/scripts (still a sub-resource of workers)
    if len(parents) == 1 and leaf == service:
        return service, []
    # Build the resource chain from everything after the service directory plus
    # the file leaf, except suppress redundant ".../foo/foo.py" entries.
    chain: List[str] = list(parents[1:])
    if not chain or chain[-1] != leaf:
        if leaf != "__init__":
            chain.append(leaf)
    return service, chain


_DUAL_SCOPE_SDK_PATTERNS = [
    # SDK templates the same dual-scope routes as the OpenAPI spec but uses
    # `{account_or_zone}` (no 's') and `{account_or_zone_id}`. After OpenAPI
    # fanout we have concrete paths like /accounts/{account_id}/... and
    # /zones/{zone_id}/...; expand the SDK paths the same way so we can match.
    "/{account_or_zone}/{account_or_zone_id}",
    "/{accounts_or_zones}/{account_or_zone_id}",
]

_SDK_FANOUT_SCOPES = [
    ("/accounts/{account_id}", "account_id"),
    ("/zones/{zone_id}",       "zone_id"),
]


def _fanout_sdk_path(path: str) -> List[Tuple[str, str]]:
    """If `path` starts with one of the dual-scope SDK templates, return the
    two scope-specific concrete paths it implies, paired with a scope tag
    ('account' or 'zone'). Otherwise return [(path, '')]."""
    for templ in _DUAL_SCOPE_SDK_PATTERNS:
        if path.startswith(templ):
            tail = path[len(templ):]
            return [
                (_SDK_FANOUT_SCOPES[0][0] + tail, "account"),
                (_SDK_FANOUT_SCOPES[1][0] + tail, "zone"),
            ]
    return [(path, "")]


def build_sdk_index(sdk_root: Path) -> List[SdkOperation]:
    """Parse every .py file under <sdk_root>/resources/ and return one SdkOperation
    per (http_method, path) call found.

    SDK paths that template `{account_or_zone}` / `{accounts_or_zones}` are
    fanned out so they match the post-fanout OpenAPI paths produced by
    `stackql_cloudflare_provider.fanout`. Each scoped variant gets the same
    sdk_method, service, and resource_chain.
    """
    resources_root = sdk_root / "resources"
    if not resources_root.exists():
        raise FileNotFoundError(f"Cloudflare SDK resources/ dir not found at {resources_root}")

    ops: List[SdkOperation] = []
    for py in resources_root.rglob("*.py"):
        if py.name == "__init__.py":
            continue
        try:
            tree = ast.parse(py.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        service, chain = _resource_chain_for(py, resources_root)
        if not service:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            calls = _walk_method_for_http_calls(node)
            if not calls:
                continue
            # The SDK names async methods identically to sync counterparts, so we
            # de-duplicate later by (service, chain, sdk_method, http_method, path).
            for verb, path, line in calls:
                for concrete, _scope in _fanout_sdk_path(path):
                    ops.append(SdkOperation(
                        service=service,
                        resource_chain=chain,
                        sdk_method=node.name,
                        http_method=verb,
                        path=concrete,
                        source_file=py,
                        line=line,
                    ))
    return ops


def build_path_to_service_index(ops: List[SdkOperation]) -> Dict[Tuple[str, str], SdkOperation]:
    """Index by (http_method, path) -> SdkOperation (sync version preferred)."""
    idx: Dict[Tuple[str, str], SdkOperation] = {}
    for op in ops:
        key = (op.http_method, op.path)
        # Prefer the sync (non-async) version, and prefer the first match.
        existing = idx.get(key)
        if existing is None:
            idx[key] = op
    return idx
