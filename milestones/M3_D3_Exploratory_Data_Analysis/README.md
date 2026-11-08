# M3 / D3 — Exploratory Data Analysis

**Status: IN REVIEW — executed notebook and matching Excel input uploaded; reviewer sign-off pending.**

## Objective
Explore quarterly IndiGo EBITDA Margin and its association with USD/INR, CPI, WPI and supplied daily/monthly oil-benchmark indicators. This is exploratory analysis, not a causal study or forecast evaluation.

## Canonical files
- **Dataset:** [EDA ANALYSIS(4).xlsx](01_INPUTS/EDA%20ANALYSIS%284%29.xlsx), worksheet `Sheet1`.
- **Notebook:** [ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb).

The workbook contains 38 quarterly records and 9 columns, including PAT Margin. The notebook deliberately uses 8 columns and EBITDA Margin as its only profitability outcome. Its saved outputs were checked against the workbook: EBITDA Margin mean 12.306%, median 15.000% and standard deviation 14.255 percentage points.

## Notebook record
34 cells (20 markdown, 14 code), 43 saved outputs and 14 execution counts are retained. The input-loading code points to the workbook in M3/01_INPUTS and includes notebook-directory, repository-root, Colab and /mnt/data fallbacks.

## Analysis workflow
1. Load `Sheet1` from the canonical Excel input.
2. Check dimensions, duplicates, missingness, types and quarter coverage.
3. Standardize columns and construct chronological quarter-end dates.
4. Describe EBITDA-margin and macro/market indicator distributions.
5. Examine trends, correlations and calendar-quarter differences.
6. Test the five pre-specified hypotheses and record effect sizes and p-values.
7. Summarize insights, limitations and modelling recommendations for M4.

## Scope alignment
The adopted project target is EBITDA Margin, and this notebook's EBITDA-focused analysis is aligned with that target. The workbook also contains PAT Margin as a separate reference field, but PAT Margin is not the D3 outcome. The original D1 PDF proposed PAT Margin; the project's later scope decision adopting EBITDA Margin is documented in the M1 evaluation record and editable charter.

## Limitations
There are 38 quarterly observations. The oil series is a supplied benchmark proxy; the exact instrument and units are not fully established in the EDA workbook. Association does not establish causation or predictive performance.

## Standard milestone structure
- [01_INPUTS](01_INPUTS/README.md) — canonical Excel dataset and input lineage.
- [02_WORKING](02_WORKING/README.md) — canonical executed notebook.
- [03_DELIVERABLES](03_DELIVERABLES/README.md) — separate faculty-facing summary/report, if required.
- [04_EVIDENCE](04_EVIDENCE/README.md) — execution and review evidence.
- [05_REFERENCES](05_REFERENCES/README.md) — source and method references.

See [MILESTONE_CONTROL](MILESTONE_CONTROL.md), [DELIVERABLES_CHECKLIST](DELIVERABLES_CHECKLIST.md), [EVALUATION_RECORD](EVALUATION_RECORD.md) and [MILESTONE_MANIFEST](MILESTONE_MANIFEST.csv).
