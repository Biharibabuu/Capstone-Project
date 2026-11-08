# M3 / D3 — Inputs

## EDA source-file status
The prior standalone EDA Analysis workbook has been removed from this milestone. No EDA-specific Excel dataset is currently stored under `01_INPUTS`.

## Notebook input dependency
The canonical executed notebook in [02_WORKING](../02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb) expects:
- Filename: `EDA ANALYSIS(5).xlsx`
- Worksheet: `Sheet1`
- Required columns: Year, Quarter (Calendar), EBITDA Margin, USD/INR quarterly mean, CPI quarterly mean, WPI quarterly mean, daily oil-benchmark quarterly mean and monthly oil-benchmark quarterly mean.
- Expected panel: 38 quarterly observations.

This exact workbook is not committed to GitHub. It must be provided locally before a clean execution can be reproduced. The notebook's saved outputs are retained in GitHub and can be reviewed without rerunning the notebook.

## Candidate not substituted
`Final_Quarterly_Data(4).xlsx` was not substituted for the removed EDA workbook because its 2020 Q4 EBITDA Margin is -201.391%, compared with -20.391% in the previous EDA panel. This discrepancy changes summary statistics and must be reconciled with the source financial statement before use.

See [M3 README](../README.md), [M3 evaluation record](../EVALUATION_RECORD.md) and [M2 data audit](../../M2_D2_Data_Audit/README.md).
