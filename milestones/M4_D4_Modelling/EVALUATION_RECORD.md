# M4 / D4-v1 — Modelling Checkpoint: Evaluation Record

**Status:** Executed and documented on 7-Nov-2026. Course outcome CO3.

## Objective and data
Supervised regression to estimate next-quarter PAT margin in percentage points (PAT / Revenue from Operations × 100); not share-price prediction.

- Input: data/processed/Final_Quarterly_Data(1).xlsx; worksheet Final_Quarterly_Data.
- SHA-256: 85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c.
- 38 source rows; two excluded because Financial Data Status was not Reported (original value); 35 supervised observations after one-quarter lag.
- Calendar-quarter labels retained as supplied, not relabelled as Indian fiscal quarters.

| Split | Window | Rows |
|---|---|---:|
| Train | 2017Q4–2022Q4 | 21 |
| Validation | 2023Q1–2024Q2 | 6 |
| Locked test | 2024Q3–2026Q2 | 8 |

Predictors: lag1 PAT margin, EBITDA margin, USD/INR, CPI, WPI and monthly Brent. Only the immediately preceding reported quarter is used; gaps are not bridged. No random shuffling.

## Model results
| Model | Validation MAE (pp) | Validation RMSE (pp) | Decision |
|---|---:|---:|---|
| Persistence | **12.18** | **13.92** | Selected |
| Best Ridge (alpha=100) | 42.62 | 43.94 | Not selected |
| Best Random Forest (depth=2, leaf=3) | 51.95 | 54.15 | Not selected |

Locked test persistence MAE = **11.53 pp**, RMSE = **14.20 pp**; improvement versus the same baseline = **0%**. No trained ML artifact was selected.

## Files in this milestone
- reports/ANCP_T##_D4_v1.pdf — four-page report.
- src/d4_train.py — preparation, fixed split, baseline and challenger workflow.
- notebooks/D4_modeling_experiment.ipynb — experiment notebook.
- tests/test_d4_train.py — lag/split tests.
- requirements-d4.txt — pinned environment.
- experiments/D4_experiment_log.csv — 12 runs.
- experiments/D4_candidate_results.csv — validation comparison.
- experiments/D4_metrics.json — selection and metrics.
- experiments/D4_test_predictions.csv — eight locked test rows.
- experiments/D4_data_manifest.json — input checksum/row accounting.
- experiments/D4_environment.json — runtime/dependency versions.
- README.md and MILESTONE_MANIFEST.csv — reproduction and inventory.

Reproduce: install milestones/M4_D4_Modelling/requirements-d4.txt; run src/d4_train.py with data/processed/Final_Quarterly_Data(1).xlsx; run pytest on milestones/M4_D4_Modelling/tests/test_d4_train.py.

## Limitations and next gate
35 observations are small; validation/test are 6/8. Historical release timestamps are missing, Brent is a proxy and calendar quarter labels remain. Newer Final_Quarterly_Data(2).xlsx is a distinct local receipt and must be reconciled/versioned, not substituted silently. D5 should add point-in-time checks, rolling-origin evaluation, regime/error analysis and uncertainty.
