# D4-v1 — Experiment Evidence and Reproducibility

This folder contains the experiment tracker and environment/run guidance for the D4-v1 EBITDA Margin forecasting exercise.

## Files

- [Experiment log CSV](experiment_log_d4-v1.csv) — candidate-level validation metrics, test metrics where saved, model parameters, feature set, seed and data-version caveats.
- [Requirements](requirements-d4-v1.txt) — Python package dependencies; xgboost is optional.
- [Run instructions](RUN_D4_v1.md) — setup and execution steps.

## Notebook and report

The training notebook used as the source for the report was supplied as `ML_Model_Training(1).ipynb`. It has not yet been committed to this repository folder. Add the executed notebook here before treating the repository evidence bundle as complete.

The assignment PDF is generated separately as `ANCP_T##_D4_v1.pdf`; it is not committed in this evidence folder yet.

## Recorded experiment outcome

- Target: next-quarter EBITDA Margin.
- Split: chronological 60% / 20% / 20% (20 train, 7 validation, 7 test rows).
- Validation winner: Seasonal Naive (MAE 7.470).
- Holdout Seasonal Naive: MAE 3.948, RMSE 4.714, MASE 0.237.
- Historical Mean holdout: MAE 12.948, RMSE 14.347, MASE 0.777.

## Data and execution caveats

The original notebook does not preserve the exact source workbook hash/version, run timestamp, package lockfile, or exact split quarter boundaries. The CSV labels the date as report-preparation date and explicitly records these omissions. Do not treat that date as the original execution timestamp. Capture these items in every subsequent run.
