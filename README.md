# Claude Code Starter

A clean starting point for working with Claude Code on a MacBook (Apple Silicon).

## Structure

```
claude-code-starter/
├── CLAUDE.md               Project instructions Claude Code reads every session
├── .claude/
│   ├── settings.json       Project permissions for Claude Code
│   └── commands/
│       └── review.md       Custom /review slash command
├── src/
│   └── main.py             Entry point
├── tests/
│   └── test_main.py        Tests (pytest)
├── docs/
│   └── NOTES.md            Working notes and decisions
├── requirements.txt
└── .gitignore
```

## Setup (macOS)

```bash
git clone https://github.com/mnaseeresga-cyber/claude-code-starter.git
cd claude-code-starter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
pytest
```

## Use with Claude Code

1. Open the Claude app and click the **Code** tab.
2. Select the `claude-code-starter` folder.
3. Try: `Explain this project`, `Add a function that ...`, or `/review`.

Claude Code reads `CLAUDE.md` at the start of every session, so keep project rules and conventions there.
