---
title: "The Three-Statement Model: How the Income Statement, Balance Sheet and Cash Flow Fit Together"
slug: three-statement-financial-model
date: 2026-10-02
author: Muhammad Naseer, OSPA
category: Insights
tags: [Financial Modelling, FP&A, Due Diligence, U.S. GAAP]
summary: "A practical guide to building a linked three-statement model, with a five-year worked example, the five checks that prove it works, and the U.S. GAAP points that matter."
reading_time: 7 min
---

# The Three-Statement Model: How the Income Statement, Balance Sheet and Cash Flow Fit Together

Every serious finance decision, from a bank facility to an acquisition, eventually comes back to one question: does the cash work? A three-statement model answers it by linking the income statement, balance sheet and cash flow statement so that a change in one assumption flows correctly through all three.

Most models we review in due diligence fail not because the formulas are wrong, but because the statements are not truly linked. Cash is hard-coded, working capital is a plug, or the balance sheet is forced to balance. This article sets out how a properly linked model is built, using a five-year worked example.

## 1. What each statement does

- **Income statement:** measures performance on an accrual basis. Revenue is recognised when control transfers to the customer under ASC 606, not when cash is received.
- **Balance sheet:** records the position at a point in time: what the business owns, owes, and what belongs to shareholders.
- **Cash flow statement:** reconciles accrual profit to actual cash movement, classified into operating, investing and financing activities under ASC 230.

Individually, each statement tells part of the story. Linked, they tell you whether the business can fund its growth.

## 2. The four links that hold the model together

1. **Net income to equity.** Net income from the income statement increases retained earnings; dividends reduce it. Closing equity = opening equity + net income - dividends.
2. **Net income to cash flow.** The cash flow statement starts with net income, then adds back non-cash charges such as depreciation.
3. **Balance sheet movements to cash flow.** Every change in a balance sheet account, other than cash, must appear in the cash flow statement. Higher receivables consume cash; higher payables provide it.
4. **Cash flow to cash.** Closing cash on the balance sheet = opening cash + net change in cash from the cash flow statement. Cash is never typed in.

If these four links hold, the balance sheet balances on its own. If it needs a plug, one of the links is broken.

## 3. A five-year worked example

The example below starts from an opening balance sheet of 4,900 in total assets and uses these drivers:

| Driver | Assumption |
|---|---|
| Base revenue | 10,000 |
| Revenue growth | 10%, 10%, 8%, 7%, 6% |
| Gross margin | 40% |
| Operating expenses | 20% of revenue |
| Capex | 5% of revenue |
| Depreciation | 10% of opening net PP&E |
| Receivable / inventory / payable days | 30 / 45 / 30 |
| Term debt | 2,000 at 7%, repaying 200 a year |
| Tax rate | 21% (U.S. federal corporate rate) |
| Dividend payout | 20% of net income |
| Minimum cash | 250, funded by a revolver if needed |

**Results:**

| | Year 1 | Year 3 | Year 5 |
|---|---:|---:|---:|
| Revenue | 11,000 | 13,068 | 14,822 |
| EBITDA | 2,200 | 2,614 | 2,964 |
| Net income | 1,398 | 1,724 | 2,000 |
| Cash from operations | 1,523 | 1,973 | 2,325 |
| Capex | (550) | (653) | (741) |
| Closing cash | 993 | 2,428 | 4,292 |
| Term debt | 1,800 | 1,400 | 1,000 |
| Balance check | 0.0 | 0.0 | 0.0 |

Three observations a lender or investor would draw immediately:

- **Year 1 working capital absorbs 175 of cash.** Receivables rise by 104 and inventory by 214, partly offset by a 143 increase in payables. Growth costs cash before it produces it.
- **Cash conversion is strong.** Cash from operations exceeds net income in every year, reaching 2,325 against net income of 2,000 in Year 5.
- **The business deleverages from its own cash flow.** Term debt falls by 1,000 over five years while cash rises by 3,792, and the revolver is never drawn.

## 4. Five checks that prove the model works

Before any model is relied on, we apply five tests:

1. **Balance check equals zero in every period**, without a plug.
2. **Cash ties:** balance sheet cash equals opening cash plus the cash flow statement's net change.
3. **Equity rolls forward:** opening equity + net income - dividends = closing equity.
4. **No tax on losses:** a loss-making scenario produces zero current tax (deferred tax under ASC 740 is modelled separately where material).
5. **Stress test:** cut gross margin sharply and confirm the revolver draws, cash never falls below the minimum, and the balance sheet still balances.

A model that passes all five can be trusted to answer "what if" questions. One that fails any of them cannot.

## 5. Design choices that keep models reliable

- **Interest on opening balances.** Calculating interest on average balances creates a circular reference between interest, net income and debt. Using opening balances removes the circularity with immaterial loss of accuracy in an annual model.
- **An automatic revolver.** Rather than letting cash go negative, a revolver draws to hold minimum cash and repays from surplus. This shows funding needs directly.
- **Drivers separated from calculations.** All assumptions sit in one place, so scenarios change inputs, never formulas.
- **Validation built in.** Our models run the five checks automatically every time an assumption changes.

## 6. U.S. GAAP points that change the numbers

- **ASC 606 (revenue):** multi-element contracts, variable consideration and timing of control transfer can move revenue between periods and create contract assets or liabilities on the balance sheet.
- **ASC 842 (leases):** operating leases bring right-of-use assets and lease liabilities onto the balance sheet, affecting leverage ratios and covenant headroom.
- **ASC 810 (consolidation):** group models must eliminate intercompany balances and present non-controlling interests correctly.
- **ASC 230 (cash flows):** classification matters. Interest paid sits in operating activities under U.S. GAAP, whereas IFRS allows a policy choice, which is relevant for groups reporting in both the U.S. and the UAE.

## How OSPA can help

OSPA builds and reviews financial models for transactions, financing and board decision-making across the UAE, the GCC and the United States. Our models are fully linked, automatically tested, and documented so your team can run scenarios with confidence.

- Three-statement and integrated operating models
- Financial due diligence and model audits
- Lender and investor cases with covenant testing
- Group consolidation models under U.S. GAAP and IFRS

**Talk to us:** [mnaseer@ospa.ae](mailto:mnaseer@ospa.ae) | [ospa.ae](https://ospa.ae)

*This article is for general information and does not constitute accounting, tax or investment advice.*
