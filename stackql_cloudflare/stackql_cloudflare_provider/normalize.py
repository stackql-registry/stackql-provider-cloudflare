"""Schema normalization for StackQL: collapse allOf / oneOf / anyOf into a
single flat schema (superset of properties, deduplicated by key) and strip
additionalProperties / discriminator.

StackQL projects schemas onto a relational model, so polymorphism creates
problems: a column can't be one of N shapes. We pre-normalize before the
provider-utils' own normalize step so we keep tight control over what each
schema becomes.

Strategy:
- allOf:    UNION - merge every member into the parent. `required` is unioned
            (a property is required if any composed-in piece requires it,
            consistent with the OpenAPI semantics of `allOf` as inheritance).
- oneOf:    MERGE + DEDUP - same property-union as allOf. `required` is
            intersected across branches: only mark required if every branch
            requires it, otherwise the value may legitimately be absent for
            some branches.
- anyOf:    Treated identically to oneOf.
- additionalProperties: deleted.
- discriminator: deleted (the polymorphism it described has been flattened).

For all three, key-on-key conflicts keep the first-seen property (no second
pass overwrites). `type` / `format` / `description` / `enum` etc. only fall
through onto the parent when the parent doesn't already have one. Cycles in
`$ref` chains are broken via a `seen` set carried through the recursion.
"""
from __future__ import annotations

import copy
from typing import Any, Dict, List, Optional, Set


_REF_PREFIX = "#/components/schemas/"


def _is_ref(obj: Any) -> bool:
    return isinstance(obj, dict) and "$ref" in obj


def _resolve(ref: str, schemas: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if not ref.startswith(_REF_PREFIX):
        return None
    name = ref[len(_REF_PREFIX):]
    return schemas.get(name)


def _merge_properties(target: Dict[str, Any], src_props: Dict[str, Any]) -> None:
    """Union src_props into target['properties']. First definition wins on key clash."""
    if not src_props:
        return
    tp = target.setdefault("properties", {})
    for k, v in src_props.items():
        if k not in tp:
            tp[k] = v


def _merge_required(target: Dict[str, Any], src_req: List[str], intersect: bool) -> None:
    src_set = set(src_req or [])
    if "required" not in target:
        target["required"] = list(src_set) if not intersect else list(src_set)
        return
    cur = set(target["required"])
    if intersect:
        target["required"] = sorted(cur & src_set)
    else:
        target["required"] = sorted(cur | src_set)


def _merge_into(target: Dict[str, Any], src: Dict[str, Any], intersect_required: bool) -> None:
    """Merge `src` schema into `target`. Properties union; required follows
    `intersect_required` flag. Type/format/description fall through if target
    doesn't have one."""
    if not isinstance(src, dict):
        return
    # type/format/title/description: only fill in if missing on target.
    for key in ("type", "format", "title", "description", "example", "default", "items"):
        if key in src and key not in target:
            target[key] = copy.deepcopy(src[key])
    if "enum" in src and "enum" not in target:
        target["enum"] = list(src["enum"])
    _merge_properties(target, src.get("properties", {}))
    if "required" in src:
        _merge_required(target, src["required"], intersect_required)


def _normalize_schema(
    sch: Any,
    schemas: Dict[str, Any],
    seen: Set[str],
) -> Any:
    """Walk a schema in-place, flattening polymorphism. Returns the (possibly
    new) value to replace the input with."""
    if isinstance(sch, list):
        return [_normalize_schema(s, schemas, seen) for s in sch]
    if not isinstance(sch, dict):
        return sch

    # additionalProperties + discriminator: delete unconditionally.
    sch.pop("additionalProperties", None)
    sch.pop("discriminator", None)

    # $ref: once we've scrubbed sibling polymorphism keywords, leave the ref
    # alone. The schemas it points to are normalized at the top level.
    if "$ref" in sch:
        return sch

    # Flatten allOf.
    if "allOf" in sch:
        members = sch.pop("allOf")
        for m in members:
            if _is_ref(m):
                ref_name = m["$ref"][len(_REF_PREFIX):] if m["$ref"].startswith(_REF_PREFIX) else None
                if ref_name and ref_name not in seen:
                    target = _resolve(m["$ref"], schemas)
                    if isinstance(target, dict):
                        new_seen = seen | {ref_name}
                        resolved = _normalize_schema(copy.deepcopy(target), schemas, new_seen)
                        _merge_into(sch, resolved, intersect_required=False)
            elif isinstance(m, dict):
                resolved = _normalize_schema(copy.deepcopy(m), schemas, seen)
                _merge_into(sch, resolved, intersect_required=False)

    # Collapse oneOf/anyOf into a union of properties (intersect required).
    for keyword in ("oneOf", "anyOf"):
        if keyword in sch:
            members = sch.pop(keyword)
            for i, m in enumerate(members):
                if _is_ref(m):
                    ref_name = m["$ref"][len(_REF_PREFIX):] if m["$ref"].startswith(_REF_PREFIX) else None
                    if ref_name and ref_name in seen:
                        continue
                    target = _resolve(m["$ref"], schemas)
                    if isinstance(target, dict):
                        new_seen = seen | ({ref_name} if ref_name else set())
                        resolved = _normalize_schema(copy.deepcopy(target), schemas, new_seen)
                        _merge_into(sch, resolved, intersect_required=(i > 0))
                elif isinstance(m, dict):
                    resolved = _normalize_schema(copy.deepcopy(m), schemas, seen)
                    _merge_into(sch, resolved, intersect_required=(i > 0))

    # After flattening, if we have at least one property and no `type`, force
    # type to object; if we have `items` and no `type`, force `array`.
    if "properties" in sch and "type" not in sch:
        sch["type"] = "object"
    if "items" in sch and "type" not in sch:
        sch["type"] = "array"

    # Recurse into nested constructs.
    if "properties" in sch:
        sch["properties"] = {
            k: _normalize_schema(v, schemas, seen)
            for k, v in sch["properties"].items()
        }
    if "items" in sch:
        sch["items"] = _normalize_schema(sch["items"], schemas, seen)
    if "parameters" in sch:
        sch["parameters"] = [_normalize_schema(p, schemas, seen) for p in sch["parameters"]]
    return sch


def normalize_schemas(schemas: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize every component schema in place. Returns the same dict."""
    for name in list(schemas.keys()):
        schemas[name] = _normalize_schema(schemas[name], schemas, seen={name})
    return schemas


def normalize_inline(obj: Any, schemas: Dict[str, Any]) -> Any:
    """Normalize an arbitrary inline schema (e.g. inside a parameter,
    response body, or request body)."""
    return _normalize_schema(obj, schemas, seen=set())


def fix_required_without_properties(node: Any) -> Any:
    """Walk a schema tree and drop `required` from any object that lacks
    `properties`. Some upstream definitions list required fields but have
    no properties block (the names came from the polymorphic branches that
    we've since collapsed away). Tooling downstream of us assumes that
    `required[i]` always has a matching `properties[name]`, so reconcile.
    """
    if isinstance(node, dict):
        if "required" in node and not node.get("properties"):
            node.pop("required", None)
        for k in list(node.keys()):
            node[k] = fix_required_without_properties(node[k])
    elif isinstance(node, list):
        return [fix_required_without_properties(v) for v in node]
    return node
