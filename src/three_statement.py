"""Linked three-statement financial model (income statement, balance sheet, cash flow).

Annual projection. Interest is calculated on opening balances, so the model has
no circular references. A revolving credit facility draws automatically to keep
cash at the minimum balance and repays from excess cash. Equity is shown as a
single line (paid-in capital plus retained earnings).
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path

DAYS = 365


@dataclass
class OpeningBalanceSheet:
    """Balance sheet at the start of the first projection year."""

    cash: float = 500.0
    accounts_receivable: float = 800.0
    inventory: float = 600.0
    ppe_net: float = 3_000.0
    accounts_payable: float = 400.0
    revolver: float = 0.0
    term_debt: float = 2_000.0
    equity: float = 2_500.0

    def check(self) -> float:
        """Return assets minus liabilities and equity (0 when balanced)."""
        assets = self.cash + self.accounts_receivable + self.inventory + self.ppe_net
        liab_eq = self.accounts_payable + self.revolver + self.term_debt + self.equity
        return assets - liab_eq


@dataclass
class Assumptions:
    """Operating and financing drivers. Rates are decimals (0.10 = 10%)."""

    base_revenue: float = 10_000.0
    revenue_growth: list[float] = field(default_factory=lambda: [0.10, 0.10, 0.08, 0.07, 0.06])
    gross_margin: float = 0.40
    opex_pct_revenue: float = 0.20
    capex_pct_revenue: float = 0.05
    depreciation_pct_opening_ppe: float = 0.10
    tax_rate: float = 0.21
    dso: float = 30.0
    dio: float = 45.0
    dpo: float = 30.0
    term_debt_rate: float = 0.07
    revolver_rate: float = 0.08
    cash_interest_rate: float = 0.02
    term_debt_repayment: float = 200.0
    dividend_payout: float = 0.20
    minimum_cash: float = 250.0

    @property
    def years(self) -> int:
        """Number of projection years."""
        return len(self.revenue_growth)


def build_model(assumptions: Assumptions, opening: OpeningBalanceSheet) -> list[dict[str, float]]:
    """Project the three statements and return one dict of line items per year."""
    if abs(opening.check()) > 0.01:
        raise ValueError(f"Opening balance sheet does not balance (difference {opening.check():,.2f})")

    a = assumptions
    prev = {
        "cash": opening.cash,
        "accounts_receivable": opening.accounts_receivable,
        "inventory": opening.inventory,
        "ppe_net": opening.ppe_net,
        "accounts_payable": opening.accounts_payable,
        "revolver": opening.revolver,
        "term_debt": opening.term_debt,
        "equity": opening.equity,
    }
    revenue_prev = a.base_revenue
    years: list[dict[str, float]] = []

    for i, growth in enumerate(a.revenue_growth, start=1):
        y: dict[str, float] = {"year": i}

        # Income statement
        y["revenue"] = revenue_prev * (1 + growth)
        y["cogs"] = y["revenue"] * (1 - a.gross_margin)
        y["gross_profit"] = y["revenue"] - y["cogs"]
        y["opex"] = y["revenue"] * a.opex_pct_revenue
        y["ebitda"] = y["gross_profit"] - y["opex"]
        y["depreciation"] = prev["ppe_net"] * a.depreciation_pct_opening_ppe
        y["ebit"] = y["ebitda"] - y["depreciation"]
        y["interest_expense"] = prev["term_debt"] * a.term_debt_rate + prev["revolver"] * a.revolver_rate
        y["interest_income"] = max(prev["cash"], 0.0) * a.cash_interest_rate
        y["pre_tax_income"] = y["ebit"] - y["interest_expense"] + y["interest_income"]
        y["tax"] = max(y["pre_tax_income"], 0.0) * a.tax_rate
        y["net_income"] = y["pre_tax_income"] - y["tax"]

        # Working capital and fixed assets
        y["accounts_receivable"] = y["revenue"] * a.dso / DAYS
        y["inventory"] = y["cogs"] * a.dio / DAYS
        y["accounts_payable"] = y["cogs"] * a.dpo / DAYS
        y["capex"] = y["revenue"] * a.capex_pct_revenue
        y["ppe_net"] = prev["ppe_net"] + y["capex"] - y["depreciation"]

        # Cash flow statement
        y["change_ar"] = prev["accounts_receivable"] - y["accounts_receivable"]
        y["change_inventory"] = prev["inventory"] - y["inventory"]
        y["change_ap"] = y["accounts_payable"] - prev["accounts_payable"]
        y["cfo"] = (
            y["net_income"] + y["depreciation"] + y["change_ar"] + y["change_inventory"] + y["change_ap"]
        )
        y["cfi"] = -y["capex"]
        y["term_debt_repaid"] = min(a.term_debt_repayment, prev["term_debt"])
        y["dividends"] = max(y["net_income"], 0.0) * a.dividend_payout

        pre_revolver_cash = prev["cash"] + y["cfo"] + y["cfi"] - y["term_debt_repaid"] - y["dividends"]
        if pre_revolver_cash < a.minimum_cash:
            revolver_flow = a.minimum_cash - pre_revolver_cash
        else:
            revolver_flow = -min(prev["revolver"], pre_revolver_cash - a.minimum_cash)
        y["revolver_draw_repay"] = revolver_flow
        y["cff"] = revolver_flow - y["term_debt_repaid"] - y["dividends"]
        y["net_change_cash"] = y["cfo"] + y["cfi"] + y["cff"]

        # Balance sheet
        y["cash"] = prev["cash"] + y["net_change_cash"]
        y["revolver"] = prev["revolver"] + revolver_flow
        y["term_debt"] = prev["term_debt"] - y["term_debt_repaid"]
        y["equity"] = prev["equity"] + y["net_income"] - y["dividends"]
        y["total_assets"] = y["cash"] + y["accounts_receivable"] + y["inventory"] + y["ppe_net"]
        y["total_liabilities_equity"] = (
            y["accounts_payable"] + y["revolver"] + y["term_debt"] + y["equity"]
        )
        y["balance_check"] = y["total_assets"] - y["total_liabilities_equity"]

        years.append(y)
        prev = {k: y[k] for k in prev}
        revenue_prev = y["revenue"]

    return years


SECTIONS = {
    "INCOME STATEMENT": [
        "revenue", "cogs", "gross_profit", "opex", "ebitda", "depreciation", "ebit",
        "interest_expense", "interest_income", "pre_tax_income", "tax", "net_income",
    ],
    "BALANCE SHEET": [
        "cash", "accounts_receivable", "inventory", "ppe_net", "total_assets",
        "accounts_payable", "revolver", "term_debt", "equity", "total_liabilities_equity",
        "balance_check",
    ],
    "CASH FLOW STATEMENT": [
        "net_income", "depreciation", "change_ar", "change_inventory", "change_ap", "cfo",
        "capex", "cfi", "revolver_draw_repay", "term_debt_repaid", "dividends", "cff",
        "net_change_cash",
    ],
}


LABELS = {
    "cogs": "Cost of Goods Sold",
    "opex": "Operating Expenses",
    "ebitda": "EBITDA",
    "ebit": "EBIT",
    "ppe_net": "PP&E, Net",
    "total_liabilities_equity": "Total Liabilities & Equity",
    "change_ar": "(Increase) in Receivables",
    "change_inventory": "(Increase) in Inventory",
    "change_ap": "Increase in Payables",
    "cfo": "Cash from Operations",
    "cfi": "Cash from Investing",
    "cff": "Cash from Financing",
    "revolver_draw_repay": "Revolver Draw / (Repay)",
}


def _label(item: str) -> str:
    """Return the display label for a line item."""
    return LABELS.get(item, item.replace("_", " ").title())


def _fmt(value: float) -> str:
    """Format a number to one decimal, suppressing negative zero."""
    return f"{(0.0 if abs(value) < 0.05 else value):>12,.1f}"


def format_model(years: list[dict[str, float]]) -> str:
    """Return the model as a plain-text table, one column per year."""
    header = f"{'':<28}" + "".join(f"{'Year ' + str(int(y['year'])):>12}" for y in years)
    lines = []
    for section, items in SECTIONS.items():
        lines += ["", section, header]
        for item in items:
            lines.append(f"{_label(item):<28}" + "".join(_fmt(y[item]) for y in years))
    return "\n".join(lines).lstrip()


def export_csv(years: list[dict[str, float]], path: str | Path) -> Path:
    """Write the model to CSV (rows = line items, columns = years) and return the path."""
    path = Path(path)
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Section", "Line item"] + [f"Year {int(y['year'])}" for y in years])
        for section, items in SECTIONS.items():
            for item in items:
                writer.writerow([section, _label(item)] + [round(y[item], 2) + 0.0 for y in years])
    return path


if __name__ == "__main__":
    model = build_model(Assumptions(), OpeningBalanceSheet())
    print(format_model(model))
    print(f"\nSaved: {export_csv(model, 'three_statement_model.csv')}")
