# Project Status and Work Log — IndiGo Profitability Intelligence

**Status date:** 7 November 2026  
**Repository:** Biharibabuu/Capstone-Project  
**Branch:** main  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya  
**Current active milestone:** M4 / D4 — Modelling

## 1. Project purpose

Develop an end-to-end analytics system to forecast IndiGo's next-quarter **EBITDA margin** using historical company financial data and selected macroeconomic/market indicators. This is profitability forecasting, not stock-price prediction. The HTML application is the interface; data governance, modelling, chronological evaluation and reproducibility are the core analytical work.

**Target:** EBITDA margin (%) = EBITDA / Revenue from Operations × 100, subject to the documented source-line reconciliation and approved denominator.

## 2. Executive status

| Milestone | Deliverable | Status | Evidence and next gate |
|---|---|---|---|
| M1 | D1 Project Charter | Done | Business problem, scope, team, risks and delivery plan documented; maintain formal change control |
| M2 | D2 Data Audit | Done | Source register, collection tracker, data dictionary, workbook hashes, data package and audit limitations documented |
| M3 | D3 EDA | Done | EBITDA-only panel and analysis handoff stored under M3; latest output-rich notebook still requires repository publication/correction |
| M4 | D4 Modelling | **In Progress** | Active work: build reproducible EBITDA-margin baseline/candidate models; legacy PAT D4-v1 is historical evidence only |
| M5 | D5 Model Evaluation | Todo | Begin after M4 model candidates and data protocol are stable; run rolling-origin evaluation |
| M6 | D6 Deployment and Monitoring | Todo | Integrate only a D5-approved model; scaffold is groundwork, not completed deployment |
| M7 | D7 Final Communication | Todo | Final report, model card, presentation and demo after D5/D6 |

## 3. Data package and milestone ownership

| Milestone | Data / artifacts |
|---|---|
| M1 | No analytical source dataset; charter and project baseline only |
| M2 | Raw Bloomberg source workbooks, quarterly data snapshot, source register, collection tracker, data dictionary, checksums and audit reports |
| M3 | `data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv` — 38-quarter EBITDA-only panel, plus EDA notebook/review evidence |
| M4 | Its own versioned quarterly modelling input snapshot, model-ready features, splits, predictions and manifests; source links back to M2/M3 |
| M5 | Frozen M4 validation/test dataset vintage, evaluation predictions, backtest outputs and error analysis |
| M6 | Approved M5 model artifact, validated feature schema and live refresh inputs; no duplicate training dataset |
| M7 | Final approved datasets/results referenced by version/checksum; no new ungoverned data source |

## 4. Modelling evidence and separation from legacy experiment

The archived D4-v1 experiment is a PAT-margin exercise. It selected a persistence baseline because Ridge and Random Forest did not beat it on validation. Its locked-test MAE/RMSE were 11.53/14.20 percentage points. These results must not be described as EBITDA-model performance. A separate current EBITDA-target M4 experiment must be completed and evaluated.

## 5. Data governance

- Raw Bloomberg workbook copies are stored under M2's milestone data folder and have canonical source lineage.
- The same workbook bytes may be linked across milestone documentation; do not create competing modified copies.
- M3's EDA panel has only the EBITDA outcome and five market/currency predictor series.
- M4's model data must be versioned, checksummed and tied to the exact source snapshot and transformations.
- New data or workbook versions must be compared to existing versions, checked for financial alignment/actual-vs-estimate status, and cleared for redistribution before publication.
- Keep observation dates separate from publication/availability dates.
- Do not commit credentials, API keys or other secrets.

## 6. End-to-end workflow

M2 source audit → M3 EBITDA EDA → M4 model development and chronological validation → M5 rolling-origin and robustness evaluation → M6 approved-model deployment and monitoring → M7 final communication.

## 7. Current M4 next actions

1. Confirm target calculation and revenue denominator from source line items.
2. Validate dates, missing periods and fiscal-quarter labels.
3. Build one-quarter-ahead rows without bridging gaps.
4. Establish a persistence baseline and appropriate candidate models.
5. Use chronological validation and leakage-safe preprocessing.
6. Save the experiment log, metrics, predictions, residuals, tests, environment and a concise report.
