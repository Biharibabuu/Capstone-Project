# Milestone M4 / D4-v1 — Modelling checkpoint

**Status:** In Progress — D4 is the active milestone. D4-v1 is a completed baseline experiment within the milestone; further modelling work remains open.
**Course outcome:** CO3.

## Folder contents
- reports/ANCP_T##_D4_v1.pdf — four-page report within the five-page limit.
- src/d4_train.py — supervised data preparation, fixed chronological split, baseline, candidate models, tuning and locked holdout evaluation.
- notebooks/D4_modeling_experiment.ipynb — reproducible experiment notebook.
- tests/test_d4_train.py — lag and split tests (2 passed locally).
- experiments/D4_experiment_log.csv — all 12 runs: baseline, 10 candidate configurations and final test.
- experiments/D4_candidate_results.csv — candidate validation comparison.
- experiments/D4_metrics.json — full model-selection and test metrics.
- experiments/D4_test_predictions.csv — eight locked test predictions and absolute errors.
- experiments/D4_data_manifest.json — input workbook, worksheet, SHA-256 and row accounting.
- experiments/D4_environment.json and requirements-d4.txt — versions and pinned dependencies.

## Problem and model choice
This is supervised regression to estimate next-quarter PAT margin in percentage points. The persistence baseline carries forward the immediately preceding reported quarter's PAT margin. Ridge regression is a regularised linear challenger suitable for a small sample with potentially correlated macro variables. Random Forest is a nonlinear challenger that can represent thresholds and interactions; shallow depth and leaf-size constraints limit complexity.

## Fixed validation protocol
The split windows are constants in the training script; tuning sees only the validation period. The locked test is not used for hyperparameter selection.

| Split | Target-quarter window | Rows |
|---|---|---:|
| Train | 2017Q4–2022Q4 | 21 |
| Validation | 2023Q1–2024Q2 | 6 |
| Test | 2024Q3–2026Q2 | 8 |

## Result summary
- Persistence baseline validation: MAE **12.18 pp**, RMSE **13.92 pp**.
- Best Ridge validation: MAE **42.62 pp**, RMSE **43.94 pp** (alpha=100).
- Best Random Forest validation: MAE **51.95 pp**, RMSE **54.15 pp** (max_depth=2, min_samples_leaf=3).
- Selected D4-v1 model: persistence baseline, because neither candidate beat it on validation.
- Locked test: MAE **11.53 pp**, RMSE **14.20 pp**. Test MAE improvement against the same persistence rule is **0%**.

The candidate ML models did not improve on the simple baseline. The eight-quarter holdout and 35 supervised rows are small; this is an academic backtest, not production forecasting validation.

## Reproduce
From repository root:
```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r milestones/M4_D4_Modelling/requirements-d4.txt
python -m src.d4_train --input "data/processed/Final_Quarterly_Data(1).xlsx" --output-dir "milestones/M4_D4_Modelling/experiments"
pytest -q milestones/M4_D4_Modelling/tests/test_d4_train.py
```

The SHA-256 hash in the data manifest and run log identifies the exact input. Random seed is 42.

## Limitations and handoff to D5
The source uses calendar-quarter labels, not relabelled Indian fiscal quarters. Historical publication timestamps are not available, so one-quarter lagging prevents same-quarter target leakage but does not prove exact point-in-time public availability. Brent is a crude benchmark proxy, not IndiGo's realised ATF cost. D5 should add release-date/vintage controls, inspect errors by regime, expand rolling-origin evaluation and quantify forecast uncertainty.

## Standard folder structure

- `data/` — immutable modelling input references and checksums.
- `notebooks/` — reproducible experiments.
- `src/` — training and feature pipeline code.
- `tests/` — automated checks.
- `experiments/` — run logs, metrics, predictions and manifests.
- `reports/` — experiment reports and model-selection decisions.
- `MILESTONE_CONTROL.md` and `DELIVERABLES_CHECKLIST.md` — current scope and acceptance gate.
