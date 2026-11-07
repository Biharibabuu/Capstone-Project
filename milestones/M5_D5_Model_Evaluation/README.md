# M5 / D5 — Model Evaluation

**Status:** TODO — NOT STARTED

## Brief
Independently evaluate the model selected from M4. D5 tests whether the model is reliable enough for intended use; it is not another model-building stage.

## Workflow
1. Freeze the M4 candidate, baseline, preprocessing and dataset vintage.
2. Establish point-in-time feature eligibility using observation and publication/availability dates.
3. Run expanding-window or rolling-origin backtests.
4. Compare against a simple baseline using MAE and RMSE.
5. Analyse residuals by period, market regime and unusual quarters.
6. Quantify uncertainty and define conditions under which forecasts should be withheld.
7. Write the evaluation report and update the model card.

## Inputs and data
- M2 source-data definitions and approved data package.
- M3 EDA handoff and exact data-vintage manifest.
- M4 EBITDA-target model artifact, preprocessing pipeline, experiment log and baseline.
- Any new data/features must be versioned; do not silently replace the M4 input snapshot.

## Planned deliverables
Rolling-origin notebook/code; evaluation experiment log; metrics and quarter-level error analysis; evaluation report; model-card evidence; data/environment manifests; reproducibility instructions.

## Dependencies and exit gate
Start after M4 model candidates and training protocol are stable. Close only when time-aware validation, leakage checks, baseline comparison, uncertainty and limitations are reviewed and reproducible.
