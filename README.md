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

## Three-statement model

`src/three_statement.py` projects a linked income statement, balance sheet and cash flow statement for 5 years.

```bash
python src/three_statement.py      # prints the model and saves three_statement_model.csv
```

- Drivers live in `Assumptions` (growth, margins, DSO/DIO/DPO, capex, tax, debt, dividends, minimum cash).
- Opening position lives in `OpeningBalanceSheet`; the model rejects an unbalanced opening.
- Interest is on opening balances, so there are no circular references.
- A revolver draws automatically to hold minimum cash and repays from excess cash.
- Tests check that the balance sheet balances, cash ties to the cash flow statement, and equity rolls forward.

## Use with Claude Code

1. Open the Claude app and click the **Code** tab.
2. Select the `claude-code-starter` folder.
3. Try: `Explain this project`, `Add a function that ...`, or `/review`.

Claude Code reads `CLAUDE.md` at the start of every session, so keep project rules and conventions there.
