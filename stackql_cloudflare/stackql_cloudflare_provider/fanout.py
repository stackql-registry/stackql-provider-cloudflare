"""Fan out dual-scope Cloudflare paths into single-scope paths.

Upstream Cloudflare templates 64 endpoints under

    /{accounts_or_zones}/{account_or_zone_id}/...

where `{accounts_or_zones}` is *not* a real parameter (it's literally the
string "accounts" or "zones") and `{account_or_zone_id}` is the ID of
whichever scope was chosen. That makes a poor StackQL surface: a SQL
WHERE clause would have to discriminate on a magic-string column.

We rewrite each such path into two concrete paths:

    /accounts/{account_id}/...     (account scope)
    /zones/{zone_id}/...           (zone scope)

For each fanned-out path we:

  - clone the operation
  - drop the `accounts_or_zones` parameter from the parameter list
  - rename the `account_or_zone_id` parameter to `account_id` or `zone_id`
    on the parameter list AND in the path template
  - suffix the upstream operationId with `_for_account` / `_for_zone` so
    they remain unique within the spec

Downstream passes (param inlining, schema rename, splitter, CSV builder)
then naturally produce distinct rows per scope - because the required-
param signatures differ (`account_id` vs `zone_id`), StackQL can route
WHERE clauses to the correct method.
"""
from __future__ import annotations

import copy
import re
from typing import Any, Dict, List, Tuple


_DUAL_SCOPE_PREFIX = "/{accounts_or_zones}/{account_or_zone_id}"

_SCOPES: List[Tuple[str, str, str, str]] = [
    # (replacement_prefix, scope_id_param_name, operation_id_suffix, tag_suffix)
    ("/accounts/{account_id}",      "account_id", "for_account", "(account scope)"),
    ("/zones/{zone_id}",             "zone_id",     "for_zone",    "(zone scope)"),
]


def _rewrite_path(original: str, replacement_prefix: str) -> str:
    """Replace the leading '/{accounts_or_zones}/{account_or_zone_id}' with
    the scope-specific prefix. Anything after the prefix is preserved
    verbatim."""
    if not original.startswith(_DUAL_SCOPE_PREFIX):
        return original
    return replacement_prefix + original[len(_DUAL_SCOPE_PREFIX):]


def _rewrite_parameters(
    params: List[Any],
    scope_id_param_name: str,
) -> List[Any]:
    """Return a new parameter list where:

      - The 'accounts_or_zones' path parameter is dropped (it is no longer
        templated - the path segment is now a literal).
      - The 'account_or_zone_id' parameter is cloned, renamed to
        `scope_id_param_name`, and any description referencing "Account or
        Zone" is left as-is (the schema is generic enough to handle both).
    """
    new_params: List[Any] = []
    for p in params:
        if not isinstance(p, dict):
            new_params.append(p)
            continue
        name = p.get("name")
        loc = p.get("in")
        if loc == "path" and name == "accounts_or_zones":
            # Drop entirely - no longer templated.
            continue
        if loc == "path" and name == "account_or_zone_id":
            renamed = copy.deepcopy(p)
            renamed["name"] = scope_id_param_name
            new_params.append(renamed)
            continue
        new_params.append(copy.deepcopy(p))
    return new_params


def _verbs(item: Dict[str, Any]) -> List[str]:
    return [v for v in ("get", "put", "post", "delete", "patch", "options", "head", "trace")
            if v in item]


def fanout_dual_scope_paths(spec: dict) -> int:
    """Walk every path in `spec` and explode any dual-scope template into
    one path per concrete scope. Returns the count of new paths created.

    Original templated paths are removed once they've been fanned out.
    """
    paths = spec.get("paths") or {}
    if not paths:
        return 0

    to_remove: List[str] = []
    added: Dict[str, Any] = {}

    for path, item in paths.items():
        if not path.startswith(_DUAL_SCOPE_PREFIX):
            continue
        if not isinstance(item, dict):
            continue
        to_remove.append(path)
        for replacement_prefix, scope_id, op_suffix, tag_suffix in _SCOPES:
            new_path = _rewrite_path(path, replacement_prefix)
            new_item: Dict[str, Any] = {}
            # Carry over any path-item-level parameters (rewritten).
            if isinstance(item.get("parameters"), list):
                new_item["parameters"] = _rewrite_parameters(item["parameters"], scope_id)
            # Carry over each verb's operation, cloned and rewritten.
            for verb in _verbs(item):
                op = copy.deepcopy(item[verb])
                if isinstance(op, dict):
                    if isinstance(op.get("parameters"), list):
                        op["parameters"] = _rewrite_parameters(op["parameters"], scope_id)
                    # Suffix the operationId so the two scoped clones don't
                    # collide downstream.
                    op_id = op.get("operationId")
                    if op_id:
                        op["operationId"] = f"{op_id}_{op_suffix}"
                new_item[verb] = op
            # Carry over any other top-level keys (summary, description, etc.)
            for k, v in item.items():
                if k in new_item or k in _verbs(item) or k == "parameters":
                    continue
                new_item[k] = copy.deepcopy(v)
            added[new_path] = new_item

    for path in to_remove:
        del paths[path]
    paths.update(added)

    return len(added)
