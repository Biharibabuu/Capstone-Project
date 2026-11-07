# M3 / D3 — EDA Input Data

**Purpose:** Record the exact quarterly panel used for exploratory data analysis and its lineage from M2.

## Dataset stored in this milestone

[EDA_ANALYSIS_EBITDA_ONLY_38Q.csv](EDA_ANALYSIS_EBITDA_ONLY_38Q.csv)

- 38 quarterly observations, 2017–2026 Q2.
- Eight fields only: Year, Calendar Quarter, EBITDA Margin, USD/INR quarterly mean, CPI quarterly mean, WPI quarterly mean, daily oil-benchmark quarterly mean and monthly oil-benchmark quarterly mean.
- PAT is excluded from this analytical input.
- SHA-256 of the source workbook EDA ANALYSIS(6).xlsx: 0c2a79065faaee48cec6393f79ff330a98a9eb20c1add3e87e8a45dd7e1c0f46.

## Workbook and notebook provenance

The uploaded workbook is EDA ANALYSIS(6).xlsx (Sheet1). The uploaded executed notebook refers internally to EDA ANALYSIS(5).xlsx; use the same column set and verify the workbook hash before rerunning.

The notebook has 34 cells, including 14 executed code cells with saved table and chart outputs. The source-only notebook currently committed at the M3 root remains the published reproducible-code copy. The full output-rich notebook has not been committed as a GitHub binary in this update.

## Input lineage

The raw financial and macro/market workbooks and their data dictionary are stored in [M2 / D2](../../M2_D2_Data_Audit/data/README.md). This M3 CSV is a derived EDA panel and should not replace the raw data or the D4 model input.
