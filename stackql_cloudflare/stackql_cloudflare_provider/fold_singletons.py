"""One-shot CSV mutation: fold singleton non-SELECT resources into existing
sibling resources as exec methods.

Many resources in the auto-generated CSV are "verb resources" - a single row
whose name is an action verb (`/move`, `/cancel`, `/purge_cache`, ...) and
whose verb is `insert` / `update` / `replace` / `delete` / `exec`. These
clutter the surface and create non-selectable entries. The cleaner shape is
to fold the operation into a proper sibling parent resource as an `exec`
method (`accounts.set_pay_per_crawl_zones`, `datasets.move`,
`zones.purge_cache`, ...).

This script:

  1. Builds a per-service inventory of "parent" candidates - any resource
     that has at least one SELECT (it's a real noun the user queries).
  2. Iterates singleton non-SELECT resources from `billing.yaml` onwards
     (services before that have been hand-curated already).
  3. For each, picks the best sibling parent by longest-path-prefix match.
     Falls back to the service name's "natural" anchor resource (e.g.
     `accounts` in `accounts.yaml`, `zones` in `zones.yaml`).
  4. Synthesises a clean method name from the action leaf / SDK method.
  5. Sets stackql_verb=`exec` for all folds (lifecycle / RPC semantics).
  6. Writes the CSV in place.

Run via:
    python -m stackql_cloudflare_provider.fold_singletons --dry-run
    python -m stackql_cloudflare_provider.fold_singletons        # commit
"""
from __future__ import annotations

import argparse
import csv
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple


logger = logging.getLogger(__name__)

PKG_DIR = Path(__file__).resolve().parent
CSV_PATH = PKG_DIR.parent / "provider-dev" / "config" / "all_services.csv"


# Services BEFORE this are assumed hand-curated and untouched.
# `billing.yaml` is the first one whose singletons we fold.
START_FROM = "billing.yaml"


# A method name is a "real verb" (not a noun) if it starts with one of these.
# We use it to decide whether the existing method name is already a good
# fit for an `exec` fold or needs to be derived from the path.
_ACTION_VERB_PREFIXES = (
    "abort", "activate", "ack", "apply", "approve", "attach", "batch", "bulk",
    "cancel", "check", "clear", "clone", "complete", "convert", "copy",
    "create", "deactivate", "deny", "detach", "disable", "discover",
    "dismiss", "dispatch", "download", "duplicate", "edit", "enable",
    "escalate", "expire", "export", "flush", "force", "generate", "get",
    "import", "impersonate", "invalidate", "invite", "issue", "kick",
    "list", "lock", "login", "logout", "migrate", "move", "mute", "new",
    "pause", "plan", "populate", "post", "preview", "publish", "pull",
    "purge", "push", "query", "reboot", "rebuild", "reclassify", "redeem",
    "refresh", "register", "reject", "release", "renew", "reorder",
    "reroute", "reset", "restart", "restore", "resume", "retire", "retry",
    "rerun", "revoke", "rollback", "rotate", "run", "scan", "schedule",
    "search", "send", "set", "share", "signal", "snapshot", "start", "stop",
    "submit", "subscribe", "suspend", "sync", "test", "tokenize", "trigger",
    "unassign", "unbind", "unlock", "unregister", "unrevoke", "unshare",
    "unsubscribe", "update", "upload", "upsert", "validate", "verify",
)


# A small set of explicit fold targets where the natural sibling parent
# isn't obvious from the path prefix. The key is (filename,
# stackql_resource_name) of the singleton; the value is
# (target_parent_resource_name, method_name, stackql_verb).
#
# Only used when the automatic algorithm can't find a sibling. Most folds
# are handled algorithmically.
EXPLICIT_FOLDS: Dict[Tuple[str, str], Tuple[str, str, str]] = {
    # billing
    ("billing.yaml", "zones_can_be_enabled"): ("accounts", "set_pay_per_crawl_zones", "exec"),
    ("billing.yaml", "query"):                 ("accounts", "query_pay_per_crawl_zones", "exec"),
    # cache
    ("cache.yaml",   "purge_cache"):           ("zones", "purge_cache", "exec"),
    # zones
    ("zones.yaml",   "activation_check"):      ("zones", "trigger_activation_check", "exec"),
}


