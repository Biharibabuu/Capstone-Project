# M5 / D5 — Model Evaluation: Evaluation Record

**Status:** Planned; no completed D5 submission is claimed.

## Objective
Test temporal generalisation of the D4 persistence baseline and whether a challenger improves on unseen quarters. Establish when forecasts should be withheld.

## Required work
1. Preserve D4-v1 dataset SHA, fixed split, run log and selection decision as immutable comparator.
2. Reconcile observation dates with publication dates; use only point-in-time eligible features.
3. Run expanding-window/rolling-origin backtests without random shuffling.
4. Compare persistence and candidate models using MAE/RMSE on identical windows.
5. Analyse errors by regime, including exceptional loss and COVID periods.
6. Quantify uncertainty and define withholding rules for stale, missing or out-of-range inputs.
7. Produce evaluation report, notebook/code, experiment log, error table, metrics, data/environment manifests and model card.

## D4 handoff
Persistence was selected because neither Ridge nor Random Forest beat validation baseline. Validation MAE/RMSE = 12.18/13.92 pp; locked-test MAE/RMSE = 11.53/14.20 pp on eight quarters. Sample size is small and historical release timestamps are unavailable.

Update this folder's MILESTONE_MANIFEST.csv as each deliverable is completed and reviewed.
