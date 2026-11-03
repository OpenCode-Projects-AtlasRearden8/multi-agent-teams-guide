#!/usr/bin/env python3
"""Verification checks for the Multi-Agent Teams Guide.

Run with:  python3 tests/run_checks.py
Exit code 0 = all checks passed. Standard library only.

Checks: docs integrity, markdown links, SVG validity, deterministic
site build, HTML links/anchors, required content, license/readme
lines, and a secrets scan.
"""
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fails = []


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" - {detail}" if detail and not ok else ""))
    if not ok:
        fails.append(f"{name}: {detail}")


def main():
    docs = ROOT / "docs"
    site = ROOT / "site"
    manifest = json.loads((docs / "MANIFEST.json").read_text())
    pages = manifest["pages"]

    # 1. Docs exist and start with an H1
    for p in pages:
        f = docs / p["file"]
        check(f"doc exists: {p['file']}", f.exists())
        if f.exists():
            first = f.read_text().lstrip().splitlines()[0]
            check(f"doc starts with H1: {p['file']}", first.startswith("# "))

    # 2. Every relative target referenced from docs exists (images, links)
    for p in pages:
        text = (docs / p["file"]).read_text()
        for m in re.finditer(r"\]\(([^)#\s]+)", text):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                continue
            check(f"link target in docs: {p['file']} -> {target}",
                  (docs / target).exists())

    # 3. Diagrams are valid XML with title+desc
    diagrams = list((docs / "diagrams").glob("*.svg"))
    check("diagram count", len(diagrams) == len(manifest["diagrams"]),
          f"found {len(diagrams)}")
    for svg in diagrams:
        ok = True
        try:
            ET.parse(svg)
            text = svg.read_text()
            ok = "<title" in text and "<desc" in text
        except ET.ParseError as e:
            ok = False
            check(f"svg parses: {svg.name}", False, str(e))
            continue
        check(f"svg valid with title/desc: {svg.name}", ok)

    # 4. Build is deterministic (rebuild, compare hashes)
    before = {
        f.name: hashlib.sha256(f.read_bytes()).hexdigest()
        for f in sorted(site.rglob("*")) if f.is_file()
    }
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_site.py")],
                   check=True, capture_output=True)
    after = {
        f.name: hashlib.sha256(f.read_bytes()).hexdigest()
        for f in sorted(site.rglob("*")) if f.is_file()
    }
    check("site build is deterministic", before == after,
          str(set(before) ^ set(after)))

    # 5. Every manifest page has a site page; index exists
    for p in pages:
        check(f"site page built: {p['slug']}.html",
              (site / f"{p['slug']}.html").exists())
    check("site index.html exists", (site / "index.html").exists())
    copied = {f.name for f in (site / "diagrams").glob("*.svg")}
    check("diagrams copied to site",
          copied == {d.name for d in diagrams}, f"site has {copied}")

    # 6. Parse each HTML; collect links; verify targets
    class LinkCollector(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.links, self.imgs, self.text, self.ids = [], [], "", set()
            self._in_body, self._in_link = False, False

        def handle_starttag(self, tag, attrs):
            a = dict(attrs)
            if tag in ("a", "img"):
                target = a.get("href") or a.get("src")
                if target:
                    (self.links if tag == "a" else self.imgs).append(target)
            if tag == "body":
                self._in_body = True
            if a.get("id"):
                self.ids.add(a["id"])

        def handle_endtag(self, tag):
            if tag == "body":
                self._in_body = False

        def handle_data(self, data):
            if self._in_body:
                self.text += data

    for p in pages:
        slug = p["slug"]
        path = site / f"{slug}.html"
        raw = path.read_text()
        parser = LinkCollector()
        parser.feed(raw)
        check(f"html has title: {slug}.html", "<title>" in raw)
        check(f"html has nav menu: {slug}.html", 'class="menu"' in raw)
        check(f"html credits LLC: {slug}.html", "Asdale Dynamics, LLC" in raw)
        check(f"html education note: {slug}.html",
              "Education" in parser.text or "education" in parser.text)
        check(f"no literal ** left: {slug}.html", "**" not in parser.text)
        check(f"no unresolved fences: {slug}.html", "```" not in parser.text)
        for target in parser.links + parser.imgs:
            if target.startswith(("#", "http")):
                pass
            elif target.startswith("#"):
                pass
            else:
                check(f"html target resolves: {slug}.html -> {target}",
                      (site / target).exists())
        # internal anchors defined on this page
        for m in re.finditer(r'href="#([^"]+)"', raw):
            check(f"anchor defined in {slug}.html: #{m.group(1)}",
                  m.group(1) in parser.ids)

    # nav links point back at least to index
    idx_raw = (site / "index.html").read_text()
    check("index links first page and last page",
          "about.html" in idx_raw and "free-tools-and-next-steps.html" in idx_raw)

    # 7. Required content in the manual
    combined = " ".join((docs / p["file"]).read_text() for p in pages)
    expected = {
        "single vs team chapter": "fifteen-second team test",
        "roles chapter": "handoff memo",
        "files chapter": "one writer per file",
        "loops chapter": "five-stage bail-out",
        "disclaimer somewhere": "not medical, legal, tax, or financial advice",
        "no-secrets rule": "No secrets",
        "companion book mention": "Agents-and-MCP Handbook",
    }
    for name, needle in expected.items():
        check(f"manual contains {name}", needle.lower() in combined.lower())

    for p in pages:
        if "project-" in p["file"]:
            text = (docs / p["file"]).read_text()
            for needle in ("kickoff.md", "the roster", "Education note"):
                check(f"{p['file']} contains {needle}",
                      needle.lower() in text.lower())
            check(f"{p['file']} has >=2 sample fences",
                  text.count("```") >= 4 and text.count("```") % 2 == 0)

    # 8. LICENSE and README
    lic = ROOT / "LICENSE"
    check("LICENSE exists", lic.exists())
    if lic.exists():
        check("LICENSE exact copyright line",
              "Copyright (c) 2026 Asdale Dynamics, LLC" in lic.read_text())
    readme = ROOT / "README.md"
    check("README exists", readme.exists())
    if readme.exists():
        check("README credits Asdale Dynamics, LLC",
              "Asdale Dynamics, LLC" in readme.read_text())

    # 9. Secrets scan (only high-signal patterns)
    secret_patterns = [
        (r"AKIA[0-9A-Z]{16}", "AWS key"),
        (r"sk-[A-Za-z0-9]{16,}", "OpenAI-style key"),
        (r"ghp_[A-Za-z0-9]{20,}", "GitHub token"),
        (r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{12,}", "embedded api key"),
        (r"(?i)password\s*[:=]\s*['\"][^'\"]{6,}", "embedded password"),
    ]
    scan_files = [f for f in ROOT.rglob("*")
                  if f.is_file() and ".git" not in f.parts
                  and f.suffix in {".md", ".html", ".py", ".json", ".svg", ".css", ".txt"}]
    clean = True
    for f in scan_files:
        text = f.read_text(errors="ignore")
        for pat, label in secret_patterns:
            if re.search(pat, text):
                clean = False
                check(f"no secrets: {f.relative_to(ROOT)} ({label})", False)
    if clean:
        check("no secrets found in repository files", True, f"({len(scan_files)} files scanned)")

    # 10. Tools sanity: no third-party imports in tools/ or tests/
    for f in list((ROOT / "tools").glob("*.py")) + list((ROOT / "tests").glob("*.py")):
        src = f.read_text()
        imports = re.findall(r"^import\s+(\w+)", src, re.M) + \
                  re.findall(r"^from\s+([\w.]+)\s+import", src, re.M)
        stdlib_ok = all(m.split(".")[0] in sys.stdlib_module_names for m in imports)
        check(f"stdlib-only: {f.name}", stdlib_ok, str(imports))

    print()
    if fails:
        print(f"{len(fails)} check(s) FAILED")
        for f in fails:
            print(" -", f)
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
