# The Multi-Agent Teams Guide

A plain-English manual on running several AI agents together like a tiny staff — when a team beats one agent, assigning roles and handoffs, shared-file conventions, spotting confusion loops, and three worked home/small-business projects. Written for absolute beginners, explained like a friend would, and **no code required** to use the method.

> Education only: this guide is general AI education, not medical, legal, tax, or financial advice. All examples are fictional. No secrets, API keys, or personal data — use fictional stand-ins everywhere real life appears.

## What's inside

- `docs/` — the full Markdown manual, page by page:
  - **01** When a team beats one agent (the fifteen-second team test)
  - **02** Roles and handoffs (Planner / Workers / Checker, the Done–Next–Watch-out memo)
  - **03** Shared-file conventions (the folder floor plan, one writer per file, status lines)
  - **04** Spotting confusion loops (the five-stage bail-out)
  - **05–07** Three worked projects: eBay listing team, book-launch team, household paperwork team
  - **08** Free tools and next steps
- `docs/diagrams/` — five hand-made SVG diagrams (also copied into the site)
- `site/` — a dependency-free static HTML version of the whole manual
- `tools/build_site.py` — stdlib-only builder that converts `docs/` into `site/`
- `tests/run_checks.py` — verification suite (docs integrity, links, SVGs, build determinism, HTML checks, secrets scan)

## How to read it

Open `docs/00-about-this-guide.md` and read in numbered order, or start a project straight from the projects pages. Prefer a website? Open `site/index.html` in any browser — everything is local, no JavaScript, no network calls.

## How to rebuild and verify

```bash
python3 tools/build_site.py      # rebuild site/ from docs/ (idempotent)
python3 tests/run_checks.py      # run all verification checks
```

Both commands use only the Python standard library (tested with Python 3.13).

## Who made this

By **Asdale Dynamics, LLC** — beginner-friendly AI education in the plain, warm style of Dylan Asdale's *The Massive AI Manual*. Pair it with the companion *Agents-and-MCP Handbook* for single-agent and MCP setup.

## License

MIT — see `LICENSE`. Copyright (c) 2026 Asdale Dynamics, LLC.
