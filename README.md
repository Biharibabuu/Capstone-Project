# IndiGo Profitability Intelligence System

**Integrated market-sensitive machine-learning model for forecasting IndiGo's business profitability**  
**Capstone:** PGDM Business Analytics · **Modules:** M1–M7 · **Deliverables:** D1–D7

## Project vision

Build an end-to-end forecasting product that combines historical IndiGo financial performance with selected public market, macroeconomic and airline operating indicators. A Python data/ML backend will expose forecasts through an API; a single HTML/CSS/JavaScript application will let users inspect inputs, next-quarter PAT-margin forecasts, scenario results, model status and data health.

**The project predicts IndiGo business profitability, not its stock price.** Its primary target is next-quarter PAT margin. The model is the core technical deliverable; the HTML application is the user interface, not a substitute for ML experimentation and evaluation.

> This is an academic prototype using public and aggregate information. It is not commissioned by or endorsed by IndiGo and does not reveal unpublished actual results. Forecasts are estimates and must be presented with evaluation results and limitations.

## Current implementation status

The repository includes the project plan, D1 charter, D2 audit notes, data dictionary, validation utilities, HTML/CSS/JavaScript interface, FastAPI scaffold, and the reviewed D3 EDA notebook. The prediction API deliberately remains disabled until the financial inputs are reconciled and a model has been evaluated against a baseline.

**Current D3 review status:** the raw Bloomberg `IS` sheet and supplied master workbook do not align: the legacy `Financial source` margins in the master workbook are shifted by two quarters. The raw workbook also contains periods marked `Est`, which must not be labelled as actual outcomes. The notebook reconstructs margins from the raw statement, excludes estimates and aligns series to the project's Indian fiscal-quarter convention. The supplied flat EDA analysis workbook should be rebuilt before any model training.

**Next recommended step:** rebuild `Final_Quarterly_Data.xlsx` and the calculation audit from actual raw `IS` periods, verify financial definitions and publication dates, then rerun D3 before starting D4 baseline modelling. Local Bloomberg workbooks and output-rich reports are not stored in this public repo unless licence terms permit redistribution.

## Primary business question

Can historical IndiGo performance and public market, macroeconomic and operating indicators be combined to forecast next-quarter PAT margin, and does the selected model improve out-of-sample performance over a simple historical baseline?

**Primary target:**  
PAT margin (%) = PAT / Revenue from Operations × 100

**Forecast horizon:** one quarter ahead. The pipeline may refresh the latest valid inputs, but it cannot know an unpublished current-quarter profit.

## Product capabilities planned

- Import or refresh latest available financial, market and operating information.
- Validate source dates, units, missing values, data freshness and feature availability at forecast time.
- Produce a next-quarter PAT-margin forecast using the same preprocessing as model training.
- Compare models using chronological validation and a simple baseline.
- Show inputs used, key contributing factors and reliability/uncertainty information where supported by evaluation.
- Run low-cost/favourable, base and high-cost/adverse scenarios where assumptions are defensible.
- Store forecast metadata so predictions can be compared with actual results once published.
- Monitor input quality, freshness, feature drift, prediction errors and model version.

## Planned technical architecture

| Layer | Responsibility | Candidate technology |
|---|---|---|
| Data pipeline | Collect/import, clean, align, document and store observations | Python, pandas, CSV/Parquet/SQLite |
| Feature engineering | Margins, lags, changes, rolling summaries, seasonality and justified interactions | pandas, NumPy |
| ML engine | Baseline, candidate training, time-ordered validation and prediction | scikit-learn |
| API | Validate requests and expose prediction/scenario functions | FastAPI or Flask |
| Frontend | Forecast overview, market inputs, scenarios, historical performance and model/data status | HTML, CSS, JavaScript |
| Monitoring | Data health, prediction log, model version, errors and retraining triggers | Python logs / stored metrics |

## Candidate data

The final feature list will be frozen only after the data-feasibility audit and EDA. Candidate variables are not guaranteed to be included.

