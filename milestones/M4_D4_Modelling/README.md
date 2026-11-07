# M4 / D4 — Modelling and Forecasting

**Status:** IN PROGRESS — current active milestone.

## Brief
Develop and compare reproducible forecasting approaches for IndiGo's next-quarter EBITDA margin. M4 includes feature preparation, baseline modelling, candidate models, chronological validation, experiment tracking and model selection.

## Workflow
1. Lock the M3 EBITDA-only EDA panel and M2 source lineage.
2. Reconcile target construction and convert calendar labels to the agreed fiscal-quarter key where appropriate.
3. Build supervised one-quarter-ahead features with no look-ahead leakage.
4. Establish a simple persistence baseline.
5. Train candidate models with preprocessing fitted on training data only.
6. Tune using chronological validation, then retain a locked test period.
7. Compare MAE/RMSE and inspect errors by quarter/regime.
8. Save run logs, predictions, metrics, tests, data/environment manifests and a report.
9. Select a model only if evidence supports improvement over the baseline; otherwise retain the baseline and explain why.

## Data used
- [M4 modelling snapshot](data/Final_Quarterly_Data%281%29.xlsx) — quarterly source snapshot and audit sheets.
- [M3 EBITDA-only EDA panel](../M3_D3_Exploratory_Data_Analysis/data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv) — 38-quarter, eight-field analysis panel.
- [M2 raw/source workbooks](../M2_D2_Data_Audit/data/README.md) — underlying statement and macro/market provenance.

## Existing evidence and current caution
The existing D4-v1 run is a historical PAT-margin experiment. It compared persistence, Ridge and Random Forest and found neither ML candidate beat the persistence baseline on validation. Keep those artifacts as a reproducibility record only; do not present them as the current EBITDA model.

## Folder map
- data/ — immutable modelling input and source links.
- notebooks/ — modelling experiments.
- src/ — training and feature engineering code.
- tests/ — automated checks.
- experiments/ — logs, metrics, predictions and manifests.
- reports/ — model comparison report and decisions.
- MILESTONE_CONTROL.md and DELIVERABLES_CHECKLIST.md — scope and acceptance tracking.

## Exit gate
M4 closes only when the EBITDA-margin training workflow is reproducible, tested, chronologically evaluated, compared against a baseline and documented with limitations.


## Standard evaluation structure

- [01_INPUTS](01_INPUTS/README.md)
- [02_WORKING](02_WORKING/README.md)
- [03_DELIVERABLES](03_DELIVERABLES/README.md)
- [04_EVIDENCE](04_EVIDENCE/README.md)
- [05_REFERENCES](05_REFERENCES/README.md)

See MILESTONE_CONTROL.md, DELIVERABLES_CHECKLIST.md, EVALUATION_RECORD.md and MILESTONE_MANIFEST.csv.
