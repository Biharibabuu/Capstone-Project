# M3 / D3 — EDA Evaluation Record

**Status:** Notebook and matching Excel input uploaded; scope/reviewer approval pending.  
**Dataset:** [EDA ANALYSIS(4).xlsx](01_INPUTS/EDA%20ANALYSIS%284%29.xlsx), Sheet1.  
**Notebook:** [ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb).

## Dataset
38 quarterly observations, 9 columns including header. The data fields are Year, Quarter (Calendar), PAT Margin, EBITDA Margin, USD/INR quarterly mean, CPI quarterly mean, WPI quarterly mean, daily oil-benchmark quarterly mean and monthly oil-benchmark quarterly mean. SHA-256: `0c2a79065faaee48cec6393f79ff330a98a9eb20c1add3e87e8a45dd7e1c0f46`.

The notebook uses 8 fields: Year, Quarter (Calendar), EBITDA Margin, USD/INR, CPI, WPI, daily oil benchmark and monthly oil benchmark. PAT Margin is present in the Excel file but intentionally excluded from this EBITDA-focused notebook.

## Notebook integrity and data match
The executed notebook retains 34 cells, 43 saved outputs and 14 execution counts. The workbook's EBITDA Margin statistics are mean 12.305878%, median 15.000185% and sample standard deviation 14.255359 percentage points. These match the notebook's saved rounded summary (12.306%, 15.000%, 14.255%). The notebook input path and labels have been updated to the committed Excel filename. The notebook was not freshly re-executed after that path change.

## Exploratory results
- H1 USD/INR: Spearman rho 0.554, p < 0.001, n = 38.
- H2 monthly oil proxy: rho 0.264, p = 0.109, n = 38.
- H3 CPI: rho -0.087, p = 0.605, n = 38.
- H4 WPI: rho -0.450, p = 0.005, n = 38.
- H5 calendar-quarter difference: Kruskal–Wallis p = 0.125, n = 38.

These are exploratory same-period associations, not causal effects or out-of-sample next-quarter prediction evidence. The sample is small and time-dependent.

## Critical project-target alignment
The approved D1/D4 project target is PAT Margin. This notebook analyses EBITDA Margin only, even though PAT Margin exists in the input workbook. Keep D3 described as EBITDA-focused unless the team explicitly expands the analysis to PAT Margin and reruns the tests.

## Closure criteria
1. Clean-run the notebook from M3/02_WORKING using the uploaded workbook in M3/01_INPUTS.
2. Confirm the oil benchmark definition/units and source lineage.
3. Approve the EBITDA-vs-PAT EDA scope with the capstone team/faculty.
4. Store any separate faculty-ready summary/report in 03_DELIVERABLES and update the manifest.
