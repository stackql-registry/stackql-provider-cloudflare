"""Post-process generated docusaurus markdown files to scrub MDX-hostile
content sourced from upstream Cloudflare API descriptions and parameter
names. Run automatically at the end of `npm run generate-docs`, but safe
to invoke standalone.

Issues handled:

  1. Angle brackets inside `<code>...</code>` blocks. Cloudflare API param
     names like `meta.<field>[<operator>]` look to MDX like opening JSX
     tags, which then break the `</code>` close.

  2. Tildes inside `<code>...</code>` blocks. Names like `issue_class~neq`
     trigger MDX strikethrough parsing.

     Both 1 and 2 are fixed by HTML-entity-escaping the offending chars
     INSIDE `<code>` only. Rendered output is identical because the chars
     are in a code block already.

  3. Stray `<br />` (and `<br>`, `</br>`) tags in description blobs.
     Cloudflare descriptions cram multi-paragraph text into a single
     line using `<br />`, but the downstream HTML5 minifier complains
     about the void-tag closing forms. We replace runs of `<br />`
     (any case / spacing variant) with two real newlines, turning the
     blob into proper markdown paragraphs.

  4. Cloudflare-relative links like `/api/resources/foo/methods/bar/`
     are absolute paths into the Cloudflare developer-docs site, not
     into our docusaurus site. Rewrite them to point at
     `https://developers.cloudflare.com/...` so they resolve.

  5. Same-page anchor links like `[text](#some-anchor)` that reference
     anchors copied from Cloudflare's docs (e.g. `#ip-access-rules-for-
     a-zone`) and don't exist on our site. We unwrap the link to its
     plain-text label so the docusaurus broken-link check stays happy.
     Exempt: `#methods`, `#parameter-*`, `#get*`, `#list*`, `#create*`,
     `#update*`, `#delete*`, `#replace*` and snake-case method-name
     anchors (e.g. `#get_by_account`) - these are anchors that the
     generated page actually emits.

Run via:
    python -m stackql_cloudflare_provider.sanitize_docs
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Tuple


logger = logging.getLogger(__name__)

PKG_DIR = Path(__file__).resolve().parent
WEBSITE_DOCS_DIR = PKG_DIR.parent / "website" / "docs"


# Match a <code>...</code> block (non-greedy, allowing newlines).
_CODE_BLOCK_RE = re.compile(r"<code>(.*?)</code>", re.DOTALL)

# Match the invalid `</br>` close tag (with optional whitespace).
# `<br>`, `<br/>`, and `<br />` are valid void / self-closing forms and we
# leave them alone - they render fine. Only the close-tag form is invalid
# for a void element and must be removed.
_BR_CLOSE_RE = re.compile(r"</\s*br\s*>", re.IGNORECASE)

# Markdown links pointing at Cloudflare-relative API paths.
# Captures: [text](/api/path) -> text only, with the path absolutised.
_CLOUDFLARE_API_LINK_RE = re.compile(r"\]\((/api/[^)\s]+)\)")

# Same-page anchor links. We unwrap any whose anchor isn't a known
# docusaurus-generated one.
_ANCHOR_LINK_RE = re.compile(r"\[([^\]]+)\]\(#([^)\s]+)\)")

# Anchors that the generator does emit on every per-resource page.
_KEEP_ANCHOR_PREFIXES = ("methods", "parameter-", "field-")
# Anchors that match a stackql method name template (e.g. `get_by_account`,
# `list_by_zone`, `create_by_account`, plus bare CRUD verbs).
_KEEP_ANCHOR_RE = re.compile(
    r"^(get|list|create|update|delete|replace|edit)(_by_[a-z_]+)?$"
)


def _keep_anchor(anchor: str) -> bool:
    a = anchor.lower()
    if a.startswith(_KEEP_ANCHOR_PREFIXES):
        return True
    if _KEEP_ANCHOR_RE.match(a):
        return True
    return False


# Non-OpenAPI type names that occasionally appear in upstream specs. We
# blank these out in the Datatype column so users don't see meaningless
# placeholders like "unknown". Real OpenAPI types are: string, number,
# integer, boolean, array, object, plus anything with format() like
# "string (date-time)".
_BOGUS_TYPE_RE = re.compile(
    r"<code>(?:unknown|any|null|none|undefined)</code>",
    re.IGNORECASE,
)


def _fix_bogus_types(text: str) -> Tuple[str, int]:
    """Replace `<code>unknown</code>` (and a few other non-OpenAPI type
    placeholders) with an empty `<code></code>` cell so the table doesn't
    surface noise."""
    if not _BOGUS_TYPE_RE.search(text):
        return text, 0
    new, n = _BOGUS_TYPE_RE.subn("<code></code>", text)
    return new, n


def _escape_code_inner(text: str) -> str:
    """Replace MDX-hostile characters with HTML entities.

    Inside a <code> block these render to the same glyph but no longer trip
    the MDX parser.
    """
    return (
        text
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("~", "&#126;")
    )


def _fix_code_blocks(text: str) -> Tuple[str, int]:
    """Escape MDX-hostile chars inside every <code>...</code> block."""
    n = 0

    def _sub(match: "re.Match[str]") -> str:
        nonlocal n
        inner = match.group(1)
        if "<" in inner or ">" in inner or "~" in inner:
            n += 1
            return f"<code>{_escape_code_inner(inner)}</code>"
        return match.group(0)

    return _CODE_BLOCK_RE.sub(_sub, text), n


def _fix_br_tags(text: str) -> Tuple[str, int]:
    """Strip invalid `</br>` close tags (void elements have no close tag).

    We do NOT touch self-closing `<br/>` or `<br />`: upstream Cloudflare
    descriptions use them inside table cells (`<td>...<br/><br/>...</td>`)
    where introducing a literal newline / blank line ends MDX's paragraph
    parsing mid-cell and breaks the table.
    """
    if not _BR_CLOSE_RE.search(text):
        return text, 0
    new, n = _BR_CLOSE_RE.subn("", text)
    return new, n


def _fix_cloudflare_api_links(text: str) -> Tuple[str, int]:
    """Rewrite `](/api/foo)` to `](https://developers.cloudflare.com/api/foo)`
    so the link resolves to the Cloudflare developer-docs site."""
    n = 0

    def _sub(match: "re.Match[str]") -> str:
        nonlocal n
        n += 1
        return f"](https://developers.cloudflare.com{match.group(1)})"

    return _CLOUDFLARE_API_LINK_RE.sub(_sub, text), n


def _fix_orphan_anchors(text: str) -> Tuple[str, int]:
    """Unwrap any `[label](#anchor)` whose anchor isn't a stackql-generated
    one. Keeps anchors we know exist (`#methods`, `#parameter-*`, method-
    name anchors, etc.)."""
    n = 0

    def _sub(match: "re.Match[str]") -> str:
        nonlocal n
        label, anchor = match.group(1), match.group(2)
        if _keep_anchor(anchor):
            return match.group(0)
        n += 1
        return label

    return _ANCHOR_LINK_RE.sub(_sub, text), n


def sanitize_file(path: Path) -> dict:
    """Rewrite `path` in-place if any sanitization was needed. Returns a
    per-file stats dict."""
    original = path.read_text(encoding="utf-8")
    text = original

    text, code_n = _fix_code_blocks(text)
    text, br_n = _fix_br_tags(text)
    text, link_n = _fix_cloudflare_api_links(text)
    text, anchor_n = _fix_orphan_anchors(text)
    text, type_n = _fix_bogus_types(text)

    if text != original:
        path.write_text(text, encoding="utf-8")
    return {"code": code_n, "br": br_n, "cf_link": link_n, "anchor": anchor_n, "bogus_type": type_n}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", default=str(WEBSITE_DOCS_DIR),
                        help=f"Docs root to scrub. Default: {WEBSITE_DOCS_DIR}")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    docs_dir = Path(args.docs_dir)
    if not docs_dir.exists():
        logger.error("Docs dir not found: %s", docs_dir)
        return 1

    files_touched = 0
    totals = {"code": 0, "br": 0, "cf_link": 0, "anchor": 0, "bogus_type": 0}
    for md in docs_dir.rglob("*.md"):
        stats = sanitize_file(md)
        if any(stats.values()):
            files_touched += 1
            for k, v in stats.items():
                totals[k] += v
            logger.debug("%s: %s", md.relative_to(docs_dir), stats)

    logger.info(
        "Sanitised %d files. Fixes: %d <code> blocks, %d <br> runs, %d cloudflare-api links, %d orphan anchors, %d bogus types.",
        files_touched, totals["code"], totals["br"], totals["cf_link"], totals["anchor"], totals["bogus_type"],
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
