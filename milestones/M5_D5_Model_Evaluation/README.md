# M5 / D5 — Model Evaluation

**Status:** TODO — NOT STARTED

## Brief
Independently evaluate the M4-selected EBITDA-margin forecasting model. D5 tests reliability and robustness; it does not build the production UI or re-run arbitrary model searches.

## Inputs and data
- Frozen M4 model, preprocessing and candidate/baseline definitions.
- Exact M4 modelling dataset version and SHA-256.
- M2 source availability metadata and M3 EDA limitations.
- New evaluation panels only when versioned with source and availability dates.

## Workflow
1. Freeze candidate, baseline, feature schema and input vintage.
2. Enforce point-in-time eligibility using observation and publication/available-at dates.
3. Run expanding-window or rolling-origin backtests.
4. Compare MAE/RMSE against persistence and any appropriate seasonal-naive baseline.
5. Analyse residuals by quarter, period and market regime.
6. Quantify uncertainty and define forecast abstention conditions.
7. Prepare an evaluation report, model card update and deployment recommendation.

## Planned deliverables
Rolling-origin notebook/code; experiment log; prediction/error CSV; metrics JSON; evaluation report; updated model card; reproducibility manifest.

## Folder map
01_INPUTS frozen model and data contracts; 02_WORKING backtest notebook/code; 03_DELIVERABLES evaluation report; 04_EVIDENCE metrics/predictions/error analysis; 05_REFERENCES validation methodology.

## Exit gate
Reviewed point-in-time evaluation, benchmark comparison, error analysis and documented recommendation for deployment.
