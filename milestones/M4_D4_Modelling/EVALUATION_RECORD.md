# M4 / D4 — Modelling Evaluation Record

**Status:** IN PROGRESS — current active milestone  
**Current target:** Next-quarter EBITDA margin

## 1. Purpose

Build and compare forecasting baselines and candidate models using the M3 EBITDA-only EDA handoff and approved M2 source definitions. M4 is not complete merely because an earlier PAT-margin experiment was run.

## 2. Current data

- Primary EDA panel: [M3 EBITDA-only 38-quarter CSV](../../M3_D3_Exploratory_Data_Analysis/data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv).
- Quarterly workbook snapshot: [Final_Quarterly_Data(1).xlsx](data/Final_Quarterly_Data%281%29.xlsx); SHA-256 recorded in `data/README.md`.
- Raw statement and market sources: [M2 data package](../../M2_D2_Data_Audit/data/README.md).

## 3. Historical experiment — D4-v1 (legacy PAT target)

D4-v1 remains preserved as historical evidence only:
- Target: next-quarter PAT margin, not EBITDA margin.
- Models compared: persistence, Ridge and Random Forest.
- Persistence validation MAE/RMSE: 12.18/13.92 percentage points.
- Ridge and Random Forest did not outperform persistence on validation.
- Locked-test persistence MAE/RMSE: 11.53/14.20 percentage points.
- No ML improvement was demonstrated.

Do not quote these values as performance of the current EBITDA model.

## 4. Current M4 work required

1. Freeze the M3 EBITDA-only panel and its checksum.
2. Confirm the EBITDA margin formula and revenue denominator against source statement data.
3. Construct a clean one-quarter-ahead supervised table; do not bridge missing quarters.
4. Establish persistence and seasonal-naive baselines.
5. Compare parsimonious candidates with time-ordered validation.
6. Enforce training-only preprocessing and feature-availability cut-offs.
7. Save run configuration, metrics, predictions, residuals, tests, environment and report.
8. Select no complex model unless it beats the baseline in defensible validation.

## 5. Exit gate

M4 is complete only when the EBITDA target data and feature pipeline are frozen, the experiments are reproducible, the model comparison is documented, and the selected baseline/candidate is handed to M5 for independent rolling-origin evaluation.
