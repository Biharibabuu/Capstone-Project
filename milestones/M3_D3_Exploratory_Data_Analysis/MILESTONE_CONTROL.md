# M3 / D3 — Milestone Control

**Administrative status:** Executed notebook uploaded; saved outputs preserved; clean rerun pending exact input workbook.  
**Project target:** EBITDA Margin only.  
**Canonical notebook:** [02_WORKING/ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb)  
**Standalone EDA Analysis workbook:** removed from M3.

## Purpose
Assess the 38-quarter dataset, describe EBITDA Margin and macro-market indicators, examine trends and calendar-quarter patterns, test five predefined hypotheses and document modelling implications for M4.

## Current notebook record
- 34 cells, including 14 code cells.
- 43 saved outputs and 14 execution counts.
- EBITDA Margin is the only profitability outcome.
- Analysis window: 2017-03-31 to 2026-06-30.
- Candidate indicators: USD/INR, CPI, WPI and daily/monthly oil-benchmark quarterly means.

## Input dependency
The notebook still expects `EDA ANALYSIS(5).xlsx`, worksheet `Sheet1`. This workbook is not committed in the repository. The saved outputs are retained, but clean execution from a fresh clone cannot currently be performed.

## Data-version warning
Do not substitute `Final_Quarterly_Data(4).xlsx` without reconciliation. Its 2020 Q4 EBITDA Margin is -201.391%, versus -20.391% in the prior EDA panel. This would materially change the mean, standard deviation and exploratory results.

## Work completed
- Replaced the previous edited D3 notebook version with the latest user-supplied executed notebook.
- Removed the previous M3 EDA Analysis Excel file.
- Preserved all saved notebook outputs.
- Updated README, evaluation record, manifest and M4 handoff notes.
- Recorded the required input file and unresolved source discrepancy.

## Exit criteria
1. Obtain the exact source workbook or approve a corrected quarterly source version.
2. Re-run the notebook from a clean environment and compare regenerated outputs to the retained execution.
3. Confirm the oil-benchmark security identity, units and source lineage.
4. Preserve chronological and publication-date controls in M4 modelling.

## Risks
Only 38 observations are available. Serial dependence, omitted operating drivers and the ambiguous oil-proxy definition limit interpretation. The analysis is exploratory and is not predictive validation.
