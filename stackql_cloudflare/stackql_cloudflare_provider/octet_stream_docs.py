"""Rewrite doc examples for methods whose request body is
`application/octet-stream`.

Companion to `octet_stream_requests.py`. That pass drops the `naive`
requestBodyTranslate from octet-stream request methods and presents a
single required `value` body column via a `schema_override` wrapper.
With naive translation gone, the body column is only addressable with
the `data__` prefix - but docgen renders body columns unprefixed (or
omits them entirely when it can't project the octet-stream schema).

This pass patches the generated markdown so each affected method's SQL
example shows the body column as `data__value`:

    REPLACE cloudflare.kv.values
    SET data__value = '{{ value }}'
    WHERE account_id = '...' AND namespace_id = '...' AND key_name = '...';

Targets are discovered from the generated provider yamls (any resource
method carrying `request.mediaType: application/octet-stream`), so the
two passes can never drift apart. Only the matched method's TabItem SQL
block is touched - all other examples on the page are left alone.

Runs after `sanitize_docs.py` in the `generate-docs` post-pass chain.
Idempotent.
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml


logger = logging.getLogger(__name__)

PKG_DIR = Path(__file__).resolve().parent
PROVIDER_DIR = (
    PKG_DIR.parent
    / "provider-dev" / "openapi" / "src" / "cloudflare" / "v00.00.00000"
)
DOCS_DIR = PKG_DIR.parent / "website" / "docs" / "services"

_OCTET_STREAM = "application/octet-stream"

_VERB_TO_SECTION = {
    "insert": "INSERT",
    "update": "UPDATE",
    "replace": "REPLACE",
}


def _discover_targets(provider_dir: Path) -> List[Dict]:
    """Walk generated service yamls; return one record per resource
    method with an octet-stream request block:
    {service, resource, method, sql_verb, body_cols}."""
    out: List[Dict] = []
    for svc_path in sorted((provider_dir / "services").glob("*.yaml")):
        spec = yaml.safe_load(svc_path.read_text(encoding="utf-8"))
        if not isinstance(spec, dict):
            continue
        components = spec.get("components") or {}
        schemas = components.get("schemas") or {}
        resources = components.get("x-stackQL-resources") or {}
        for r_name, r in resources.items():
            methods = r.get("methods") or {}
            sql_verbs = r.get("sqlVerbs") or {}
            for m_name, m in methods.items():
                req = m.get("request") or {}
                if req.get("mediaType") != _OCTET_STREAM:
                    continue
                verb = None
                for sv, refs in sql_verbs.items():
                    for x in (refs or []):
                        ref = (x or {}).get("$ref") or ""
                        if ref.endswith("/methods/" + m_name):
                            verb = sv
                if verb not in _VERB_TO_SECTION:
                    logger.debug("%s.%s.%s: no insert/update/replace sqlVerb - skipping",
                                 svc_path.stem, r_name, m_name)
                    continue
                cols = None
                so_ref = (req.get("schema_override") or {}).get("$ref") or ""
                wrapper = schemas.get(so_ref.split("/")[-1]) if so_ref else None
                if isinstance(wrapper, dict):
                    cols = wrapper.get("required") or list((wrapper.get("properties") or {}).keys())
                out.append({
                    "service": svc_path.stem,
                    "resource": r_name,
                    "method": m_name,
                    "sql_verb": verb,
                    "body_cols": cols or ["value"],
                })
    return out


def _rewrite_insert_sql(sql: str, body_cols: List[str]) -> Optional[str]:
    """Rewrite an INSERT example: drop any pre-existing (data__-prefixed
    or bare) body columns and re-insert them data__-prefixed at the top
    of the column list, with matching '{{ col }}' select values."""
    lines = sql.split("\n")
    try:
        open_idx = next(i for i, l in enumerate(lines) if l.rstrip().endswith("("))
        close_idx = next(i for i in range(open_idx + 1, len(lines)) if lines[i].strip() == ")")
        select_idx = next(i for i in range(close_idx, len(lines)) if lines[i].strip().upper() == "SELECT")
    except StopIteration:
        return None
    vals_end = len(lines)
    for i in range(select_idx + 1, len(lines)):
        s = lines[i].strip()
        if s.upper() == "RETURNING" or s == ";":
            vals_end = i
            break

    cols = [l.strip().rstrip(",") for l in lines[open_idx + 1:close_idx] if l.strip()]
    vals = [l.strip().rstrip(",") for l in lines[select_idx + 1:vals_end] if l.strip()]
    if len(cols) != len(vals):
        return None

    drop = {c for c in body_cols} | {"data__" + c for c in body_cols}
    kept = [(c, v) for c, v in zip(cols, vals) if c not in drop]
    injected = [("data__" + c, "'{{ " + c + " }}' /* required */") for c in body_cols]
    pairs = injected + kept

    new_cols = [c + ("," if i < len(pairs) - 1 else "") for i, (c, _) in enumerate(pairs)]
    new_vals = [v + ("," if i < len(pairs) - 1 else "") for i, (_, v) in enumerate(pairs)]
    return "\n".join(
        lines[:open_idx + 1] + new_cols + lines[close_idx:select_idx + 1]
        + new_vals + lines[vals_end:]
    )


def _rewrite_set_sql(sql: str, body_cols: List[str]) -> Optional[str]:
    """Rewrite a REPLACE/UPDATE example: the SET block becomes exactly
    the data__-prefixed body columns (replacing '-- No updatable
    properties' placeholders or unprefixed column lines)."""
    lines = sql.split("\n")
    try:
        set_idx = next(i for i, l in enumerate(lines) if l.strip().upper().startswith("SET"))
        where_idx = next(i for i in range(set_idx + 1, len(lines)) if l_upper(lines[i]).startswith("WHERE"))
    except StopIteration:
        return None
    set_lines = ["data__" + c + " = '{{ " + c + " }}'" for c in body_cols]
    set_lines = [l + "," for l in set_lines[:-1]] + [set_lines[-1]]
    return "\n".join(lines[:set_idx + 1] + set_lines + lines[where_idx:])


def l_upper(line: str) -> str:
    return line.strip().upper()


def _patch_page(page: Path, target: Dict) -> bool:
    """Patch one method's SQL example on one page. Returns True if the
    page content changed."""
    text = page.read_text(encoding="utf-8")
    section_word = _VERB_TO_SECTION[target["sql_verb"]]
    section_re = re.compile(
        r"(## `" + section_word + r"` examples.*?)(?=\n## |\Z)", re.DOTALL)
    sec_m = section_re.search(text)
    if not sec_m:
        logger.warning("%s: no `%s` examples section found", page, section_word)
        return False
    section = sec_m.group(1)

    tab_re = re.compile(
        r'(<TabItem value="' + re.escape(target["method"]) + r'">.*?</TabItem>)', re.DOTALL)
    tab_m = tab_re.search(section)
    if not tab_m:
        logger.warning("%s: no TabItem for method %s in `%s` section",
                       page, target["method"], section_word)
        return False
    tab = tab_m.group(1)

    sql_re = re.compile(r"```sql\n(.*?)```", re.DOTALL)
    sql_m = sql_re.search(tab)
    if not sql_m:
        logger.warning("%s: no sql block in TabItem %s", page, target["method"])
        return False
    sql = sql_m.group(1)

    if any(("data__" + c) in sql for c in target["body_cols"]):
        return False  # already patched

    if target["sql_verb"] == "insert":
        new_sql = _rewrite_insert_sql(sql, target["body_cols"])
    else:
        new_sql = _rewrite_set_sql(sql, target["body_cols"])
    if new_sql is None:
        logger.warning("%s: could not parse sql example for %s.%s",
                       page, target["resource"], target["method"])
        return False
    if new_sql == sql:
        return False

    new_tab = tab.replace(sql_m.group(0), "```sql\n" + new_sql + "```")
    new_section = section.replace(tab, new_tab)
    # newline='\n' so Windows doesn't rewrite the whole file to CRLF
    page.write_text(text.replace(section, new_section), encoding="utf-8", newline="\n")
    return True


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider-dir", default=str(PROVIDER_DIR),
                        help=f"Provider root containing services/. Default: {PROVIDER_DIR}")
    parser.add_argument("--docs-dir", default=str(DOCS_DIR),
                        help=f"Generated docs root (services/). Default: {DOCS_DIR}")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    provider_dir = Path(args.provider_dir)
    docs_dir = Path(args.docs_dir)
    if not (provider_dir / "services").exists():
        logger.error("services/ dir not found at %s.", provider_dir / "services")
        return 1
    if not docs_dir.exists():
        logger.error("docs dir not found at %s. Run `npm run generate-docs` first.", docs_dir)
        return 1

    targets = _discover_targets(provider_dir)
    logger.info("Discovered %d octet-stream request methods.", len(targets))

    patched = 0
    for t in targets:
        page = docs_dir / t["service"] / t["resource"] / "index.md"
        if not page.exists():
            logger.warning("Doc page not found: %s", page)
            continue
        if _patch_page(page, t):
            patched += 1
            logger.info("Patched %s.%s.%s (%s example) -> data__ body columns",
                        t["service"], t["resource"], t["method"], t["sql_verb"])

    logger.info("Patched %d doc examples.", patched)
    return 0


if __name__ == "__main__":
    sys.exit(main())
