# STATUS

Last updated: 2026-11-03

## What was built

**The Multi-Agent Teams Guide** — a plain-English, education-only manual on running several AI agents together like a tiny staff (orchestration basics; method, not code). Complements the planned/companion *Agents-and-MCP Handbook* (single agents + MCP).

- `docs/` — 9 Markdown chapters with 5 hand-made SVG diagrams:
  1. About This Guide
  2. When a Team Beats One Agent (fifteen-second team test, four failure patterns)
  3. Roles and Handoffs (Planner/Workers/Checker, one-writer-per-file, Done–Next–Watch-out memos, kickoff)
  4. Shared-File Conventions (folder floor plan, naming habits, status lines, event log, decision log)
  5. Spotting Confusion Loops (symptoms, four causes, five-stage bail-out, prevention, kill-switch habit)
  6. Project A — eBay Listing Team (5 guitar pedals; role cards, fact sheets, claim maps, bounce/approve memos)
  7. Project B — Book-Launch Team (fictional book "Calm Money"; banned-claims list, two narrow checkers: claims + tone)
  8. Project C — Household Paperwork Team (weekly 15-minute ritual, ADHD-friendly energy rule, practice-documents-only sensitive-data rule)
  9. Free Tools and Next Steps (free toolbox, 5-level upgrade path, walk-away list)
- `docs/diagrams/` — team-vs-single.svg, roles-handoffs.svg, shared-files.svg, confusion-loop.svg, project-pipeline.svg
- `site/` — static HTML version of the whole manual (10 pages incl. index), no JavaScript, no network calls, warm style consistent with Asdale Dynamics' "like a friend would" voice
- `tools/build_site.py` — stdlib-only deterministic Markdown-subset → HTML site builder
- `tests/run_checks.py` — full verification suite
- `README.md` (credits Asdale Dynamics, LLC), `LICENSE` (MIT, exact line "Copyright (c) 2026 Asdale Dynamics, LLC")

## How to run it

- Read the book: open `docs/00-about-this-guide.md`, or open `site/index.html` in any browser.
- Rebuild the site: `python3 tools/build_site.py` (idempotent; requires no third-party packages).
- Run verification: `python3 tests/run_checks.py` (exit 0 on success).

## Verification results

- `python3 tests/run_checks.py` → **All checks passed** (~190 checks). Includes:
  - every doc exists, starts with an H1, and every relative link target resolves
  - all 5 SVGs parse as XML and have `<title>`/`<desc>`
  - site rebuild is byte-for-byte deterministic
  - every manifest page has a built site page; all HTML href/src targets resolve; every `#anchor` referenced is defined in its page
  - each page has `<title>`, nav menu, LLC credit, education note; no literal `**` or unresolved ``` remnants leak into HTML
  - required content present (team test, handoff memos, one-writer-per-file, bail-out, disclaimer, no-secrets rule, companion-book mention); each project page has roster, kickoff, education note, and balanced sample fences
  - LICENSE contains the exact copyright line; README credits Asdale Dynamics, LLC
  - secrets scan over all text files (AWS/OpenAI/GitHub tokens, api_key/password patterns): clean
  - `tools/` and `tests/` are stdlib-only (verified against `sys.stdlib_module_names`)
- Worked-project examples were dry-run end-to-end while writing: memo chains (researcher → writer → checker → boss) are internally consistent (file names, claim maps, bounce reasons, log lines all agree across steps).

## Known gaps

- Diagrams are hand-authored SVG (no diagram toolchain); they are valid and titled but visually plain.
- The `site/` HTML uses one inline stylesheet per page (duplicate bytes); acceptable for a small static book, trivially refactored later into a shared `.css` file if size ever matters.
- The builder supports a deliberate Markdown subset (no nested emphasis, no multi-level lists); docs are written to conform, and checks catch regressions.
- No print/PDF export and no search UI. The method is tool-agnostic prose; screenshots of specific agent products were deliberately avoided to keep the guide version-proof.
- Projects are fictional dry-runs (by design — no personal data, no real listings/payments); they have not been executed against live marketplaces or publishing platforms.