| Category | Candidate fields | Candidate source |
|---|---|---|
| Company financials | Revenue from operations, PAT, PAT margin, EBITDAR margin where consistently reported | [IndiGo quarterly results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html) |
| Fuel / market | ATF price or a verified fuel-price proxy | [IndianOil historical domestic ATF prices](https://www.iocl.com/atf-domestic-airlines); PPAC for broader cross-checks |
| Currency | USD/INR level, changes or lags | [RBI DBIE](https://data.rbi.org.in/DBIE/) |
| Macroeconomy | CPI inflation / quarterly summary | [MoSPI](https://www.mospi.gov.in/) |
| Operations / demand | Passengers carried, passenger load factor when comparable | [IndiGo investor relations](https://www.goindigo.in/information/investor-relations.html), [DGCA](https://www.dgca.gov.in/) |
| Time / events | Fiscal-quarter indicators; exceptional-event flags only if reliable | Documented derived fields |

Expected historical coverage and usable row count are **to be confirmed during D2**. Record source URL, publication/retrieval date, period, units, definitions and revisions. Preserve raw data unchanged and keep raw and processed data separate. Do not publish source data unless redistribution terms allow it; link to the source if rights are unclear. No passenger-level personal data is required.

## Modelling and evaluation

1. Establish a simple historical baseline.
2. Test Ridge / Elastic Net as transparent regularized candidates.
3. Test Random Forest / Gradient Boosting only if sample size and feasibility justify them.
4. Use chronological train/validation/test splits and rolling-origin backtesting where feasible; do not randomly shuffle quarters.
5. Fit preprocessing only on data available within each training window.
6. Compare MAE and RMSE; directional accuracy may be added if defined consistently.
7. Select the most defensible model based on out-of-sample performance, stability, interpretability and business usefulness—not complexity.
8. If ML does not beat the baseline, report that honestly and retain the baseline.

Every feature must pass the **forecast-date availability rule**. Latest-market refresh applies to future use only; it must not leak future values into historical evaluation. Scenario analysis is sensitivity testing, not evidence of causal effects.

## Academic deliverables (M1–M7 / D1–D7)

| Module | Deliverable | Expected evidence |
|---|---|---|
| M1 | D1 — Project charter | Problem, decision-maker, analytics question, metrics, scope, data plan, risks, roles, meeting log, responsibility matrix |
| M2 | D2 — Data audit | Source register, coverage, definitions, missingness, access/privacy notes, cleaned dataset, data dictionary |
| M3 | D3 — EDA | Descriptive analysis, relationships, hypotheses, anomalies, seasonality and insights |
| M4 | D4 — Modelling checkpoint | Baseline, candidate models, experiments, tuning decisions and experiment log |
| M5 | D5 — Evaluation memo | Chronological validation, errors, leakage checks, uncertainty and limitations |
| M6 | D6 — Deployment and monitoring | HTML/API prototype or demo, data refresh, data health, drift, retraining and maintenance |
| M7 | D7 — Communication | Final report, model card, presentation and technical/business Q&A readiness |

## 12-week roadmap

| Week | Focus | Gate / output |
|---|---|---|
| 1 | Scope and feasibility audit | Confirm target, data coverage, source register, repository; decide whether comparable data are sufficient |
| 2 | Historical data collection | Raw datasets and source register |
| 3 | Cleaning and alignment | Master dataset, PAT margin and data dictionary |
| 4 | EDA and hypotheses | EDA notebook, insights, unusual-period review and initial feature list |
| 5 | Baseline | Baseline forecast, chronological evaluation setup, MAE/RMSE |
| 6 | Candidate ML models | Model comparison and experiment log |
| 7 | Evaluation | Unseen-quarter evaluation, leakage and error review |
| 8 | Prediction engine | Selected/versioned model, preprocessing and scenarios |
| 9 | HTML and API | Working local application |
| 10 | Market-data refresh | Validated refresh and prediction workflow |
| 11 | Deployment and monitoring | Input tests, monitoring plan and retraining triggers |
| 12 | Final communication | Final report, model card, presentation and demo |

## Main risks

| Risk | Mitigation |
|---|---|
| Small quarterly sample | Simple baseline, parsimonious models and time-based validation |
| Inconsistent data definitions | Source register, dictionary, unit reconciliation and documented transforms |
| Future-information leakage | Publication-date tracking and chronological evaluation |
| API/source access limitations | Verified file-import fallback and documented refresh status |
| Exceptional events or regime changes | Robustness checks, event flags only where reliable, clear limitations |
| ML underperforms baseline | Keep baseline as formal comparator; simplify if necessary |
| Integration delays | Freeze the evaluated model before UI integration; build in stages |

## Repository map

- [Master project plan](docs/Master_Project_Plan.md) — integrated project vision and 12-week work plan.
- [D1 project charter](docs/Project_Charter.md) — charter, milestones, role matrix and meeting log.
- [Data dictionary](IndiGo_Data_Dictionary.csv) — candidate variables and preparation controls.
- frontend/ — HTML/CSS/JS interface.
- backend/ — API routes and request schemas.
- src/ — data pipeline, features, training, prediction and scenarios.
- notebooks/ — data audit, EDA, baseline, experiments and evaluation.
- data/ — raw and processed data (respect source terms; do not commit sensitive or unlicensed data).
- models/, tests/, reports/ — model artifacts, tests and project outputs.

See the [D1 charter](docs/Project_Charter.md) and [full plan](docs/Master_Project_Plan.md) before implementation.


## Phase 1 — data collection and dataset build

- [Data collection plan](docs/Phase1_Data_Collection_Plan.md) — source-by-source steps, release-date rules, quarter alignment, cleaning and small-sample policy.
- [Master dataset schema](docs/Master_Dataset_Schema.md) — exact output columns, feature/label separation and timing rules.
- [Initial source register](data/source_register.csv) · [Blank source register template](data/templates/source_register.csv).
- [Financials template](data/templates/financial_quarterly.csv).
- [Operations template](data/templates/operational_monthly.csv).
- [ATF template](data/templates/atf_monthly.csv).
- [USD/INR template](data/templates/usd_inr_daily.csv).
- [CPI template](data/templates/cpi_monthly.csv).
- [Phase 1 collection plan](docs/Phase1_Data_Collection_Plan.md).
- [Master dataset schema](docs/Master_Dataset_Schema.md).
- [Dataset builder](src/build_master_dataset.py) and [point-in-time tests](tests/test_master_dataset_builder.py).

### How to build the dataset

1. Copy the five CSV templates into `data/raw/` using the same filenames.
2. Fill them with normalized source records and actual publication dates. Do not invent dates; record source URLs.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run `python -m src.build_master_dataset --input-dir data/raw --output-dir data/processed`.
5. Review `data/processed/data_quality_report.csv` and the missingness/leakage checks before starting EDA.

The script creates one row per **target quarter**, with the forecast cutoff on the last day before that quarter begins. It selects only inputs whose observation period is before the target quarter and whose publication date is no later than the cutoff. The target quarter's own revenue, PAT and PAT margin are labels only.

The public source templates are headers only. Raw Bloomberg workbooks and working master files are maintained locally in the ignored data folders. The master-data builder and model have not yet been run on a reconciled dataset; do not treat earlier generated quarterly workbooks as training-ready.

## D2 — Data audit (data-v1.0)

The D2 audit report and its three-page datasheet document the audit of the Bloomberg raw export and the supplied master workbook.

- **Audit summary:** [D2 Data Audit Summary](docs/D2_Data_Audit_Summary.md)
- **Required PDF filename:** `reports/ANCP_T##_D2_v1.pdf` (11 pages total: up to 8 audit-report pages plus 3 datasheet pages).
- **Provisional coverage:** the raw `IS` export contains actual quarters from 2017-03-31 through 2026-06-30 plus later rows marked as estimates. The earlier 33-row modelling count is not approved for training because the generated master target sheet was misaligned; rebuild and recalculate it from raw actual financials first.
- **Critical finding:** the supplied master workbook's `Financial source` sheet is shifted by two quarters relative to the raw Bloomberg `IS` sheet. The analytical financial outcomes must be rebuilt from raw `IS` values; do not use the misaligned financial source sheet for modelling.
- **CPI date check:** the supplied master still has a non-month-end observation date around August 2026; verify it against the source export before treating the issue as resolved.
- **Data governance:** Bloomberg source files are proprietary. Do not publish raw exports or derived data unless institutional licence terms permit it. Keep raw exports in authorised private storage.
- **Feature timing:** use only information available at the forecast cutoff; the next-quarter PAT margin is a target, never a predictor.

Keep licensed Bloomberg exports and data-derived workbook values in authorized local/private storage. The public repository should contain code, schemas, source metadata and documentation only unless the applicable licence explicitly permits redistribution. Do not use the earlier generated master dataset until it has been rebuilt from the raw `IS` sheet.


## D3 — Exploratory Data Analysis (reviewed source notebook)

- **Notebook:** [`notebooks/03_eda.ipynb`](notebooks/03_eda.ipynb). The source-only notebook includes pre-specified hypotheses, source and cleaned-data quality checks, distributions, trends, fiscal-quarter segmentation, statistical tests, an insight log and modelling recommendations. Outputs are cleared in the public copy to avoid republishing Bloomberg-derived values and figures.
- **Review note:** the supplied master workbook's `Financial source` sheet is shifted by two quarters relative to the raw Bloomberg `IS` sheet. The notebook reconstructs quarterly PAT and EBITDA margins from the raw statement, excludes records marked `Est`, and aligns market indicators to Indian fiscal quarters. The separate flat EDA analysis workbook should be rebuilt rather than used as the modelling master.
- **Next step:** rebuild the final quarterly master and calculation audit from actual raw financials, rerun EDA locally, then start D4 baseline modelling. No forecast model has been trained or validated yet.
- **Data governance:** raw Bloomberg workbooks, output-rich notebook/HTML exports and derived data tables are not committed to the public repo unless the applicable licence permits redistribution. Local input paths are documented in [`notebooks/README.md`](notebooks/README.md) and [the D3 status note](reports/D3_eda/README.md).
