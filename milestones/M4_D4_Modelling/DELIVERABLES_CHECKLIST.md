# M4 / D4 — EBITDA Margin Modelling Checklist

**Status:** IN PROGRESS. The current M4 deliverable is a separate EBITDA Margin experiment. The existing D4-v1 PAT-margin experiment is retained only as legacy evidence.

## Target and data
- [x] Adopted target recorded: next-quarter EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.
- [x] M3 EDA workbook and notebook available as the exploratory handoff.
- [ ] Confirm source EBITDA definition and Revenue from Operations denominator.
- [ ] Reconcile target-quarter financial rows, estimates and unavailable periods against raw CP `IS` sheet.
- [ ] Freeze the approved EBITDA modelling dataset and record its SHA-256, source lineage and fiscal-quarter keys.
- [ ] Ensure the target-quarter EBITDA and revenue values are labels only, never predictors.
- [ ] Record actual/publication availability dates or apply an explicit conservative lag.

## Modelling workflow
- [ ] Create the one-quarter-ahead supervised table without bridging missing quarters.
- [ ] Implement persistence and seasonal-naive benchmarks.
- [ ] Implement parsimonious challenger model(s) only where sample size supports them.
- [ ] Use chronological train/validation/test or rolling-origin splits; do not shuffle quarters.
- [ ] Fit imputation, scaling and feature selection only on training data.
- [ ] Compare baseline and challengers on the same periods using MAE and RMSE in EBITDA-Margin percentage points.
- [ ] Save quarter-level predictions, residuals, metrics and model-selection rationale.

## Reproducibility and handoff
- [ ] Add run log, seed/configuration, environment and dataset manifest.
- [ ] Add or update unit tests for target construction, chronology and leakage controls.
- [ ] Produce the M4 EBITDA modelling report and document limitations.
- [ ] Hand the selected baseline/candidate and frozen data version to M5.

## Legacy evidence
- [x] D4-v1 PAT-margin experiment is preserved and labelled as legacy.
- [x] Its metrics are not represented as EBITDA model performance.

The D4-v1 PAT code, report and metrics do not complete the active EBITDA Margin modelling milestone.
