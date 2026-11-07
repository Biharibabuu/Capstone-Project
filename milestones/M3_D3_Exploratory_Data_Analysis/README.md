# M3 / D3 — Exploratory Data Analysis

**Status: IN REVIEW — latest executed notebook uploaded; input-data and target-alignment gates remain open.**

## Canonical notebook
[ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb)

This is the executed notebook supplied on 7 November 2026. It contains 34 cells (20 markdown and 14 code), 43 saved outputs and 14 execution counts. Saved chart and table outputs have been retained.

**Original attachment SHA-256:** 74c175b6b4b701b767702bff8945fb0ec7e5d7aea1342ae48117bbc54896fb78

## Dataset referenced by notebook
- Workbook: EDA ANALYSIS(5).xlsx
- Worksheet: Sheet1
- Observation count: 38 quarterly observations
- Quarter span shown in output: 31 March 2017 to 30 June 2026
- Outcome: EBITDA Margin
- Indicators: USD/INR, CPI, WPI, daily oil-benchmark quarterly mean and monthly oil-benchmark quarterly mean
- Quarter definition: calendar quarters

**Input status:** EDA ANALYSIS(5).xlsx was not attached with the notebook and is not in this repository. The executed results are viewable, but a clean rerun requires this exact workbook in 01_INPUTS. Do not substitute an older EDA workbook.

## Recorded hypothesis results
| Hypothesis | Spearman rho / test | p-value | Result |
|---|---:|---:|---|
| EBITDA Margin and USD/INR | 0.554 | <0.001 | Significant exploratory association |
| EBITDA Margin and monthly oil proxy | 0.264 | 0.109 | Not significant |
| EBITDA Margin and CPI | -0.087 | 0.605 | Not significant |
| EBITDA Margin and WPI | -0.450 | 0.005 | Significant exploratory association |
| EBITDA Margin across calendar quarters | Kruskal–Wallis | 0.125 | No significant quarter-group difference |

Descriptive results: mean EBITDA Margin 12.306%, median 15.000%, standard deviation 14.255 percentage points. The notebook cautions that small sample size and time dependence limit inference. These are associations, not causal effects or predictive-performance results.

## Scope alignment gate
The approved D1/D4 project target elsewhere in the repository is next-quarter **PAT Margin**. This D3 notebook analyses **EBITDA Margin** only. Keep it as the requested D3 artifact, but do not treat its results as validation of a PAT-margin model. The team must decide whether this is supplementary EBITDA analysis or whether a PAT-margin EDA is also required.

## Limitations stated in notebook
The 38-quarter workbook does not include passenger load factor, passenger yield, capacity, revenue, fuel consumption or explicit source metadata. The exact oil benchmark and units are not identified in the workbook; it is treated as a supplied proxy.

## Standard structure
- 01_INPUTS — input workbook register and authorized input files.
- 02_WORKING — the single canonical executed D3 notebook.
- 03_DELIVERABLES — faculty-ready D3 report/summary; not yet supplied separately.
- 04_EVIDENCE — execution and review evidence; notebook outputs are embedded.
- 05_REFERENCES — data definitions, provenance and source references.

See MILESTONE_CONTROL.md, DELIVERABLES_CHECKLIST.md, EVALUATION_RECORD.md and MILESTONE_MANIFEST.csv.

## Exit criteria
D3 may be marked complete after the exact input workbook is added, the notebook is rerun from a clean environment, the result is checked against the input and EBITDA-vs-PAT target scope is approved.
