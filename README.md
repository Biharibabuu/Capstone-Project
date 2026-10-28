# IndiGo Profitability Intelligence System

**Integrated market-sensitive machine-learning model for forecasting IndiGo's business profitability**  
**Capstone:** PGDM Business Analytics · **Modules:** M1–M7 · **Deliverables:** D1–D7

## Project vision

Build an end-to-end forecasting product that combines historical IndiGo financial performance exported from Bloomberg Terminal with Bloomberg-sourced currency, inflation and oil-benchmark indicators. Public operational indicators may be added later if collected and validated. A Python data/ML backend will expose forecasts through an API; a single HTML/CSS/JavaScript application will let users inspect inputs, next-quarter PAT-margin forecasts, scenario results, model status and data health.

**The project predicts IndiGo business profitability, not its stock price.** Its primary target is next-quarter PAT margin. The model is the core technical deliverable; the HTML application is the user interface, not a substitute for ML experimentation and evaluation.

> This is an academic prototype using licensed Bloomberg extracts and aggregate financial/market data, plus public reference sources where used for validation. It is not commissioned by or endorsed by IndiGo and does not reveal unpublished actual results. Forecasts are estimates and must be presented with evaluation results and limitations.

## Current implementation status

The repository includes the project plan, D1 charter, D2 audit notes, data dictionary, validation utilities, HTML/CSS/JavaScript interface, FastAPI scaffold, and the reviewed D3 EDA notebook. The prediction API deliberately remains disabled until the financial inputs are reconciled and a model has been evaluated against a baseline.

**Current D3 review status:** the raw Bloomberg `IS` sheet and supplied master workbook do not align: the legacy `Financial source` margins in the master workbook are shifted by two quarters. The raw workbook also contains periods marked `Est`, which must not be labelled as actual outcomes. The notebook reconstructs margins from the raw statement, excludes estimates and aligns series to the project's Indian fiscal-quarter convention. The supplied flat EDA analysis workbook should be rebuilt before any model training.

**Next recommended step:** rebuild `Final_Quarterly_Data.xlsx` and the calculation audit from actual raw `IS` periods, verify financial definitions and publication dates, then rerun D3 before starting D4 baseline modelling. Local Bloomberg workbooks and output-rich reports are not stored in this public repo unless licence terms permit redistribution.

## Primary business question

Can historical IndiGo financial performance and Bloomberg-sourced currency, inflation and oil-benchmark indicators be combined to forecast next-quarter PAT margin, and does the selected model improve out-of-sample performance over a simple historical baseline?

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

## Data actually collected to date (Bloomberg Terminal exports)

The table below reflects the workbooks reviewed: `CP(3).xlsx` (raw Bloomberg export), `CP Master Data.xlsx` (exported/normalized market series and a legacy financial sheet), `Final_Quarterly_Data.xlsx` (quarterly aggregation and calculation audit), and `EDA ANALYSIS(1).xlsx` (flat EDA input). The Excel files are kept in authorized local storage; they are not committed here because Bloomberg data are licensed.

