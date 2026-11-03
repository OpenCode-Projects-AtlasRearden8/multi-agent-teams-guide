#!/usr/bin/env python3
"""Build the static HTML site/ from the Markdown docs/.

Standard library only. Supports a deliberate subset of Markdown:
headings (#..####), paragraphs, - bullets, 1. numbered lists,
> blockquotes, ``` fenced code, pipe tables, standalone images,
and inline **bold**, *em*, `code`, [links](targets). Everything
else is passed through escaped. Deterministic, offline, no CDNs.

Usage: python3 tools/build_site.py
"""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
MANIFEST = DOCS / "MANIFEST.json"

STYLE = """\
:root {
  --bg: #fbf7f0; --paper: #ffffff; --ink: #3a3a3a; --soft: #6b5d4f;
  --teal: #2a7f8f; --rust: #b58a4a; --violet: #5c6bb0; --line: #e4dccb;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  font-family: "Trebuchet MS", Verdana, system-ui, sans-serif;
  line-height: 1.65; font-size: 17px;
}
header.site {
  background: #f2e9da; border-bottom: 3px solid #d8c7a8; padding: 1rem 1.25rem 0.6rem;
}
.site-title { font-size: 1.35rem; font-weight: bold; color: var(--soft); text-decoration: none; }
.site-title span { color: var(--teal); }
nav.menu { margin-top: 0.6rem; display: flex; flex-wrap: wrap; gap: 0.25rem 0.9rem; font-size: 0.85rem; }
nav.menu a { color: var(--soft); text-decoration: none; padding: 0.12rem 0.4rem; border-radius: 6px; }
nav.menu a:hover { background: #e8dcc3; }
nav.menu a.current { background: var(--teal); color: #fff; }
main { max-width: 820px; margin: 0 auto; padding: 1.5rem 1.25rem 3rem; background: var(--paper); min-height: 55vh; border-left: 1px solid var(--line); border-right: 1px solid var(--line); }
h1 { font-size: 1.9rem; color: var(--soft); margin: 0.2em 0 0.4em; }
h2 { color: #1f5f6a; margin-top: 2.1em; border-bottom: 2px solid var(--line); padding-bottom: 0.15em; }
h3 { color: var(--rust); }
a { color: #1f6ab0; }
code { background: #f3ede0; padding: 0.08em 0.35em; border-radius: 5px; font-size: 0.9em; }
pre { background: #2f2a24; color: #f3ede0; padding: 1rem; border-radius: 10px; overflow-x: auto; line-height: 1.5; }
pre code { background: none; color: inherit; padding: 0; font-size: 0.85rem; }
blockquote { background: #fdf6e3; border-left: 5px solid var(--rust); margin: 1rem 0; padding: 0.5rem 1rem; border-radius: 0 8px 8px 0; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.92em; }
th, td { border: 1px solid var(--line); padding: 0.45rem 0.6rem; text-align: left; }
th { background: #f2e9da; color: var(--soft); }
figure { margin: 1.5rem 0; text-align: center; }
figure img { max-width: 100%; height: auto; border: 1px solid var(--line); border-radius: 10px; background: #fff; }
figcaption { font-size: 0.82rem; color: var(--soft); margin-top: 0.4rem; }
.disclaimer { background: #fdf3d7; border: 1px dashed var(--rust); border-radius: 10px; padding: 0.6rem 1rem; font-size: 0.85rem; color: var(--soft); }
footer.site { text-align: center; color: var(--soft); font-size: 0.8rem; padding: 1.5rem 1rem 2.5rem; }
.nav-arrows { display: flex; justify-content: space-between; margin-top: 2.5rem; padding-top: 1rem; border-top: 2px solid var(--line); font-size: 0.9rem; }
.onpage { font-size: 0.8rem; color: var(--soft); background: #f6f0e3; border-radius: 8px; padding: 0.55rem 0.9rem; }
.onpage strong { color: #1f5f6a; }
"""


def esc(text: str) -> str:
    return escape(text, quote=False)


def slugify(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text)
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s) or "section"


def inline(text: str) -> str:
    """Inline formatting on an already escaped string."""
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def table_html(rows):
    if len(rows) < 2:
        return ""
    header = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    out = ["<table>", "<thead>", "<tr>"]
    out += [f"<th>{inline(esc(c))}</th>" for c in header]
    out += ["</tr>", "</thead>", "<tbody>"]
    for row in rows[2:]:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        cells += [""] * (len(header) - len(cells))
        out.append("<tr>")
        out += [f"<td>{inline(esc(c))}</td>" for c in cells[: len(header)]]
        out.append("</tr>")
    out += ["</tbody>", "</table>"]
    return "\n".join(out)


