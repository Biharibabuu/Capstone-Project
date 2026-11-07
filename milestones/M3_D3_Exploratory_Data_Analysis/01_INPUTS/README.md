# M3 / D3 — Inputs

## Canonical EDA dataset
- [EDA ANALYSIS(4).xlsx](EDA%20ANALYSIS%284%29.xlsx)
- Worksheet: `Sheet1`
- Dimensions: 39 rows × 9 columns (including header)
- Data records: 38 quarterly observations
- SHA-256: `0c2a79065faaee48cec6393f79ff330a98a9eb20c1add3e87e8a45dd7e1c0f46`
- The workbook includes Year, Quarter (Calendar), PAT Margin, EBITDA Margin, USD/INR quarterly mean, CPI quarterly mean, WPI quarterly mean, daily oil-benchmark quarterly mean and monthly oil-benchmark quarterly mean.

## Notebook dependency
The canonical notebook at [02_WORKING](../02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb) reads this workbook. It uses EBITDA Margin as the sole EDA outcome and excludes PAT Margin from the analysis columns. Saved notebook summary statistics match the workbook's EBITDA Margin series.

## Source lineage
This is a derived EDA panel, not a primary external source. See [M2 / D2 Data Audit](../../M2_D2_Data_Audit/README.md), [source register](../../../data/source_register.csv) and [Phase 1 Data Collection Plan](../../../docs/Phase1_Data_Collection_Plan.md). Confirm source release/availability timing before using any variables in predictive backtests.

The previous malformed/small `EDA ANALYSIS(5).xlsx` entry was removed. Do not use it.
