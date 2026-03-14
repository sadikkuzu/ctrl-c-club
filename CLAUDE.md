# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal site automation for ctrl-c.club (~sadikkuzu). Scans user profile pages on the server, extracts social media links (Twitter, Instagram, Mastodon, GitHub), validates them, and generates an HTML page output to `~/public_html/socials.html` via cron.

## Commands

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run tests:**
```bash
pytest
pytest test_socials.py::test_ayikla       # single test
pytest test_socials.py::test_baloncuksort  # single test
```

**Lint / format (pre-commit hooks):**
```bash
pre-commit run --all-files --color always
```

**Update pinned dependencies:**
```bash
pip-compile -vU
```

## Architecture

All core logic lives in `socials.py`:

- `ayikla(adresler)` — filters a list of URLs by making live HTTP GET requests; drops unreachable ones
- `baloncuksort(liste, balon)` — bubble-sorts a specific username to the front of a list
- `olustur(liste)` — renders a list of `{url, username}` dicts into an HTML snippet
- `main()` — glues it all together: scans `/home/*/public_html/index.html` for social links via regex, validates, sorts, and prints the full HTML page to stdout

The four global lists (`twitter`, `instagram`, `mastodon`, `github`) accumulate `{url, username}` dicts during the scan. A `found` list deduplicates URLs across users.

**Cron schedule (documented in README):**
```
15,45   *       *       *       *   ~/code/socials.py > ~/public_html/socials.html
0,20,40 *       *       *       *   ~/code/codeupdate.sh > /dev/null 2>&1
```

**GitHub Actions:**
- `upgrader.yml` — daily pip-compile + pre-commit autoupdate on `dev`
- `update-dev-branch.yml` — merges `master` into `dev` on every master push

## Branch Model

- `master` — stable/production
- `dev` — active development; PRs target master
