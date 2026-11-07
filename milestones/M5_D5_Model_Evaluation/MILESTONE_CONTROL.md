# M5 / D5 — Model Evaluation: Milestone Control

**Status:** PLANNED — no completed D5 report or rolling-origin evaluation is claimed.

## Purpose
Evaluate time-series generalisation and determine whether any challenger improves on the D4 persistence baseline. Define uncertainty and conditions where forecasts must be withheld.

## Inputs
Use D4-v1 as an immutable comparator. Any new reconciled dataset must have its own version, date key, point-in-time feature-availability record and SHA-256. Do not silently substitute a new workbook into D4-v1.

## Working record
Build rolling-origin/expanding-window evaluation code and notebook, error analysis and uncertainty analysis. No completed D5 working artifact is currently recorded.

## Deliverables
D5 evaluation report, updated model card and selected-model decision; pending.

## Evidence
Identical chronological folds for baseline/challengers, MAE/RMSE, quarter-level residuals, regime analysis, uncertainty and data/environment manifests; pending.

## Exit gate
Only select a model after point-in-time eligibility, repeatable rolling-origin results, baseline comparison, uncertainty and limitations are documented. If ML does not beat persistence, retain the baseline and state this honestly.
