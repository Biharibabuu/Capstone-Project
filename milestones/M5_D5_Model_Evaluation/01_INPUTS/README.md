# M5 / D5 — Evaluation Inputs

**Status:** Todo — evaluation has not started.

## Required upstream inputs

| Input | Owner | Required version/control |
|---|---|---|
| Selected EBITDA model and preprocessing | M4 / D4 | Commit ID, model version, environment and feature schema |
| Model-ready dataset | M4 / D4 | Exact path, SHA-256, target definition and date coverage |
| Baseline and split protocol | M4 / D4 | Baseline definition and chronological boundaries |
| Data provenance | M2 / D2 | Source IDs, units, observation dates and publication/availability metadata |
| EDA caveats | M3 / D3 | 38-quarter sample, Brent proxy and target-validation limitations |

## No independent training dataset

M5 must not define a new target or silently replace the M4 dataset. Store the frozen evaluation snapshot or controlled reference to the exact M4 artifact, plus D5-specific predictions and errors under 04_EVIDENCE/.

## Planned evaluation outputs

Rolling-origin forecast origins and target quarters; actual versus predicted EBITDA Margin; MAE/RMSE by fold; baseline-relative errors; residual analysis; robustness results; uncertainty/calibration where supported; and model/data version manifest.

M5 remains Todo until M4 candidate and evaluation protocol are stable.