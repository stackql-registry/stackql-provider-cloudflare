"""Consistent identifier renaming across the upstream OpenAPI spec.

StackQL treats schema names as opaque - we can rename them however we like as
long as we update every `$ref` that points at them. Upstream Cloudflare uses
three different styles (snake_case, kebab-case, snake_PascalCase) mixed
freely, so we normalize all schema names to camelCase for consistency.

For path templates, we control the parameter names (they appear in our
generated yamls), so we snake_case those. We also rename the matching
`parameters[].name` for `in: path` entries.

We do NOT touch query, header, or body parameter names - the server
implements them and we have to accept whatever the upstream spec says.
"""
from __future__ import annotations

import re
from typing import Any, Dict


# --- name transformers ----------------------------------------------------


_CAMEL_SPLIT_RE = re.compile(r"[-_\s]+")
_CAMEL_LOWER_UPPER_RE = re.compile(r"([a-z0-9])([A-Z])")
_CAMEL_UPPER_LOWER_RE = re.compile(r"([A-Z]+)([A-Z][a-z])")


def to_camel(name: str) -> str:
    """Convert any common style (snake_case, kebab-case, PascalCase,
    snake_PascalCase mix, dot-separated) to camelCase.

    Examples:
        'iam_account'                       -> 'iamAccount'
        'email-security_ClientError'        -> 'emailSecurityClientError'
        'builds_APIResponse'                -> 'buildsAPIResponse'
        'access_apps_components-schemas-single_response'
            -> 'accessAppsComponentsSchemasSingleResponse'
        'AbuseReport'                       -> 'abuseReport'
        'ALLcaps'                           -> 'aLLcaps'  (edge: not common in upstream)
    """
    if not name:
        return name
    # Split on every non-alphanumeric separator we know about.
    parts = [p for p in _CAMEL_SPLIT_RE.split(name) if p]
    if not parts:
        return name
    out = []
    for i, p in enumerate(parts):
        if i == 0:
            # First part: lowercase the leading letter, leave the rest as-is.
            out.append(p[:1].lower() + p[1:])
        else:
            # Capitalize the first character. Preserve subsequent characters
            # (keeps acronyms like `APIResponse` intact when they come in as
            # `_APIResponse`).
            out.append(p[:1].upper() + p[1:])
    return "".join(out)


def to_snake(name: str) -> str:
    """Convert any common style to snake_case. Used for path parameter names."""
    if not name:
        return name
    # Replace hyphens / spaces with underscores; collapse runs.
    s = re.sub(r"[-\s]+", "_", name)
    # Insert underscore between lower->upper / upper->upper+lower transitions.
    s = _CAMEL_LOWER_UPPER_RE.sub(r"\1_\2", s)
    s = _CAMEL_UPPER_LOWER_RE.sub(r"\1_\2", s)
    s = re.sub(r"_+", "_", s)
    return s.strip("_").lower()


# --- schema renaming -----------------------------------------------------


_SCHEMA_REF_PREFIX = "#/components/schemas/"


def _walk_refs(node: Any, mapping: Dict[str, str]) -> Any:
    """Walk a JSON-ish tree and rewrite every '$ref' that points at
    `components/schemas/<old>` to point at `components/schemas/<new>`."""
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith(_SCHEMA_REF_PREFIX):
            old = ref[len(_SCHEMA_REF_PREFIX):]
            new = mapping.get(old)
            if new and new != old:
                node["$ref"] = _SCHEMA_REF_PREFIX + new
        for k, v in list(node.items()):
            node[k] = _walk_refs(v, mapping)
        return node
    if isinstance(node, list):
        return [_walk_refs(v, mapping) for v in node]
    return node


def rename_schemas_to_camel(spec: dict) -> int:
    """Rename every component schema to camelCase and rewrite all $refs to
    match. Returns the count of names that actually changed.

    If two upstream names collapse to the same camelCase form, we keep the
    second occurrence under a deterministic numeric suffix (rare on
    Cloudflare's spec - mostly the old/new names differ only in punctuation).
    """
    schemas = (spec.get("components") or {}).get("schemas") or {}
    if not schemas:
        return 0

    # Compute new names with collision avoidance.
    mapping: Dict[str, str] = {}
    used: set = set()
    for old in list(schemas.keys()):
        new = to_camel(old)
        if not new:
            new = old
        # Collision avoidance: if this camel form is already taken by a
        # different source name, suffix _2, _3, ...
        candidate = new
        n = 2
        while candidate in used and candidate != old:
            candidate = f"{new}_{n}"
            n += 1
        used.add(candidate)
        mapping[old] = candidate

    # Rebuild components.schemas with the new keys.
    new_schemas: Dict[str, Any] = {}
    for old, sch in schemas.items():
        new_schemas[mapping[old]] = sch
    spec["components"]["schemas"] = new_schemas

    # Rewrite every $ref in the whole spec.
    _walk_refs(spec, mapping)

    return sum(1 for o, n in mapping.items() if o != n)


# --- path parameter renaming ---------------------------------------------


_PATH_PARAM_RE = re.compile(r"\{([^}]+)\}")


def rename_path_params_to_snake(spec: dict) -> int:
    """For every path template, rewrite {paramName} placeholders to
    {snake_param_name}, and update the matching `parameters[].name` entries
    on every operation under that path. Path-level parameters are also
    rewritten (the path-item-level merge happens later).

    Returns the count of renames performed.
    """
    paths = spec.get("paths") or {}
    renamed_paths: Dict[str, Any] = {}
    rename_count = 0
    for original_path, item in list(paths.items()):
        # Build the per-path rename map: {old_param -> new_param}.
        param_map: Dict[str, str] = {}
        for m in _PATH_PARAM_RE.finditer(original_path):
            old = m.group(1)
            new = to_snake(old)
            if new and new != old:
                param_map[old] = new
        new_path = original_path
        if param_map:
            # Substitute placeholders in the path template.
            def _sub(match: "re.Match[str]") -> str:
                old = match.group(1)
                return "{" + param_map.get(old, old) + "}"
            new_path = _PATH_PARAM_RE.sub(_sub, original_path)
            # Also rename the matching parameter entries on every operation
            # and the path-item-level parameters block.
            for verb_or_key in list(item.keys() if isinstance(item, dict) else []):
                section = item.get(verb_or_key)
                if verb_or_key == "parameters" and isinstance(section, list):
                    for p in section:
                        if isinstance(p, dict) and p.get("in") == "path":
                            nm = p.get("name")
                            if nm in param_map:
                                p["name"] = param_map[nm]
                                rename_count += 1
                elif isinstance(section, dict) and "parameters" in section:
                    for p in section.get("parameters") or []:
                        if isinstance(p, dict) and p.get("in") == "path":
                            nm = p.get("name")
                            if nm in param_map:
                                p["name"] = param_map[nm]
                                rename_count += 1
        renamed_paths[new_path] = item
    spec["paths"] = renamed_paths
    return rename_count
