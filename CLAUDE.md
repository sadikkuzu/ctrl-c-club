# CLAUDE.md

Guidance for Claude Code (claude.ai/code) in this repo.

## Project Overview

Personal site automation for ctrl-c.club (~sadikkuzu). Scans user profile pages, extracts social links (Twitter, X, Instagram, GitHub), validates, generates HTML → `~/public_html/socials.html` via cron.

## Commands

**Install dependencies:**
```bash
uv sync                              # local dev (creates .venv from uv.lock)
pip install -r requirements.txt      # server fallback (no uv on ctrl-c.club)
```

**Run tests:**
```bash
uv run pytest
uv run pytest test_socials.py::test_ayikla       # single test
uv run pytest test_socials.py::test_baloncuksort  # single test
```
Tests hit live twitter.com — require network.

Python 3.10+ (CI pins 3.10; pyupgrade uses --py310-plus).

**Lint / format (pre-commit hooks):**
```bash
pre-commit run --all-files --color always
```

**Update pinned dependencies:**
```bash
uv lock --upgrade
uv export --no-hashes --no-emit-project -o requirements.txt
```
`uv.lock` is the source of truth; `requirements.txt` is an export kept for pip-only installs on the server. Upgrade a single package with `uv lock --upgrade-package <name>`.

## Architecture

All core logic in `socials.py`:

- `ayikla(adresler)` — filters URL list via live HTTP GET; drops unreachable
- `baloncuksort(liste, balon)` — bubble-sorts username to front of list
- `olustur(liste)` — renders `{url, username}` dicts into HTML snippet
- `main()` — scans `/home/*/public_html/index.html` for social links via regex, validates, sorts, prints full HTML page to stdout

Four global lists (`twitter`, `x`, `instagram`, `github`) accumulate `{url, username}` dicts. `found` list deduplicates URLs across users.

**Cron schedule (documented in README):**
```
15,45   *       *       *       *   ~/code/socials.py > ~/public_html/socials.html
0,20,40 *       *       *       *   ~/code/codeupdate.sh > /dev/null 2>&1
```

**GitHub Actions:**
- `upgrader.yml` — daily `uv lock --upgrade` + requirements.txt re-export + pre-commit autoupdate on `dev`
- `update-dev-branch.yml` — merges `master` into `dev` on every master push

## Branch Model

- `master` — stable/production
- `dev` — active development; PRs target master
