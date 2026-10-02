# Project instructions for Claude Code

## Owner
Muhammad Naseer (OSPA). Finance, audit and AI workflow background.

## Working style
- Be direct. Deliver output once a decision is made.
- Make targeted changes only; do not rewrite untouched code.
- Do not use em-dash characters in generated docs or comments.
- Prefer specific figures and evidence over general commentary.

## Code conventions
- Python 3.11+.
- Source in `src/`, tests in `tests/` (pytest).
- Every new function gets a docstring and at least one test.
- Run `pytest` before declaring a task done.

## Accounting context (when relevant)
- Primary framework: U.S. GAAP (ASC 810, ASC 606).
- Note IFRS only where cross-border obligations apply.

## Commands
- Setup: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Run: `python src/main.py`
- Test: `pytest`