**Primary data provider:** [Bloomberg Terminal](<https://professional.bloomberg.com/products/bloomberg-terminal/>) and [Bloomberg DATA](<https://data.bloomberg.com/>). Bloomberg terminal exports do not provide a public, unauthenticated download URL for each licensed series, so the table records the exact Bloomberg security identifiers and field mnemonics. The public Bloomberg product links are source/access references; they are not direct links to the downloaded workbook. [Bloomberg's company profile for InterGlobe Aviation](<https://www.bloomberg.com/profile/company/INDIGO%3AIN>) identifies the company security. Independent official links in the last column are for cross-checking definitions/results only; they were not the source of the uploaded Bloomberg exports.

| Category | Data actually present in the uploaded workbooks | Bloomberg security / fields actually shown | Coverage, validation reference and status |
|---|---|---|---|
| Company financials | Quarterly Revenue, Net Income (GAAP) and EBITDA; PAT-margin and EBITDA-margin calculations derived from the exported rows. | **InterGlobe Aviation Ltd (`INDIGO IN`), BBG GAAP**. Bloomberg field IDs: Revenue `SALES_REV_TURN`; Net Income, GAAP `NET_INCOME`; EBITDA `EBITDA`. Workbook unit note: millions of INR except per-share items. | Raw statement dates run from 31 Mar 2017 to 30 Jun 2026 for actual periods; 30 Sep and 31 Dec 2026 are marked `Est` and must not be treated as actual results. Cross-check line-item definitions and reported figures against [IndiGo's official quarterly results](<https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html>). `NET_INCOME` is used provisionally as the PAT component; reconcile it and the Revenue field to the exact Indian financial-statement line items before modelling. The current export has EBITDA, **not EBITDAR**. |
| Currency | Monthly USD/INR observations; `PX_LAST` is used in the current quarterly-mean workbook, and `PX_BID` is also present in the raw export. | **`USDINR REGN Curncy`**, period `M`; fields `PX_LAST`, `PX_BID`. | Monthly data begin in Jan 2015. A row dated **30 Oct 2026** appears in the export, after the 28 Oct 2026 review date; exclude it from any as-of analysis. This is a monthly series, not the daily FX series described in the earlier candidate table. [RBI's reference-rate archive](<https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx>) is an independent comparison source, not the source of this workbook's values. |
| CPI inflation | Monthly CPI inflation indicator values from the Bloomberg export. | **`INFUTOTY Index`**, period `M`; field `PX_LAST`; workbook sheet `cpi`. | Observations run from Jan 2015 through Sep 2026. Confirm the exact Bloomberg instrument description and series definition in Terminal before using it as a named CPI measure. [MoSPI's CPI catalogue](<https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI>) is for definition/series cross-checking, not the source of the uploaded values. |
| WPI inflation | Monthly WPI inflation indicator values from the Bloomberg export. | **`INBGWPIY Index`**, period `M`; field `PX_LAST`; workbook sheet `wpi`. | Observations run from Oct 2006 through Sep 2026. Verify the precise Bloomberg series definition and its linkage to the WPI base-year revision before analysis. The [Office of the Economic Adviser WPI data page](<https://eaindustry.nic.in/download_data_2223.asp>) is an official cross-check, not the source of the uploaded values. |
| Oil / market benchmark | Daily and monthly USD oil-price observations. | **`EUCRBRDT Index`**, field `PX_LAST`; daily source sheet `co new`, monthly source sheet `co new monthly`; workbook records currency as USD. | Daily records run from 2 Jan 2015 through 19 Oct 2026; monthly records run from Jan 2015 through Sep 2026. This ticker identifies **Dated Brent crude**, not Indian ATF and not IndiGo's negotiated fuel cost. Keep it labelled as a Brent/oil benchmark proxy unless another series is collected. Bloomberg access reference: [Terminal](<https://professional.bloomberg.com/products/bloomberg-terminal/>) / [Bloomberg DATA](<https://data.bloomberg.com/>); a general series reference is also available via the [ECB financial-market data catalogue](https://data.ecb.europa.eu/data/datasets/FM). |
| Derived quarterly workbook | Quarterly means of USD/INR, CPI, WPI, daily Brent and monthly Brent; the workbook also has a `Calculation Audit` and `Data Quality Checks` sheet. PAT and EBITDA margins are included in `Final_Quarterly_Data.xlsx`. | Derived locally from the Bloomberg exports above; this is not a separate Bloomberg series. | The current derived workbook labels periods as `Quarter (Calendar)` and repeats the first PAT/EBITDA margin values despite those early periods being marked unavailable. Rebuild margins from the raw `IS` sheet, reconcile financial rows, and relabel quarter IDs to the Indian fiscal year before EDA/model training. |
| Operations / demand | Passenger counts, passenger load factor, RPK/ASK and capacity are **not present** in the currently supplied workbooks. | No Bloomberg operational series has been included in this data version. | Not collected yet. This is a possible later feature only; do not present it as an existing model input. Official [IndiGo investor relations](https://www.goindigo.in/information/investor-relations.html) and [DGCA](https://www.dgca.gov.in/) are candidate sources if we decide to add operational data. |
| Time / events | Year and calendar-quarter labels are derived in the current quarterly workbook. No event flags are present. | Project-derived fields, not Bloomberg event data. | Convert calendar-quarter labels to the project's Indian fiscal-quarter convention consistently (Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar). No exceptional-event flags have been collected. |

### Source and data-use notes

- The uploaded Bloomberg exports are the **actual data source** for the variables listed above. Do not describe the current data as downloaded from RBI, MoSPI, IndianOil, DGCA or IndiGo IR.
- Bloomberg public references: [Bloomberg Terminal](<https://professional.bloomberg.com/products/bloomberg-terminal/>), [Bloomberg DATA](<https://data.bloomberg.com/>), and [InterGlobe Aviation company profile](<https://www.bloomberg.com/profile/company/INDIGO%3AIN>). The exact security identifiers and field mnemonics above are required to reproduce the terminal extraction.
- Independent cross-check links: [IndiGo quarterly results](<https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html>), [RBI reference-rate archive](<https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx>), [MoSPI CPI catalogue](<https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI>), and [Office of the Economic Adviser WPI data](<https://eaindustry.nic.in/download_data_2223.asp>).
- Raw Bloomberg workbooks, values and output-filled Excel/HTML files stay in authorized local/private storage unless your Bloomberg/institutional licence explicitly permits redistribution. The public repository contains source identifiers, code and documentation only.
- This dataset version is **not ready for modelling** until the financial source alignment, actual-vs-estimate status, fiscal-quarter labels, source publication-date availability and instrument definitions have been checked.


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

### Dataset build status and next implementation task

The existing `src/build_master_dataset.py` and original CSV templates were designed around the earlier normalized-source plan (including daily FX and ATF). They are **not yet mapped to the current Bloomberg export**, which contains monthly USD/INR, CPI inflation, WPI inflation, and daily/monthly Dated Brent. Do not place the Excel workbooks in `data/raw/` and expect the current builder to read them directly.

The upcoming source-mapping step must convert the local workbook sheets into normalized CSVs for:
- financial quarterly values rebuilt from raw `IS` rows;
- monthly USD/INR;
- monthly CPI inflation;
- monthly WPI inflation;
- daily and monthly Dated Brent;
- optional operations data, once collected.

For the current source IDs, file paths, units and known gaps, see [the actual-source register](data/source_register.csv) and [collection tracker](data/collection_tracker.csv). After the import mapping and fiscal-quarter corrections are implemented, run the master builder and review missingness, publication-date eligibility and leakage checks before modelling.

The script creates one row per **target quarter**, with the forecast cutoff on the last day before that quarter begins. It selects only inputs whose observation period is before the target quarter and whose publication date is no later than the cutoff. The target quarter's own revenue, PAT and PAT margin are labels only.

The public source templates are headers only. Raw Bloomberg workbooks and working master files are maintained locally in the ignored data folders. The master-data builder and model have not yet been run on a reconciled dataset; do not treat earlier generated quarterly workbooks as training-ready.

## D2 — Data audit (data-v1.0)

The D2 audit report and its three-page datasheet document the audit of the Bloomberg raw export and the supplied master workbook.

- **Audit summary:** [D2 Data Audit Summary](docs/D2_Data_Audit_Summary.md)
- **Required PDF filename:** `reports/ANCP_T##_D2_v1.pdf` (11 pages total: up to 8 audit-report pages plus 3 datasheet pages).
- **Provisional coverage:** the raw `IS` export contains actual quarters from 2017-03-31 through 2026-06-30 plus later rows marked as estimates. The earlier 33-row modelling count is not approved for training because the generated master target sheet was misaligned; rebuild and recalculate it from raw actual financials first.
- **Critical finding:** the supplied master workbook's `Financial source` sheet is shifted by two quarters relative to the raw Bloomberg `IS` sheet. The analytical financial outcomes must be rebuilt from raw `IS` values; do not use the misaligned financial source sheet for modelling.
- **CPI date check:** the latest raw `CP(3).xlsx` sheet has monthly dates through 2026-09-30; the earlier malformed-date concern was not reproduced in this version. Verify any dates in the derived quarterly file against the raw series and do not manually alter source dates.
- **Data governance:** Bloomberg source files are proprietary. Do not publish raw exports or derived data unless institutional licence terms permit it. Keep raw exports in authorised private storage.
- **Feature timing:** use only information available at the forecast cutoff; the next-quarter PAT margin is a target, never a predictor.

Keep licensed Bloomberg exports and data-derived workbook values in authorized local/private storage. The public repository should contain code, schemas, source metadata and documentation only unless the applicable licence explicitly permits redistribution. Do not use the earlier generated master dataset until it has been rebuilt from the raw `IS` sheet.


## D3 — Exploratory Data Analysis (reviewed source notebook)

- **Notebook:** [`notebooks/03_eda.ipynb`](notebooks/03_eda.ipynb). The source-only notebook includes pre-specified hypotheses, source and cleaned-data quality checks, distributions, trends, fiscal-quarter segmentation, statistical tests, an insight log and modelling recommendations. Outputs are cleared in the public copy to avoid republishing Bloomberg-derived values and figures.
- **Review note:** the supplied master workbook's `Financial source` sheet is shifted by two quarters relative to the raw Bloomberg `IS` sheet. The notebook reconstructs quarterly PAT and EBITDA margins from the raw statement, excludes records marked `Est`, and aligns market indicators to Indian fiscal quarters. The separate flat EDA analysis workbook should be rebuilt rather than used as the modelling master.
- **Next step:** rebuild the final quarterly master and calculation audit from actual raw financials, rerun EDA locally, then start D4 baseline modelling. No forecast model has been trained or validated yet.
- **Data governance:** raw Bloomberg workbooks, output-rich notebook/HTML exports and derived data tables are not committed to the public repo unless the applicable licence permits redistribution. Local input paths are documented in [`notebooks/README.md`](notebooks/README.md) and [the D3 status note](reports/D3_eda/README.md).
