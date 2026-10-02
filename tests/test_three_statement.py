import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from three_statement import (  # noqa: E402
    Assumptions,
    OpeningBalanceSheet,
    build_model,
    export_csv,
    format_model,
)


@pytest.fixture
def model():
    return build_model(Assumptions(), OpeningBalanceSheet())


def test_balance_sheet_balances_every_year(model):
    for y in model:
        assert y["balance_check"] == pytest.approx(0.0, abs=1e-6)


def test_cash_flow_ties_to_balance_sheet_cash(model):
    prev_cash = OpeningBalanceSheet().cash
    for y in model:
        assert y["cash"] == pytest.approx(prev_cash + y["net_change_cash"])
        prev_cash = y["cash"]


def test_year_one_income_statement_figures(model):
    y1 = model[0]
    assert y1["revenue"] == pytest.approx(11_000.0)
    assert y1["gross_profit"] == pytest.approx(4_400.0)
    assert y1["ebitda"] == pytest.approx(2_200.0)
    assert y1["depreciation"] == pytest.approx(300.0)
    # Interest: 2,000 x 7% = 140 expense; 500 x 2% = 10 income
    assert y1["pre_tax_income"] == pytest.approx(1_770.0)
    assert y1["net_income"] == pytest.approx(1_770.0 * 0.79)


def test_retained_earnings_roll_forward(model):
    prev_equity = OpeningBalanceSheet().equity
    for y in model:
        assert y["equity"] == pytest.approx(prev_equity + y["net_income"] - y["dividends"])
        prev_equity = y["equity"]


def test_revolver_draws_to_hold_minimum_cash():
    a = Assumptions(gross_margin=0.10, minimum_cash=400.0)  # loss-making case
    model = build_model(a, OpeningBalanceSheet())
    for y in model:
        assert y["cash"] >= a.minimum_cash - 1e-6
        assert y["balance_check"] == pytest.approx(0.0, abs=1e-6)
    assert model[-1]["revolver"] > 0


def test_no_tax_on_losses():
    model = build_model(Assumptions(gross_margin=0.10), OpeningBalanceSheet())
    assert model[0]["pre_tax_income"] < 0
    assert model[0]["tax"] == 0


def test_rejects_unbalanced_opening_balance_sheet():
    with pytest.raises(ValueError):
        build_model(Assumptions(), OpeningBalanceSheet(cash=999.0))


def test_format_and_csv_export(model, tmp_path):
    text = format_model(model)
    assert "INCOME STATEMENT" in text and "Year 5" in text
    path = export_csv(model, tmp_path / "out.csv")
    assert path.read_text().startswith("Section,Line item,Year 1")
