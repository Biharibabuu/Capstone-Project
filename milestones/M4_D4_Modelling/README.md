# M4 / D4 — Modelling and Forecasting

**Status:** IN PROGRESS — current active milestone.

## Brief
Develop reproducible forecasting baselines and candidate models for IndiGo's next-quarter EBITDA margin. M4 includes target construction, feature engineering, chronological validation, model comparison, experiment tracking and a model-selection report.

## Data used
- [M4 quarterly snapshot](data/Final_Quarterly_Data%281%29.xlsx) — preserved modelling input snapshot and audit tabs.
- [M3 EBITDA-only analysis panel](../M3_D3_Exploratory_Data_Analysis/data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv) — 38-quarter exploratory handoff.
- [M2 source data index](../M2_D2_Data_Audit/data/README.md) — raw data lineage and dictionary.

## Workflow
1. Lock the M2/M3 dataset versions and checksums.
2. Verify EBITDA definition and revenue denominator; reconcile unavailable/estimated periods.
3. Build a chronological one-quarter-ahead supervised dataset without bridging missing periods.
4. Create persistence and seasonal-naive baselines.
5. Build candidate models with preprocessing fitted on training data only.
6. Tune on chronological validation; preserve a final untouched test segment.
7. Compare MAE/RMSE, inspect residuals and report limits.
8. Save model artefacts, run logs, predictions, tests, environment and report.
9. Hand the selected model/baseline and exact data version to M5.

## Important historical record
D4-v1 in the existing reports/notebooks is a completed PAT-margin experiment. Its metrics are preserved as legacy evidence only and must not be represented as EBITDA-model results. The current M4 work must produce a separate EBITDA-target experiment.

## Folder map
01_INPUTS approved datasets; 02_WORKING scripts/notebooks/tests; 03_DELIVERABLES model comparison report; 04_EVIDENCE experiments/metrics/predictions; 05_REFERENCES methodology/source references; data/ modelling dataset snapshots.

## Exit criteria
Reproducible EBITDA model pipeline, leakage-safe chronological validation, baseline comparison, tests and documented selection decision handed to M5.
