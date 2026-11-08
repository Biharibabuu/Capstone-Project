# M3 / D3 — Exploratory Data Analysis

**Status:** Executed notebook uploaded; saved outputs retained; clean rerun pending exact source workbook.

## Purpose
Explore quarterly IndiGo EBITDA Margin and its relationship with USD/INR, CPI, WPI and supplied daily/monthly oil-benchmark indicators. The work supports feature understanding for next-quarter EBITDA Margin modelling. It is not causal analysis or predictive model validation.

## Canonical D3 artifact
- **Notebook:** [ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb).
- **Contents:** 34 cells (20 markdown and 14 code), 43 saved outputs and 14 execution counts.
- **Status:** latest user-supplied notebook is the only D3 notebook retained. The previous input workbook `EDA ANALYSIS(4).xlsx` has been removed from this milestone.

## Analysis profile
The executed notebook analyses 38 quarterly observations from 31 March 2017 through 30 June 2026. It uses EBITDA Margin as the sole profitability outcome and five macro/market measures: USD/INR, CPI, WPI, daily oil-benchmark quarterly mean and monthly oil-benchmark quarterly mean.

| Measure | Result |
|---|---:|
| Mean EBITDA Margin | 12.306% |
| Median EBITDA Margin | 15.000% |
| Standard deviation | 14.255 percentage points |
| Minimum | -36.667% |
| Maximum | 29.933% |
| Duplicate Year–Quarter rows | 0 |
| Missing values in transformed analysis panel | 0 |

## Hypothesis results
| Hypothesis | Statistic | p-value | Notebook interpretation |
|---|---:|---:|---|
| H1: EBITDA Margin and USD/INR | Spearman rho 0.554 | <0.001 | Significant exploratory association |
| H2: EBITDA Margin and monthly oil proxy | Spearman rho 0.264 | 0.109 | Not statistically significant |
| H3: EBITDA Margin and CPI | Spearman rho -0.087 | 0.605 | Not statistically significant |
| H4: EBITDA Margin and WPI | Spearman rho -0.450 | 0.005 | Significant exploratory association |
| H5: EBITDA Margin across calendar quarters | Kruskal–Wallis | 0.125 | No significant quarter-group difference |

These are same-period exploratory results. They do not show that the variables cause EBITDA Margin movements or improve one-quarter-ahead forecast accuracy.

## Dataset handling and reproducibility
The standalone EDA Analysis Excel file has been removed from M3 as requested. The uploaded notebook's data-loading cell still expects `EDA ANALYSIS(5).xlsx`, worksheet `Sheet1`. That exact source workbook is not committed in GitHub, so the saved outputs are viewable but a clean rerun is not yet reproducible.

Do not silently replace that input with `Final_Quarterly_Data(4).xlsx`: the latter has a 2020 Q4 EBITDA Margin of -201.391%, whereas the previous EDA panel has -20.391%. This is a material source-data discrepancy that must be reconciled before refreshing notebook outputs or modelling.

## Limitations
- Only 38 quarterly observations are available; statistical power and model reliability are limited.
- The exact oil benchmark identity and units are not fully documented. It is a proxy, not IndiGo's realised ATF cost.
- The workbook does not include passenger load factor, yield, passenger count, capacity, fuel consumption or route mix.
- Quarterly observations may be serially dependent.
- Statistical significance is exploratory and does not establish causation or predictive value.

## Milestone structure
- [01_INPUTS](01_INPUTS/README.md) — source dependency status; no separate EDA workbook retained.
- [02_WORKING](02_WORKING/README.md) — canonical executed notebook.
- [03_DELIVERABLES](03_DELIVERABLES/README.md) — faculty-facing summary/report, if separately required.
- [04_EVIDENCE](04_EVIDENCE/README.md) — preserved notebook outputs and clean-run evidence.
- [05_REFERENCES](05_REFERENCES/README.md) — source lineage and methods.

See [MILESTONE_CONTROL](MILESTONE_CONTROL.md), [DELIVERABLES_CHECKLIST](DELIVERABLES_CHECKLIST.md), [EVALUATION_RECORD](EVALUATION_RECORD.md) and [MILESTONE_MANIFEST](MILESTONE_MANIFEST.csv).
