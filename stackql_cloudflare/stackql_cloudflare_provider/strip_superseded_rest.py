"""Strip upstream REST endpoints that have been superseded by hand-authored
GraphQL operations.

Read the GraphQL manifest's `replaces_rest` entries and, for each
(path, verb) listed:

  1. Remove the operation from the matching `provider-dev/source/<service>.yaml`.
     If the path-item is left with no verbs after removal, remove the
     path entry entirely.
  2. Remove the matching row from `provider-dev/config/all_services.csv`
     (identity key is `(filename, path, verb)`).

Run between Step 2 (assign_resource_names) and Step 3 (generate-provider)
so the downstream provider + docs are built without the dead endpoints.

Why this exists: when an upstream REST endpoint is sunset (e.g.
`/zones/{id}/analytics/dashboard` returns code 1015) we don't want it
appearing in `SHOW METHODS`, `DESCRIBE`, or the docusaurus site as a
broken trap. The GraphQL-backed resource that replaces it is the
documented path forward.

Idempotent: re-running after the rows are already stripped is a no-op.

Usage:
    python -m stackql_cloudflare_provider.strip_superseded_rest
    python -m stackql_cloudflare_provider.strip_superseded_rest --dry-run
"""
from __future__ import annotations

import argparse
import csv
import logging
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml


logger = logging.getLogger(__name__)


# YAML 1.1 truthy/falsy guard (matches the other passes' dumper config).
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
SOURCE_DIR = PROVIDER_DEV / "source"
SOURCE_GRAPHQL = PROVIDER_DEV / "source-graphql"
ALL_SERVICES_CSV = PROVIDER_DEV / "config" / "all_services.csv"
GRAPHQL_MANIFEST = SOURCE_GRAPHQL / "manifest.yaml"


def _load_manifest() -> List[dict]:
    if not GRAPHQL_MANIFEST.exists():
        return []
    data = yaml.safe_load(GRAPHQL_MANIFEST.read_text(encoding="utf-8")) or {}
    return data.get("operations") or []


def _collect_targets(operations: List[dict]) -> List[Tuple[str, str, str]]:
    """Flatten manifest replaces_rest entries into (service, path, verb)
    tuples. service comes from the manifest entry; path + verb come from
    each replaces_rest item.
    """
    targets: List[Tuple[str, str, str]] = []
    for op in operations:
        service = op.get("service")
        if not service:
            continue
        for entry in (op.get("replaces_rest") or []):
            path = entry.get("path")
            verb = (entry.get("verb") or "get").lower()
            if path:
                targets.append((service, path, verb))
    return targets


def _strip_from_source_yaml(service: str, victims: List[Tuple[str, str]], dry_run: bool) -> Tuple[int, int]:
    """Remove victim (path, verb) entries from provider-dev/source/<service>.yaml.

    Returns (ops_removed, paths_removed). If a path-item is left with no
    verbs after removal, the path entry itself is removed.
    """
    service_path = SOURCE_DIR / f"{service}.yaml"
    if not service_path.exists():
        logger.warning("Source yaml not found, skipping: %s", service_path)
        return (0, 0)

    doc = yaml.safe_load(service_path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        return (0, 0)

    paths = doc.get("paths") or {}
    ops_removed = 0
    paths_removed = 0
    for path, verb in victims:
        item = paths.get(path)
        if not isinstance(item, dict):
            continue
        if verb in item:
            del item[verb]
            ops_removed += 1
            logger.info("  strip: %s %s %s", service_path.name, verb.upper(), path)
        # If only non-operation keys remain (e.g. `parameters`, `summary`)
        # OR nothing at all, drop the path entry. We treat the absence
        # of any HTTP verb as "empty enough to remove".
        remaining_verbs = {v for v in ("get", "put", "post", "delete", "patch", "options", "head") if v in item}
        if not remaining_verbs:
            del paths[path]
            paths_removed += 1
            logger.debug("  removed empty path entry: %s", path)

    if (ops_removed or paths_removed) and not dry_run:
        with service_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(doc, f, sort_keys=False, default_flow_style=False, width=1000)

    return (ops_removed, paths_removed)


def _strip_from_csv(targets: List[Tuple[str, str, str]], dry_run: bool) -> int:
    """Remove rows from all_services.csv whose (filename, path, verb)
    matches a target. service maps to filename via `<service>.yaml`.

    Returns the number of rows removed.
    """
    if not ALL_SERVICES_CSV.exists():
        logger.warning("CSV not found, skipping: %s", ALL_SERVICES_CSV)
        return 0

    victim_keys: Set[Tuple[str, str, str]] = {
        (f"{service}.yaml", path, verb.lower())
        for service, path, verb in targets
    }

    rows_kept: List[List[str]] = []
    header: List[str] = []
    rows_removed = 0
    with ALL_SERVICES_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        # `filename` is col 0, `path` is col 1, `verb` is col 4 per the
        # CSV header we just read.
        for row in reader:
            if len(row) < 5:
                rows_kept.append(row)
                continue
            key = (row[0], row[1], row[4].lower())
            if key in victim_keys:
                rows_removed += 1
                logger.info("  strip CSV: %s,%s,%s", *key)
                continue
            rows_kept.append(row)

    if rows_removed and not dry_run:
        with ALL_SERVICES_CSV.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows_kept)

    return rows_removed


def strip(dry_run: bool = False) -> int:
    operations = _load_manifest()
    if not operations:
        logger.info("No GraphQL operations declared; nothing to strip.")
        return 0

    targets = _collect_targets(operations)
    if not targets:
        logger.info("No replaces_rest entries in manifest; nothing to strip.")
        return 0

    logger.info("Stripping %d superseded REST endpoint(s)", len(targets))
    if dry_run:
        logger.info("DRY RUN - no files will be modified")

    # Group by service for fewer yaml round-trips.
    by_service: Dict[str, List[Tuple[str, str]]] = {}
    for service, path, verb in targets:
        by_service.setdefault(service, []).append((path, verb))

    total_ops = 0
    total_paths = 0
    for service, victims in sorted(by_service.items()):
        ops_n, paths_n = _strip_from_source_yaml(service, victims, dry_run)
        total_ops += ops_n
        total_paths += paths_n

    csv_n = _strip_from_csv(targets, dry_run)

    logger.info(
        "Done. Removed %d operations (%d empty paths) from source yamls, %d rows from %s.",
        total_ops,
        total_paths,
        csv_n,
        ALL_SERVICES_CSV.name,
    )
    return 0


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be removed without modifying any files.",
    )
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    return strip(dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
