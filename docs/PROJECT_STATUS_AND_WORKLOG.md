# Project Status and Work Log — IndiGo Profitability Intelligence

**Status date:** 7 November 2026  
**Repository:** [Bih aribabuu/Capstone-Project](https://github.com/Biharibabuu/Capstone-Project)  
**Branch:** main  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya  
**Project:** PGDM Business Analytics capstone

## 1. Project purpose

Build and evaluate an end-to-end analytics system that forecasts **IndiGo's next-quarter Profit After Tax (PAT) margin** using the airline's historical financial performance and selected economic/market indicators.

`PAT margin (%) = PAT / Revenue from Operations × 100`

The project forecasts company profitability, not IndiGo's stock price. The model must use only information available as of the forecast date. The HTML application is the user interface; the data pipeline, modelling, validation and evidence are the core analytics work.

## 2. Executive status

| Milestone | Deliverable | Status | What exists | Next gate |
|---|---|---|---|---|
| M1 | D1 — Project Charter | **Completed** | Charter, scope, objective, risks, team and project plan documented in GitHub | Keep the approved problem and target consistent; record any approved scope changes |
| M2 | D2 — Data Audit | **Completed** | Source register, collection tracker, data dictionary, feasibility audit, 30-Oct package manifest and D2 evaluation record | Reconcile the newest derived workbooks; freeze a dated, checksum-verified master dataset |
| M3 | D3 — Exploratory Data Analysis | **Completed** | Source-only EDA notebook, pre-specified hypotheses, review notes and analysis controls | Rebuild the financial target series, use fiscal quarters, rerun the EDA and freeze defensible features |
| M4 | D4 — Modelling | **In Progress — current active milestone** | Persistence baseline, Ridge and Random Forest comparisons, fixed chronological split, 12-run log, test predictions, metrics, tests and report | Keep D4-v1 immutable; use D5 to test robustness and point-in-time validity |
| M5 | D5 — Model Evaluation | **Planned** | Evaluation plan and handoff requirements | Rolling-origin backtest, publication-date controls, error/regime analysis and uncertainty |
| M6 | D6 — Deployment and Monitoring | **Todo** | FastAPI backend, HTML/CSS/JavaScript frontend, four market-data connectors, refresh/store code and integration guide | Integrate only the D5-approved forecast logic; test API, data freshness, security and monitoring |
| M7 | D7 — Final Communication | **Planned** | Final communication checklist and narrative requirements | Final report, model card, presentation, speaker notes, demo and limitations |

## 3. What has been completed

### M1 / D1 — Project framing
The project has a defined business problem, next-quarter PAT-margin target, one-quarter forecast horizon, scope, intended user and end-to-end product direction. The master plan and charter are in `docs/` and `milestones/M1_D1_Project_Charter/`.

### M2 / D2 — Data audit
The earlier 30 October 2026 package has a documented source register, collection tracker, data dictionary, data feasibility review, workbook manifest and quality notes. The working data categories are:
- IndiGo quarterly financials: Revenue, Net Income (GAAP) and EBITDA.
- USD/INR monthly exchange-rate observations.
- CPI inflation indicator.
- WPI inflation indicator.
- Dated Brent crude oil benchmark, daily and monthly.

The available package does **not** contain passenger count, passenger load factor, RPK or ASK. Do not claim that passenger-demand data is currently part of the model.

### M3 / D3 — EDA preparation and review
A source-only EDA notebook and review notes are in the repository. They specify hypotheses, data checks, distributions, relationships, seasonality tests, insight logging and modelling handoff controls. The notebook is not a final sign-off on the newest derived dataset; rerun it after the financial series and quarter key have been reconciled.

### M4 / D4 — D4-v1 modelling checkpoint
D4-v1 is a completed, documented experiment on a fixed input snapshot. It compares a persistence baseline against Ridge Regression and Random Forest.

**D4-v1 input lock**
- Input: `Final_Quarterly_Data(1).xlsx`
- Worksheet: `Final_Quarterly_Data`
- SHA-256: `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c`
- Source rows: 38; excluded rows: 2; supervised examples after one-quarter lag: 35.
- Split: train 21, validation 6, locked test 8.
- Period labels used: calendar-quarter labels supplied in the input, not yet converted to Indian fiscal-quarter labels.

| Model | Validation MAE (pp) | Validation RMSE (pp) | Decision |
|---|---:|---:|---|
| Persistence baseline | **12.18** | **13.92** | Selected |
| Best Ridge (alpha=100) | 42.62 | 43.94 | Not selected |
| Best Random Forest (depth=2, leaf=3) | 51.95 | 54.15 | Not selected |

Locked test persistence MAE = **11.53 percentage points** and RMSE = **14.20 percentage points**. Improvement versus the same persistence baseline = **0%**. No trained ML artifact was selected. The correct conclusion is that the tested ML candidates did not beat the baseline on this small sample; do not claim that machine learning improved the forecast.

The complete evidence is in `milestones/M4_D4_Modelling/`, including the experiment log, candidate comparison, metrics, test predictions, input manifest, environment file, notebook, source code, tests and four-page report.

## 4. Latest workbook review — 7 November 2026

Four workbooks were attached in the current working session and inspected. Their hashes and sheet dimensions are recorded below. The raw workbooks are exact copies of versions already committed to the repository; the two derived workbooks are new local versions and have not been committed.

| Current attachment | Size | SHA-256 | Sheets / dimensions | Handling decision |
|---|---:|---|---|---|
| `CP(6).xlsx` | 157,304 bytes | `208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e` | `IS` 59×42; `usd inr` 149×3; `cpi` 147×3; `wpi` 246×3; `co new` 3,000×3; `co new monthly` 148×3 | SHA-256 matches existing `data/raw/CP(4).xlsx`; no duplicate upload is needed |
| `CP Master Data(5).xlsx` | 71,747 bytes | `30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474` | Five market-data sheets plus `Financial source` 37×3; all sheet dimensions documented in the data review | SHA-256 matches existing `data/raw/CP Master Data(3).xlsx`; no duplicate upload is needed |
| `Final_Quarterly_Data(3).xlsx` | 99,836 bytes | `87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970` | `Final_Quarterly_Data` 39×12; `Calculation Audit` 197×13; `Data Quality Checks` 21×6 | New derived version; keep as a local review candidate until reconciled. It is **not** the D4-v1 input |
| `EDA ANALYSIS(4).xlsx` | 13,247 bytes | `0c2a79065faaee48cec6393f79ff330a98a9eb20c1add3e87e8a45dd7e1c0f46` | `Sheet1` 39×9 | New flat EDA version; not authoritative for targets and not committed |

### Findings in the latest derived files

1. `Final_Quarterly_Data(3).xlsx` contains 38 quarterly rows. The first two financial rows are labelled `Not available in source`, yet the PAT and EBITDA margin cells contain the same repeated values (11.379634% and 15.000185%). Those two numeric cells must not be treated as real target observations; preserve the source status and set them to missing in any approved modelling dataset.
2. The quarterly file uses `Quarter (Calendar)`. The capstone's final analytical key must use Indian fiscal quarters: Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar.
3. The `Financial source` tab in the master workbook remains a legacy derived series. Prior source reconciliation found it shifted by two quarters relative to the raw Bloomberg `IS` statement. Rebuild the financial outcome series from the raw `IS` period-end dates and line items; do not use this tab as the authoritative target source.
4. `EDA ANALYSIS(4).xlsx` repeats the same early financial margin values and does not include the financial-status field or the detailed calculation audit. It is a descriptive/flat export, not an approved modelling master.
5. The latest quarterly workbook's `Data Quality Checks` tab reports no duplicate source dates in several component series, but that does not resolve target alignment, the two unavailable quarters, source definitions, publication dates or the correct fiscal-quarter mapping.
6. `CP(6).xlsx` contains quarterly financial line items and estimates. Periods marked `Est` must never be treated as actual outcomes. Confirm every field's exact statement-line definition before finalising PAT and Revenue mapping.
7. `EUCRBRDT Index` represents Dated Brent crude. It is a benchmark proxy, not Indian ATF or IndiGo's realised fuel cost. The current workbooks do not establish an EBITDAR series; the provided financial field is EBITDA.

**Data decision:** do not replace the D4-v1 snapshot with `Final_Quarterly_Data(3).xlsx`. Create a separate reconciled dataset version, calculate its checksum, document all changes and run a new experiment version only after M2/M3 sign-off. Confirm Bloomberg/institutional redistribution rights before publishing any new workbook or derived values in this public repository.

## 5. Known project risks and controls

| Risk / issue | Required control |
|---|---|
| Financial source sheet shifted relative to raw statement | Rebuild from raw `IS`; reconcile period labels and dates row by row |
| First two target quarters have repeated margins but unavailable status | Mark target values missing; do not train or evaluate on them |
| Estimate versus actual periods | Retain status flags; only reported actuals can be historical target labels |
| Calendar versus Indian fiscal-quarter labels | Use `Q-MAR` / explicit fiscal-quarter key consistently |
| No historical release timestamps for all predictors | Collect publication/availability dates; otherwise flag point-in-time validity as unresolved |
| Small quarterly sample | Prefer parsimonious models; use rolling-origin splits; always compare with persistence |
| Brent is only a proxy | Label it clearly; do not claim it represents airline ATF expenditure |
| Bloomberg licensing | Keep data private unless redistribution rights clearly allow publication |
| Live inputs may be stale or failed | Show source timestamp/health; withhold predictions when critical features are missing or stale |

## 6. What must be done next — priority order

### Priority 1 — Complete the data reconciliation (M2)
1. Keep `CP(6).xlsx` and `CP Master Data(5).xlsx` as the unchanged raw references; they are byte-identical to the versions already stored in GitHub.
2. Read the raw `IS` sheet's quarter headers and `3 Months Ending` dates together. Extract actual financial observations only.
3. Verify Revenue and Net Income (GAAP) against IndiGo's reported financial-statement line items. Confirm whether the exported Net Income field is the correct PAT measure for this project.
4. Recalculate PAT margin and EBITDA margin from the verified numerator/denominator, rather than copying the legacy `Financial source` margin series.
5. Map period ends to Indian fiscal-quarter keys. Preserve observation dates and source/publication dates separately.
6. Aggregate monthly/daily market indicators to fiscal quarters using documented methods and completeness thresholds. Do not use incomplete future-quarter means in historical tests.
7. Reconcile every raw-to-master row, preserve original values, run duplicate/missing/outlier/unit checks and export a new dated master.
8. Create a manifest containing sheet inventory, data rows, date coverage, SHA-256, exclusions and a change log.

### Priority 2 — Rerun EDA (M3)
Rerun `notebooks/03_eda.ipynb` on the approved master, not on `EDA ANALYSIS(4).xlsx`. Recheck the pre-specified hypotheses, distributions, relationships, seasonal effects, anomalies and sample sizes. Keep association and causal language separate. Freeze only features that are both analytically defensible and available by the forecast cutoff.

### Priority 3 — Complete D5 evaluation
Preserve D4-v1 as the historical benchmark. Run expanding-window or rolling-origin validation on the approved fiscal-quarter dataset, compare persistence and candidate models on identical folds, review errors by regime (including COVID/exceptional loss quarters), quantify uncertainty and define when the forecast must be withheld. If ML still does not beat persistence, retain the baseline and state that result.

### Priority 4 — Integrate and validate deployment (M6)
Connect the D5-approved forecast logic to the existing FastAPI backend. Reuse the frontend and market connectors only after checking provider schemas, units, quotas, source timestamps, data rights and failure handling. Test normal, stale, missing and failed-source conditions. Do not call the scaffold a production deployment.

### Priority 5 — Final submission (M7)
Prepare the final report, model card, presentation, speaker notes, demo runbook, references and reproducibility record. Explain the actual baseline result, data limitations, model uncertainty, source rights and the difference between observed financial outcomes and forecasts.

## 7. Evidence and project records

Use these as the project source of truth:
- [Main repository README](../README.md)
- [Milestone register](../milestones/MILESTONE_REGISTER.csv)
- [Milestone index](../milestones/README.md)
- [Data source register](../data/source_register.csv)
- [Collection tracker](../data/collection_tracker.csv)
- [Data dictionary](../IndiGo_Data_Dictionary.csv)
- [30-Oct package manifest](Data_Package_Manifest.md)
- [D2 audit summary](D2_Data_Audit_Summary.md)
- [D3 review notes](../milestones/M3_D3_Exploratory_Data_Analysis/D3_Review_Notes.md)
- [D4-v1 experiment record](../milestones/M4_D4_Modelling/README.md)
- [Workflow and data governance](WORKFLOW_AND_DATA_GOVERNANCE.md)
- [Ongoing project context and working rules](PROJECT_CONTEXT_FOR_ONGOING_WORK.md)

Every future decision should be recorded with date, dataset/version, reason, impact, evidence and next action. Do not overwrite raw data, the D4-v1 input or past experiment results.


## Current milestone control (updated)

M1, M2 and M3 are marked Done. M4 / D4 is the only active milestone. M5, M6 and M7 remain Todo. The earlier D4-v1 experiment remains a completed sub-deliverable and historical benchmark; it does not mean the overall M4 milestone is closed.
