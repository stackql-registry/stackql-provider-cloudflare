"""Enhance the Workers AI task-family doc pages (and the generic run
page).

Docgen renders the family resources mechanically, which leaves two gaps:

1. The SELECT example only shows the REQUIRED params (`account_id`,
   `model_name`) in the WHERE clause - the model input properties
   (prompt, text, audio, ...) come from the `request.schema_override`
   union schema which docgen does not surface. Without them the example
   is not a runnable query.
2. Nothing tells the reader which models are valid for `model_name`.

This pass, driven by `provider-dev/config/ai_task_families.yaml`,
rewrites each family page (`website/docs/services/ai/<family>/index.md`)
plus the generic `run` page:

- Inserts a `:::info[Supported models]` admonition after the Overview
  table listing every member model as a `<CopyableCode />` entry (the
  run page lists all families' members plus the octet-input exec-only
  models).
- Rewrites the SELECT example: the column list becomes the family's
  typed result fields (or `contents`), and the WHERE clause gains the
  family's primary input properties as commented optional params.

Runs after `octet_stream_docs.py` in the generate-docs chain.
Idempotent: the admonition is replaced between markers and the sql block
is rebuilt deterministically.
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

import yaml


logger = logging.getLogger(__name__)

PKG_DIR = Path(__file__).resolve().parent
CONFIG_PATH = PKG_DIR.parent / "provider-dev" / "config" / "ai_task_families.yaml"
DOCS_AI_DIR = PKG_DIR.parent / "website" / "docs" / "services" / "ai"

# Primary input properties shown as WHERE params in each family's SELECT
# example. These are illustrative (the full union of inputs is in the
# request schema); pick the ones a first query actually needs.
EXAMPLE_INPUTS: Dict[str, List[str]] = {
    "text_generation": ["prompt"],
    "text_embeddings": ["text"],
    "text_to_image": ["prompt"],
    "text_to_speech": ["text"],
    "speech_to_text": ["audio"],
    "translation": ["text", "target_lang"],
    "summarization": ["input_text"],
    "text_classification": ["text"],
    "reranking": ["query", "contexts"],
    "run": ["prompt"],
}

ADMONITION_START = ":::info[Supported models]"


def _admonition(models_by_group: "Dict[str, List[str]]", note: str = "") -> str:
    """Each group renders as a collapsible <details> block so long model
    lists don't overwhelm the page."""
    lines = [ADMONITION_START, "", "Set `model_name` to one of the following models:", ""]
    for group, models in models_by_group.items():
        lines.append("<details>")
        lines.append(f"<summary>{group} ({len(models)} model{'s' if len(models) != 1 else ''})</summary>")
        lines.append("")
        for m in models:
            lines.append(f'<CopyableCode code="{m}" /><br />')
        lines.append("")
        lines.append("</details>")
        lines.append("")
    if note:
        lines.append(note)
        lines.append("")
    lines.append(":::")
    return "\n".join(lines)


def _select_sql(resource: str, columns: List[str], inputs: List[str]) -> str:
    lines = ["```sql", "SELECT"]
    lines.append(",\n".join(columns))
    lines.append(f"FROM cloudflare.ai.{resource}")
    lines.append("WHERE account_id = '{{ account_id }}' -- required")
    lines.append("AND model_name = '{{ model_name }}' -- required")
    for i in inputs:
        lines.append("AND " + i + " = '{{ " + i + " }}' -- model input")
    lines.append(";")
    lines.append("```")
    return "\n".join(lines)


def _patch_page(page: Path, resource: str, models_by_group: "Dict[str, List[str]]",
                columns: List[str], note: str = "") -> bool:
    text = page.read_text(encoding="utf-8")
    orig = text

    # 1. Supported-models admonition: replace existing block or insert
    # after the Overview table (before "## Fields").
    admon = _admonition(models_by_group, note)
    if ADMONITION_START in text:
        text = re.sub(
            re.escape(ADMONITION_START) + r".*?\n:::\n", admon + "\n",
            text, count=1, flags=re.DOTALL)
    else:
        anchor = "\n## Fields"
        if anchor not in text:
            logger.warning("%s: no '## Fields' anchor - skipping admonition", page)
        else:
            # <br /> gives the admonition breathing room below the
            # Overview table (docusaurus renders them flush otherwise)
            text = text.replace(anchor, "\n<br />\n\n" + admon + "\n" + anchor, 1)

    # 2. SELECT example rewrite (first sql block in the SELECT examples section).
    sec_m = re.search(r"## `SELECT` examples.*?(?=\n## |\Z)", text, re.DOTALL)
    if sec_m:
        section = sec_m.group(0)
        sql_m = re.search(r"```sql\n.*?```", section, re.DOTALL)
        if sql_m:
            new_section = section.replace(
                sql_m.group(0), _select_sql(resource, columns, EXAMPLE_INPUTS.get(resource, [])), 1)
            text = text.replace(section, new_section, 1)
    else:
        logger.warning("%s: no SELECT examples section", page)

    if text != orig:
        page.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(CONFIG_PATH))
    parser.add_argument("--docs-ai-dir", default=str(DOCS_AI_DIR))
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    families: Dict[str, dict] = config.get("families") or {}
    octet_models: List[str] = config.get("excluded_octet_input_models") or []
    docs_dir = Path(args.docs_ai_dir)
    if not docs_dir.exists():
        logger.error("ai docs dir not found: %s. Run `npm run generate-docs` first.", docs_dir)
        return 1

    patched = 0
    for fam, meta in families.items():
        page = docs_dir / fam / "index.md"
        if not page.exists():
            logger.warning("page missing: %s", page)
            continue
        mode = meta.get("mode") or "object"
        columns = list((meta.get("result_fields") or {}).keys()) if mode == "object" else ["contents"]
        if _patch_page(page, fam, {meta.get("title") or fam: sorted(meta.get("members") or [])}, columns):
            patched += 1
            logger.info("patched %s", fam)

    # Generic run page: all families' members grouped, plus a note about
    # the octet-input exec methods.
    run_page = docs_dir / "run" / "index.md"
    if run_page.exists():
        groups = {(meta.get("title") or fam): sorted(meta.get("members") or [])
                  for fam, meta in families.items()}
        note = ("The task-family resources above give these models typed result columns - "
                "prefer them over `run` where one exists. Binary-input models ("
                + ", ".join(f"`{m}`" for m in sorted(octet_models))
                + ") take a raw request body and are exposed as exec methods on this resource "
                "instead of SELECT.")
        if _patch_page(run_page, "run", groups,
                       ["response", "usage", "data", "shape", "text", "translated_text", "summary"],
                       note):
            patched += 1
            logger.info("patched run")
    else:
        logger.warning("run page missing: %s", run_page)

    logger.info("Patched %d ai doc pages.", patched)
    return 0


if __name__ == "__main__":
    sys.exit(main())