def _snake(s: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s or "")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_").lower()
    return s


def _read_csv(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    return fields, rows


def _write_csv(path: Path, fields: List[str], rows: List[Dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def _path_static_segments(path: str) -> List[str]:
    return [s for s in path.strip("/").split("/")
            if s and not (s.startswith("{") and s.endswith("}"))]


def _is_param_segment(seg: str) -> bool:
    return seg.startswith("{") and seg.endswith("}")


def _strip_leading_scope(segs: List[str]) -> List[str]:
    """Drop leading scope segments (accounts, zones, user, etc.) and version
    markers (v1, v2, ...) so the remaining segments describe the capability
    hierarchy."""
    SCOPE = {"accounts", "zones", "user", "users", "organizations", "memberships", "tenants"}
    VERSIONS = re.compile(r"^v\d+$")
    out = list(segs)
    while out and out[0] in SCOPE:
        out.pop(0)
    # Drop a leading version segment (e.g. v2)
    while out and VERSIONS.match(out[0]):
        out.pop(0)
    return out


def _candidate_parent_names(path: str) -> List[str]:
    """Return potential parent resource names derived from the path,
    most-specific first. Skips version segments (v1, v2) and the leading
    scope so candidates are real resource nouns.

    For /accounts/{id}/cloudforce-one/events/dataset/{dataset_id}/move:
      static segs after scope = ['cloudforce-one', 'events', 'dataset', 'move']
      parents to try (in order):
        'datasets', 'dataset', 'events', 'cloudforce_one'

    For /accounts/{id}/images/v1/{image_id}/blob:
      after stripping scope+versions: ['images', 'blob']
      candidates: 'images' (drop 'blob' as it's the action leaf)
    """
    segs = _path_static_segments(path)
    inner = _strip_leading_scope(segs)
    # Strip any version segments that survived (e.g. /cloudforce-one/v2/...
    # gives us inner = ['cloudforce-one', 'v2', ...]). We already strip
    # leading versions; this catches mid-path ones.
    VER = re.compile(r"^v\d+$")
    inner = [s for s in inner if not VER.match(s)]
    if len(inner) < 2:
        return inner[:]  # might still be useful as a fallback parent
    # The trailing static segment is the verb itself - drop it and use the
    # one before as the most-specific candidate, then walk leftward.
    body = inner[:-1]
    out: List[str] = []
    for s in reversed(body):
        snake = _snake(s.replace("-", "_"))
        # Try both as-is and pluralised (datasets vs dataset).
        if snake not in out:
            out.append(snake)
        # Add a pluralised form too if it differs.
        if snake.endswith("y"):
            plural = snake[:-1] + "ies"
        elif snake.endswith("s"):
            plural = snake
        else:
            plural = snake + "s"
        if plural != snake and plural not in out:
            out.append(plural)
    return out


def _select_sibling_parent(
    candidates: List[str],
    siblings: Dict[str, Dict[str, int]],
) -> Optional[str]:
    """Pick the best sibling resource to fold into. `siblings` maps
    resource_name -> {verb: count}. We prefer:
      1. A sibling that already exists AND has a SELECT (true parent).
      2. Otherwise, any existing sibling.
    """
    for cand in candidates:
        info = siblings.get(cand)
        if info and info.get("select", 0) > 0:
            return cand
    for cand in candidates:
        if cand in siblings:
            return cand
    return None


def _strip_existing_version_suffix(name: str) -> str:
    """Remove trailing `_v1`, `_v2`, ... or `_v1b` from a method name."""
    return re.sub(r"_v\d+[a-z]?$", "", name)


def _derive_exec_method_name(row: Dict[str, str], parent: str) -> str:
    """Build a clean snake_case method name for the folded row when its
    parent is `parent`. Prefer the action verb in the path leaf, qualified
    by enough context to be readable.

    Special cases:
      - If the path leaf is a {param} (path ends in an ID like {event_id}),
        derive the method name from the HTTP verb + previous static segment
        (which is the noun being acted on).
      - Version segments (`v1`, `v2`) get appended to the method name so
        v2 endpoints don't collide with their v1 counterparts.
    """
    path = row["path"]
    segs = path.strip("/").split("/")
    if not segs:
        return _snake(row["stackql_method_name"] or "exec")

    static_only = [s for s in segs if not _is_param_segment(s)]
    inner = _strip_leading_scope(static_only)
    # Extract any version markers for qualification.
    VER = re.compile(r"^v\d+$")
    versions = [s for s in inner if VER.match(s)]
    version_suffix = "_" + "_".join(versions) if versions else ""

    last_seg = segs[-1]
    if _is_param_segment(last_seg):
        # Path ends in {id} - the action is the HTTP verb on whatever
        # the previous static segment is.
        prev_static = next((s for s in reversed(segs[:-1]) if not _is_param_segment(s)), "")
        prev_clean = _snake(prev_static.replace("-", "_"))
        http_verb = row["verb"]
        if http_verb == "get":
            base = f"get_{prev_clean}"
        elif http_verb == "delete":
            base = f"delete_{prev_clean}"
        elif http_verb in ("put", "patch"):
            base = f"update_{prev_clean}"
        else:
            base = _snake(row["stackql_method_name"]) or http_verb
        return f"{base}{version_suffix}"

    leaf = _snake(last_seg.replace("-", "_"))

    # If the leaf is an action verb, use it as-is + version suffix.
    if leaf.split("_", 1)[0] in _ACTION_VERB_PREFIXES:
        return f"{leaf}{version_suffix}"

    # Leaf is a noun (e.g. `pdf`, `screenshot`, `traceroute`). Qualify it
    # with the HTTP verb so multiple noun-leaves folded into the same
    # parent don't collide (e.g. all become `browser_rendering.create`).
    # This is preferred over the existing method name (which is often a
    # generic `create`) because the leaf carries the distinguishing info.
    http_verb = row["verb"]
    verb_prefix = {"post": "create", "get": "get", "put": "update", "patch": "update", "delete": "delete"}.get(http_verb, http_verb)
    return f"{verb_prefix}_{leaf}{version_suffix}"


def _has_user_edits(
    row: Dict[str, str],
    auto_resource: str,
    auto_method: str,
    auto_verb: str,
) -> bool:
    """Detect if the existing row was hand-edited - if so we leave it.
    A row matches the auto-defaulter's output exactly when *no one has
    touched it*. We just check the three columns we own."""
    return not (
        row["stackql_resource_name"] == auto_resource
        and row["stackql_method_name"] == auto_method
        and row["stackql_verb"] == auto_verb
    )


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the plan; do not write the CSV.")
    parser.add_argument("--start-from", default=START_FROM,
                        help=f"Service yaml filename to start from (alphabetical). Default: {START_FROM}")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    fields, rows = _read_csv(CSV_PATH)
    logger.info("Loaded %d rows from %s", len(rows), CSV_PATH)

    # Inventory: per-(filename, resource), count rows by sql verb.
    by_resource: Dict[Tuple[str, str], Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for r in rows:
        by_resource[(r["filename"], r["stackql_resource_name"])][r["stackql_verb"]] += 1

    # Inventory per-service: resource_name -> {verb: count}
    siblings_per_service: Dict[str, Dict[str, Dict[str, int]]] = defaultdict(dict)
    for (fn, rn), verb_counts in by_resource.items():
        siblings_per_service[fn][rn] = dict(verb_counts)

    # Identify singleton non-SELECT resources from start_from onwards.
    plan: List[Tuple[Dict[str, str], str, str, str]] = []  # (row, new_res, new_method, new_verb)
    skipped: List[Tuple[Dict[str, str], str]] = []

    for r in rows:
        if r["filename"] < args.start_from:
            continue
        info = by_resource[(r["filename"], r["stackql_resource_name"])]
        total = sum(info.values())
        has_select = info.get("select", 0) > 0
        # Only fold singletons that are not selectable.
        if total != 1 or has_select:
            continue

        # Explicit fold table wins.
        key = (r["filename"], r["stackql_resource_name"])
        if key in EXPLICIT_FOLDS:
            new_res, new_method, new_verb = EXPLICIT_FOLDS[key]
            plan.append((r, new_res, new_method, new_verb))
            continue

        candidates = _candidate_parent_names(r["path"])
        siblings = siblings_per_service.get(r["filename"], {})
        # Don't fold into self.
        candidates = [c for c in candidates if c != r["stackql_resource_name"]]
        parent = _select_sibling_parent(candidates, siblings)
        if parent is None:
            # Last-ditch fallback: fold into the service's namesake resource
            # if it exists; otherwise the first static segment after the
            # scope (which becomes a brand-new parent resource).
            service_root = r["filename"].replace(".yaml", "")
            if service_root in siblings and service_root != r["stackql_resource_name"]:
                parent = service_root
            else:
                static_segs = _path_static_segments(r["path"])
                inner = _strip_leading_scope(static_segs)
                VER = re.compile(r"^v\d+$")
                inner = [s for s in inner if not VER.match(s)]
                # The leaf is the action; the first remaining segment is
                # the natural parent noun.
                if len(inner) >= 2:
                    parent = _snake(inner[0].replace("-", "_"))
                else:
                    skipped.append((r, "no sibling parent found"))
                    continue

        # Detect mis-classified GETs: an HTTP GET that returns a list
        # (method name ends in `_list`, is bare `list`, or contains
        # `list_by_`) is a real listing operation. Make it a SELECT method.
        # If the path leaf is a noun (not an action), preserve the noun as
        # its own child resource under the parent so the SQL surface stays
        # discoverable. Otherwise fold into the parent as `list_<leaf>`.
        new_verb = "exec"
        new_method = _derive_exec_method_name(r, parent)
        if r["verb"] == "get" and (
            r["stackql_method_name"].endswith("_list")
            or r["stackql_method_name"] == "list"
            or "list_by_" in r["stackql_method_name"]
        ):
            static_segs = _path_static_segments(r["path"])
            leaf_raw = static_segs[-1] if static_segs else ""
            leaf_snake = _snake(leaf_raw.replace("-", "_"))
            leaf_is_noun = leaf_snake and leaf_snake.split("_", 1)[0] not in _ACTION_VERB_PREFIXES

            if leaf_is_noun:
                # Promote: make the leaf a sibling resource (not a fold).
                # e.g. /cloudforce-one/requests/{id}/asset -> resource `assets`
                # under cloudforce_one, method `list/select`.
                # Pluralise the noun for the resource name.
                if leaf_snake.endswith("y"):
                    promoted = leaf_snake[:-1] + "ies"
                elif leaf_snake.endswith("s"):
                    promoted = leaf_snake
                else:
                    promoted = leaf_snake + "s"
                parent = promoted
                new_method = "list"
                new_verb = "select"
            else:
                # Action-named leaf - fold into the parent as exec list.
                parent_info = siblings.get(parent, {})
                if parent_info.get("select", 0) == 0:
                    new_verb = "select"
                    new_method = "list"
                else:
                    new_verb = "exec"
                    new_method = _derive_exec_method_name(r, parent)

        plan.append((r, parent, new_method, new_verb))

    logger.info("Plan: %d folds, %d skipped (no sibling parent)", len(plan), len(skipped))

    # Print a tabular preview.
    if args.dry_run or args.verbose:
        for row, new_res, new_method, new_verb in plan[:50]:
            logger.info(
                "  %s | %s | %s.%s/%s -> %s.%s/%s",
                row["filename"],
                row["path"],
                row["stackql_resource_name"], row["stackql_method_name"], row["stackql_verb"],
                new_res, new_method, new_verb,
            )
        if len(plan) > 50:
            logger.info("  ... %d more", len(plan) - 50)
        for row, why in skipped[:20]:
            logger.info("  SKIP %s | %s (%s)", row["filename"], row["path"], why)
        if len(skipped) > 20:
            logger.info("  ... %d more skipped", len(skipped) - 20)

    if args.dry_run:
        logger.info("Dry run - no changes written.")
        return 0

    # Apply.
    updates_by_key = {
        (r["filename"], r["path"], r["verb"]): (nr, nm, nv)
        for r, nr, nm, nv in plan
    }
    n = 0
    for r in rows:
        key = (r["filename"], r["path"], r["verb"])
        if key in updates_by_key:
            nr, nm, nv = updates_by_key[key]
            r["stackql_resource_name"] = nr
            r["stackql_method_name"] = nm
            r["stackql_verb"] = nv
            n += 1

    _write_csv(CSV_PATH, fields, rows)
    logger.info("Applied %d row updates to %s", n, CSV_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