def md_to_html(md_text: str) -> str:
    lines = md_text.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level, text, anchor = len(m.group(1)), m.group(2), None
            html_text = inline(esc(text.strip()))
            if level == 2:
                anchor = slugify(text)
                out.append(f'<h2 id="{anchor}">{html_text}</h2>')
            else:
                out.append(f"<h{level}>{html_text}</h{level}>")
            i += 1
            continue

        if line.strip() == "---":
            out.append("<hr>")
            i += 1
            continue

        if line.lstrip().startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:-]+\|", lines[i + 1]):
            block = []
            while i < n and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            out.append(table_html(block))
            continue

        if line.lstrip().startswith("```"):
            at = line.lstrip().index("`") + 3
            lang = line.strip()[at:].strip()
            code = []
            i += 1
            while i < n and not lines[i].lstrip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            cls = f' class="language-{esc(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{esc(chr(10).join(code))}</code></pre>")
            continue

        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", line.strip())
        if m:
            src = esc(m.group(2).strip())
            out.append(
                f'<figure><img src="{src}" alt="{esc(m.group(1))}" loading="lazy">'
                f"<figcaption>{inline(esc(m.group(1)))}</figcaption></figure>"
            )
            i += 1
            continue

        if line.lstrip().startswith("> "):
            quote = []
            while i < n and lines[i].lstrip().startswith("> "):
                quote.append(lines[i].lstrip()[2:].strip())
                i += 1
            body = "</p>\n<p>".join(inline(esc(p)) for p in quote if p)
            out.append(f"<blockquote><p>{body}</p></blockquote>")
            continue

        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]).strip())
                i += 1
            out.append("<ul>")
            for it in items:
                out.append(f"<li>{inline(esc(it))}</li>")
            out.append("</ul>")
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip())
                i += 1
            out.append("<ol>")
            for it in items:
                out.append(f"<li>{inline(esc(it))}</li>")
            out.append("</ol>")
            continue

        para = []
        while i < n and lines[i].strip() and not re.match(
            r"^(#{1,4}\s|\s*[-*]\s|\s*\d+\.\s|> |```|\||---\s*$)", lines[i]
        ):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(esc(' '.join(para)))}</p>")

    return "\n".join(out)


def page_html(page, pages, body, index):
    nav = []
    for n, p in enumerate(pages):
        cls = "current" if p["slug"] == page["slug"] else ""
        nav.append(f'<a href="{p["slug"]}.html" class="{cls}">{p["title"]}</a>')
    nav_html = "\n    ".join(nav)

    sections = ""
    hs = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', body)
    if hs:
        items = "".join(f'<a href="#{h[0]}">{h[1]}</a>' for h in hs)
        sep = ""
        toc_items = []
        for hid, title in hs:
            toc_items.append(f'<a href="#{hid}">{title}</a>')
        sections = f'<p class="onpage"><strong>On this page:</strong> ' + " - ".join(toc_items) + "</p>"

    prev, nxt = None, None
    if index > 0:
        prev = pages[index - 1]
    if index + 1 < len(pages):
        nxt = pages[index + 1]
    arrows = []
    arrows.append(
        f'<a href="{prev["slug"]}.html">{chr(8592)} {prev["title"]}</a>'
        if prev
        else "<span></span>"
    )
    arrows.append(
        f'<a href="{nxt["slug"]}.html">{nxt["title"]} {chr(8594)}</a>'
        if nxt
        else "<span></span>"
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page['title']} - The Multi-Agent Teams Guide</title>
<meta name="description" content="A plain-English manual on running several AI agents together like a tiny staff. Education only, no code required.">
<style>
{STYLE}
</style>
</head>
<body>
<header class="site">
  <a class="site-title" href="index.html">The Multi-Agent <span>Teams</span> Guide</a>
  <nav class="menu">
    {nav_html}
  </nav>
</header>
<main>
{sections}
{body}
<div class="nav-arrows">
  {arrows[0]}
  {arrows[1]}
</div>
</main>
<footer class="site">
  <p>The Multi-Agent Teams Guide - plain-English orchestration basics, complements the Agents-and-MCP Handbook.</p>
  <p>Educational only - not medical, legal, tax, or financial advice. MIT licensed.</p>
  <p>Copyright (c) 2026 Asdale Dynamics, LLC</p>
</footer>
</body>
</html>
"""


def index_page(pages):
    cards = [f'<li><a href="{p["slug"]}.html">{p["title"]}</a></li>' for p in pages]
    hero_md = (
        "# The Multi-Agent Teams Guide\n\n"
        "Plain-English manual on running several AI agents together like a tiny staff. "
        "When a team beats one agent, assigning roles and handoffs, shared-file "
        "conventions, spotting confusion loops, and three worked home/small-business "
        "projects. No code required.\n\n"
        "## Read it page by page\n\n"
    )
    lead = md_to_html(hero_md)
    menu = (
        f'<ul class="toc">\n    ' + "\n    ".join(cards) + "\n  </ul>\n"
        '<p class="disclaimer">Educational only - not medical, legal, tax, or financial '
        "advice. Complements the Agents-and-MCP Handbook (single agents and MCP). "
        "Use fictional stand-ins; no secrets or personal data, ever.</p>"
    )
    pseudo = {"slug": "index", "title": "Home"}
    return page_html(pseudo, pages, lead + menu, 0)


def build():
    pages = json.loads(MANIFEST.read_text())["pages"]
    SITE.mkdir(exist_ok=True)
    diagrams_dir = SITE / "diagrams"
    diagrams_dir.mkdir(exist_ok=True)
    import shutil

    for d in sorted((DOCS / "diagrams").glob("*.svg")):
        shutil.copy(d, diagrams_dir / d.name)

    for index, page in enumerate(pages):
        md_text = (DOCS / page["file"]).read_text()
        body = md_to_html(md_text)
        out = SITE / f'{page["slug"]}.html'
        out.write_text(page_html(page, pages, body, index))

    hero = index_page(pages)
    (SITE / "index.html").write_text(hero)
    print(f"built {len(pages) + 1} pages into site/")


if __name__ == "__main__":
    build()
