# M4 / D4 — Modelling Data Package
### Active dataset and model-input governance

**Status:** In Progress  
**Target:** Next-quarter EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.

## 1. Inputs currently available

| Input | Path | Purpose | Status |
|---|---|---|---|
| Quarterly workbook snapshot | [Final_Quarterly_Data(1).xlsx](Final_Quarterly_Data%281%29.xlsx) | Historical D4-v1 benchmark input and audit sheets | Preserved; not an approved active EBITDA table without reconciliation |
| EBITDA EDA handoff | [M3 panel](../../M3_D3_Exploratory_Data_Analysis/data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv) | Exploratory context and feature reference | Available; 38 quarters |
| Raw financial/market sources | [M2 data package](../../M2_D2_Data_Audit/data/README.md) | Source lineage and field definitions | M2-owned; do not duplicate |

## 2. D4-v1 legacy snapshot

Keep D4-v1 input, code, experiment log, metrics and predictions as a historical experiment record. Its results are not the current EBITDA model results.

## 3. Active M4 build — pending

The current modelling table must be constructed separately:
1. Start from actual financial IS rows and statement definitions.
2. Calculate EBITDA Margin = EBITDA / Revenue from Operations × 100.
3. Exclude estimated rows from realised labels.
4. Reconcile dates and use the agreed Indian fiscal-quarter key.
5. Aggregate FX, CPI, WPI and Brent proxies using documented frequency rules.
6. Enforce publication/availability cutoffs at each historical forecast origin.
7. Do not bridge missing target quarters.
8. Record parent hashes, script/version, row counts, units and data-quality findings.

## 4. Candidate predictors

USD/INR, CPI, WPI and Dated Brent proxy (daily/monthly versions subject to collinearity and feature review). Do not claim unsupported load factor, yield, capacity, passenger demand or realised ATF features.

## 5. Required M4 outputs

- Versioned EBITDA modelling panel (CSV/Parquet).
- Target/feature dictionary and lineage manifest.
- Chronological train/validation/test split register.
- Data-quality report, source hashes and reproducibility notes.

These active EBITDA-target build outputs are pending. Do not label D4-v1 as the current approved EBITDA model dataset.

## 6. Handoff

M5 freezes and evaluates the exact M4-approved dataset/model. M6 uses the D5-approved feature contract. M7 cites final approved versions.