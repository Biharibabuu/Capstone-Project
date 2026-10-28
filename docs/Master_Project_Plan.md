# Master Project Plan — IndiGo Profitability Intelligence System

**Project subtitle:** Integrated market-sensitive machine-learning model for forecasting IndiGo's profitability  
**Course alignment:** ANCP Modules M1–M7 and Deliverables D1–D7  
**Implementation horizon:** 12 weeks  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya

## 1. Project background and final direction

The project began as an IndiGo macroeconomic profitability-forecasting capstone and has been refined into an end-to-end analytics product combining historical company performance with current/latest-available market information.

The project forecasts **IndiGo business profitability, not its stock price**. The primary output remains next-quarter PAT margin. The ML prediction engine is the main technical deliverable. The HTML application is the single user interface; Python handles data preparation, prediction, scenarios and validation.

## Current implementation status — 28 October 2026

D1 documentation and the D2 audit notes are in the repository. The raw Bloomberg workbook, the market-indicator master workbook, a quarterly output workbook and a D3 EDA HTML export have been received for review, but licensed workbooks and output-rich exports are kept in local/private storage rather than committed to the public repository.

The reviewed D3 source notebook is available at [`notebooks/03_eda.ipynb`](../notebooks/03_eda.ipynb). It reconstructs PAT and EBITDA margins from raw Bloomberg `IS` inputs, excludes rows marked `Est`, uses the project's Indian fiscal-quarter convention (`Q-MAR`) and checks the legacy master sheet against the raw statement. The public notebook has no stored execution outputs.

**Important data-reconciliation gate before D4:**
- The legacy `Financial source` sheet in the master workbook is shifted by two quarters relative to raw `IS` financial values.
- The supplied flat EDA output repeats margins in two early quarters that are marked unavailable in the separate quarterly dataset; rebuild it from raw financial outcomes.
- Historical rows marked as estimates must not be treated as actual labels.
- The oil benchmark's definition must be verified before it is described as Indian ATF.
- The latest raw `CP(3).xlsx` CPI series runs through 2026-09-30; the earlier malformed-date issue was not reproduced in that version. Compare derived dates with the raw observations.
- The previously reported 33-row training count is provisional and must not be used until the master is rebuilt and the audit rerun.

**Next gate:** rebuild and verify the target-quarter master from actual raw financial periods, reconcile CPI and publication timing, rerun D3 locally, then establish the D4 baseline and chronological evaluation. No forecasting model has been trained or validated yet.


## 2. Final project vision

The system will combine financial, market and operating indicators, transform them into forecasting features, run a trained ML model and return a next-quarter profitability forecast with supporting context.

### Planned capabilities

- Predict next-quarter PAT margin.
- Use only information available at each forecast date.
- Refresh forecasts when new valid market information becomes available.
- Show the input conditions used for the forecast.
- Present uncertainty/reliability information where supported by evaluation.
- Show important contributing factors without claiming causal certainty.
- Support low-cost/favourable, base and high-cost/adverse scenarios.
- Track historical predictions against actual results once those results are published.

### Boundaries

- Not a stock-price prediction system.
- Not a dashboard-only project.
- Not a real-time measurement of unpublished profit.
- Not dependent on using the most complex algorithm.
- No claim that ML is superior unless evaluation against a baseline supports it.

## 3. Business problem and decision context

Profitability can be affected by interacting factors such as fuel costs, currency movements, inflation, passenger demand and operating performance. The business need is to translate the latest available information into an evidence-based view of future profitability.

**Problem statement:** Develop and evaluate a machine-learning model that uses historical IndiGo financial performance and publicly available market and operating indicators to forecast the company's next-quarter PAT margin, and determine whether the selected model improves predictive performance over a simple historical baseline on unseen quarters.

**Decision-maker:** Business/finance decision-makers, analysts and project stakeholders who need an evidence-based view of future profitability and risk.

**Primary analytics question:** Can public macroeconomic, market and airline operating indicators, together with historical IndiGo performance, be combined in a machine-learning model to forecast next-quarter PAT margin?

**Target:**

PAT Margin (%) = Profit After Tax / Revenue from Operations × 100

PAT margin is the primary output. EBITDAR margin is a secondary operating-performance indicator where data definitions are consistent.

**Forecast horizon:** One quarter ahead.

**Forecast boundary:** The system can refresh current/latest-available market data, but it cannot know unpublished actual current-quarter profit. Predictions are forecasts based on information available at the relevant forecast date.

## 4. Stakeholders

| Stakeholder | Role / interest | Expected output or impact |
|---|---|---|
| Decision-maker / business user | Uses forecast for planning and risk assessment | Forecast, scenarios, reliability information and limitations |
| Project team | Builds, validates and documents the system | Data, code, experiments and documentation |
| Public data suppliers | Provide financial, macroeconomic and operating information | Definitions, publication dates, units and access conditions |
| Faculty / evaluator | Assesses analytical rigor and course outcomes | Charter, evidence, evaluation, report and presentation |
| Prototype users | Interact with the HTML application | Validated inputs and prediction output |

## 5. Integrated system architecture

| Layer | Responsibility | Candidate technology |
|---|---|---|
| Data | Collect/import, clean, align and store historical/latest observations | Python, pandas, CSV/Parquet/SQLite |
| Features | Create margins, changes, lags, rolling summaries, seasonality and justified interactions | pandas, NumPy |
| ML engine | Train, compare, validate and run the selected model | scikit-learn |
| API | Validate requests and expose prediction functions | FastAPI or Flask |
| Frontend | Single interface for forecast, inputs, scenarios and model status | HTML, CSS, JavaScript |
| Monitoring | Track data quality, predictions, model version and performance | Python logs / stored metrics |

### End-to-end flow

1. Retrieve or import latest valid data.
2. Validate dates, units, missingness and freshness.
3. Align indicators to the forecast period.
4. Generate the feature vector using the same preprocessing as training.
5. Run the selected model.
6. Return the PAT-margin forecast and supporting metrics.
7. Run scenarios where requested.
8. Store prediction metadata for later comparison with actual results.
9. Monitor performance and retraining conditions.

## 6. Data architecture and actual collected inputs

The currently supplied working files contain Bloomberg Terminal exports; public official-source pages listed here are for validation/reference, not the source of the current data export. The final predictor list remains provisional pending financial reconciliation and point-in-time availability checks.

| Category | Data present now | Bloomberg security / fields | Frequency / coverage and control |
|---|---|---|---|
| Company financials | Revenue, Net Income (GAAP), EBITDA; derived PAT and EBITDA margins | InterGlobe Aviation Ltd (`INDIGO IN`), BBG GAAP; `SALES_REV_TURN`, `NET_INCOME`, `EBITDA` | Quarterly actuals from 31 Mar 2017 to 30 Jun 2026. Later 30 Sep/31 Dec 2026 periods are estimates and must be excluded from actual labels. Confirm Revenue/PAT line-item equivalence. |
| USD/INR | Monthly last price; bid also present in raw export | `USDINR REGN Curncy`; `PX_LAST`, `PX_BID` | Monthly, Jan 2015 onward. Exclude the 30 Oct 2026 record from an analysis dated 28 Oct 2026. |
| CPI inflation | CPI inflation indicator | `INFUTOTY Index`; `PX_LAST` | Monthly, Jan 2015–Sep 2026. Confirm exact Terminal instrument description. |
| WPI inflation | WPI inflation indicator | `INBGWPIY Index`; `PX_LAST` | Monthly, Oct 2006–Sep 2026. Verify exact definition/base-series history. |
| Oil benchmark | Dated Brent crude proxy, not aviation fuel | `EUCRBRDT Index`; `PX_LAST`; raw daily and monthly sheets | Daily, 2 Jan 2015–19 Oct 2026; monthly, Jan 2015–Sep 2026. Do not label as Indian ATF or IndiGo's realised fuel cost. |
| Quarterly derived fields | Quarterly means of FX, CPI, WPI, daily Brent and monthly Brent; margin calculations | Derived from current local workbooks and the Bloomberg fields above | Current output labels use calendar quarters and the first two financial margins are not reconciled to raw `IS`; rebuild before model training. |
| Operations / demand | Passenger counts, load factor and RPK/ASK | Not present in current files | Not collected yet; may be added later if definitions and historical availability can be verified. |

**Source references:** [Bloomberg Terminal](<https://professional.bloomberg.com/products/bloomberg-terminal/>), [Bloomberg DATA](<https://data.bloomberg.com/>), [Bloomberg's InterGlobe Aviation profile](<https://www.bloomberg.com/profile/company/INDIGO%3AIN>). These vendor/product links are access and source references, not public downloads of the licensed series. Cross-check financial disclosures at [IndiGo IR](<https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html>), FX definitions against [RBI](<https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx>), CPI against [MoSPI](<https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI>), and WPI against [the Office of the Economic Adviser](<https://eaindustry.nic.in/download_data_2223.asp>).

### Data quality gate before feature selection

- Rebuild Revenue, Net Income (GAAP) and EBITDA margins from the raw `IS` rows. The legacy `Financial source` sheet in the master workbook is shifted by two quarters.
- Exclude rows marked `Est` from observed financial outcomes and historical evaluation.
- Confirm the Bloomberg Revenue and Net Income field definitions against official statement line items; current `NET_INCOME` is only a provisional PAT component.
- Treat `EUCRBRDT Index` as Dated Brent crude, not ATF.
- The CPI observation series in the latest raw workbook runs through 30 Sep 2026; the earlier alleged malformed date was not reproduced in this latest raw sheet. Check the derived workbook's dates against the raw dated series instead of editing source dates manually.
- Rebuild quarter labels to Indian fiscal quarters and redo the calculation audit. No model has been trained or validated on a reconciled master yet.

[Data feasibility audit](Data_Feasibility_Audit.md) · [D2 audit summary](D2_Data_Audit_Summary.md) · [D3 EDA notebook](../notebooks/03_eda.ipynb) · [D3 review notes](../reports/D3_eda/README.md)


## 7. Machine-learning strategy

Models will be compared using time-ordered validation and a simple baseline. Complexity is not a substitute for evidence.

| Model stage | Purpose |
|---|---|
| Simple historical baseline | Establish minimum forecasting performance for candidate ML models to beat |
| Ridge / Elastic Net | Transparent regularized benchmark suited to a potentially small quarterly dataset |
| Random Forest / Gradient Boosting candidate | Test whether nonlinear relationships and interactions add predictive value |
| Final model | Select based on out-of-sample performance, stability, interpretability and feasibility |

### Evaluation

- Use chronological train/validation/test splits.
- Use rolling-origin backtesting where feasible.
- Fit preprocessing only on the data permitted within each training window.
- Check publication-date availability for every feature.
- Compare mean absolute error (MAE) and root mean squared error (RMSE).
- Directional accuracy may be included if it is defined consistently.
- Select the model based on defensible out-of-sample performance and business usefulness.
- If ML does not outperform the baseline, document the result rather than claiming superiority.

MAE is the average absolute PAT-margin forecast error in percentage points. RMSE penalises larger errors more strongly. Baseline improvement is the evidence that ML adds value beyond the selected simple benchmark.

## 8. Current-market integration

The planned current-market function is a refreshable forecasting pipeline. When new information becomes available, valid inputs can update the forecast.

1. Update latest fuel/market inputs where reliable.
2. Update USD/INR and selected macroeconomic indicators where available.
3. Update operating indicators when new company disclosures are published.
4. Validate freshness and completeness.
5. Recalculate the feature vector using the training-compatible feature process.
6. Generate a revised next-quarter profitability forecast.

The system cannot observe unpublished actual profit, guarantee causal effects from market movements or use future data during historical evaluation. If automated APIs are unavailable, use a documented and validated file-import path.

## 9. HTML application

The HTML application is the single user-facing interface. Python remains responsible for data and ML processing.

| Interface section | Planned function |
|---|---|
| Overview | Current forecast and model status |
| Market Inputs | Latest validated variables and timestamps |
| Profitability Forecast | Next-quarter PAT margin and evaluation-supported reliability information |
| Drivers | Important inputs associated with the prediction |
| Scenario Analysis | Alternative fuel, currency and demand assumptions where justified |
| Historical Performance | Predictions versus actual values when available |
| Model Information | Model version, validation metrics, training period and limitations |
| Data Health | Missing/stale-input warnings and refresh status |

The application must not silently produce a forecast from stale or invalid inputs.

## 10. Course alignment and academic deliverables

| Module | Project coverage | Deliverable |
|---|---|---|
| M1 — Problem Framing | Problem, decision-maker, analytics question, metrics, scope and data plan | D1 — Project Charter |
| M2 — Data Acquisition & Preparation | Source audit, collection, cleaning, alignment and documentation | D2 — Data Audit and dataset |
| M3 — EDA | Trends, relationships, hypotheses, seasonality and anomalies | D3 — EDA notebook and insight summary |
| M4 — Modelling | Baseline, candidates, tuning and experiment logging | D4 — Modelling checkpoint |
| M5 — Evaluation | Chronological validation, leakage prevention, errors and uncertainty | D5 — Evaluation memo |
| M6 — Deployment & Monitoring | API, HTML interface, refresh, monitoring and retraining | D6 — Deployment/monitoring plan |
| M7 — Communication | Final report, model card, limitations and presentation | D7 — Final communication |

### Deliverable definitions

- **D1 — Project Charter:** Four-page main charter plus appendix containing the problem statement, stakeholder map, success metrics and acceptance criteria, scope, assumptions, data plan, risks, timeline, team roles, meeting log and responsibility matrix.
- **D2 — Data Audit:** Source register, definitions, coverage, missingness, quality, access/privacy notes, cleaned dataset and data dictionary.
- **D3 — EDA:** Descriptive analysis, relationships, hypotheses, anomalies and business insights.
- **D4 — Modelling:** Baseline, candidate algorithms, experiment design, tuning decisions and experiment log.
- **D5 — Evaluation:** Leakage-free validation, out-of-sample errors, error analysis, uncertainty and limitations.
- **D6 — Deployment and Monitoring:** HTML/API architecture, data refresh, monitoring, drift, retraining and maintenance; prototype can support the demonstration.
- **D7 — Communication:** Final report, model card, presentation and individual technical/business Q&A readiness.

## 11. Twelve-week roadmap

| Week | Focus | Module | Gate / output |
|---|---|---|---|
| 1 | Scope and feasibility audit | M1 | Confirmed scope, sources and repository; decide whether comparable observations are sufficient |
| 2 | Historical data collection | M2 | Raw datasets and source register |
| 3 | Cleaning and alignment | M2 | Master dataset and data dictionary |
| 4 | EDA and hypotheses | M3 | EDA, insights and anomaly review |
| 5 | Baseline | M4 | Baseline and metrics |
| 6 | Candidate ML models | M4 | Comparison and experiment log |
| 7 | Evaluation | M5 | Unseen-quarter evaluation and leakage check |
| 8 | Prediction engine | M4/M5 | Versioned model, preprocessing and scenarios |
| 9 | HTML and API | M6 | Working local application |
| 10 | Market-data refresh | M6 | Refresh/prediction workflow |
| 11 | Deployment and monitoring | M6 | Testing and monitoring plan |
| 12 | Report, model card and presentation | M7 | Final submission package |

## 12. Week-by-week implementation plan

### Week 1 — Scope and feasibility
Confirm the target and one-quarter horizon, audit historical data availability, create the source register and repository. Gate: are enough comparable observations available?

### Week 2 — Data acquisition
Collect financial and market data, record each source/date/unit/definition, and preserve raw data unchanged.

### Week 3 — Data preparation
Align to fiscal quarters, standardise definitions and units, calculate PAT margin, build the data dictionary and check feature availability at forecast dates.

### Week 4 — EDA
Analyse trends and seasonality; examine fuel, currency, inflation and demand relationships; investigate unusual periods; test hypotheses and freeze the initial predictor list.

### Week 5 — Baseline
Build the feature pipeline, create a simple baseline, define chronological evaluation and calculate MAE/RMSE.

### Week 6 — Candidate models
Train Ridge/Elastic Net, test a nonlinear candidate if justified, tune conservatively and log experiments.

### Week 7 — Evaluation
Evaluate on unseen later quarters, use rolling-origin evaluation where feasible, and check leakage, errors, directional accuracy and uncertainty.

### Week 8 — Prediction engine
Select a model based on evidence, package preprocessing/prediction, add input validation and scenarios, and version model metadata.

### Week 9 — HTML and API
Build the frontend and Python API, connect the UI to the model, and display forecasts, inputs and model performance.

### Week 10 — Market integration
Add reliable programmatic sources or verified file import and implement freshness/completeness checks.

### Week 11 — Deployment and monitoring
Test valid, missing and stale inputs; record predictions; define drift/performance monitoring and retraining triggers; prepare a reproducible demonstration.

### Week 12 — Final submission
Complete report and model card, document responsible use and limitations, prepare the presentation and live demonstration, and rehearse individual questions.

## 13. Scenario analysis

Scenario analysis is a business sensitivity tool, not a causal claim.

| Scenario | Concept | Purpose |
|---|---|---|
| Low-cost / favourable | More favourable cost/currency conditions with an appropriate demand assumption | Supportive-condition estimate |
| Base case | Central assumptions supported by available evidence | Reference forecast |
| High-cost / adverse | Higher costs / less favourable currency conditions | Downside-risk estimate |

Only vary inputs that the model and data can reasonably support. Keep the scenario assumptions visible.

## 14. Deployment and monitoring

| Area | Monitor | Action |
|---|---|---|
| Data freshness | Whether required inputs are updated | Warn or delay prediction |
| Data quality | Missing values, invalid units and unexpected ranges | Reject or quarantine invalid inputs |
| Feature drift | Changes in input distributions | Investigate and consider retraining |
| Prediction performance | MAE/RMSE once actual outcomes arrive | Review the model |
| Model version | Which model generated a forecast | Maintain reproducibility |
| Retraining | Sustained degradation or regime change | Retrain and revalidate |

## 15. Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Small quarterly sample | Complex models may be unstable | Parsimonious models, strong baseline and time-based validation |
| Data inconsistency | Invalid comparisons | Source register, data dictionary and reconciliation |
| Future leakage | Artificially strong evaluation | Forecast-date availability rules and chronological validation |
| API/access limitations | Automated refresh may fail | Verified file-import alternative and documented limitations |
| Exceptional events/regime changes | Relationships may shift | Flag unusual periods, robustness checks and caveats |
| ML underperformance | Complex model may not beat baseline | Keep baseline as comparator; simplify if needed |
| Integration delay | UI work can crowd out analytics | Freeze model before UI integration and stage development |

## 16. Scope and assumptions

### In scope
- Quarterly next-period PAT-margin forecasting.
- Historical financial and selected market/operating variables.
- ML comparison and time-based evaluation.
- Latest-available market-data refresh where reliable.
- HTML interface connected to a Python backend.
- Scenario analysis, monitoring design and ANCP M1–M7 documentation.

### Out of scope
- Stock-price prediction.
- Real-time measurement of unpublished profit.
- Unverified causal claims.
- Future information during evaluation.
- Deep learning unless data and evidence justify it.
- News sentiment unless reliable historical data and validation justify it.

### Assumptions
- Sufficient comparable historical observations can be assembled.
- Financial definitions can be aligned consistently.
- Selected predictors have adequate historical coverage.
- The final feature list is determined after audit and EDA.
- One-quarter forecasting remains the primary horizon.

## 17. Final deliverables

| Deliverable | Expected contents |
|---|---|
| D1 | Project charter and appendix |
| D2 | Data audit, cleaned dataset and data dictionary |
| D3 | EDA notebook and insights |
| D4 | Baseline, candidate models and experiment log |
| D5 | Evaluation, leakage controls and uncertainty |
| D6 | Deployment/monitoring plan and HTML/API prototype or demonstration |
| D7 | Final report, model card and presentation |
| Technical product | HTML frontend, Python API, ML engine, refresh workflow and scenario module |

## 18. Submission and project checklist

- Confirm team number and member names.
- Confirm milestone labels and dates against the official course schedule.
- Keep the D1 main body within the required page limit and use the permitted appendix.
- Maintain a meeting log and responsibility matrix.
- Keep raw and processed data separate.
- Maintain experiment logs from the baseline onward.
- Document sources and transformations.
- Use chronological validation and explicitly check leakage.
- Compare ML models with a simple baseline.
- Label outputs as forecasts, not unpublished actual results.
- Document limitations and responsible-use conditions.
- Test the HTML → API → ML → prediction flow end to end.
- Keep the final application reproducible from the repository.

## Final working project statement

This project will develop an integrated, market-sensitive machine-learning system for forecasting IndiGo's next-quarter PAT margin. It will combine historical financial performance with selected market, macroeconomic and operating indicators, evaluate forecasting approaches against a simple baseline using leakage-free time-based validation, and expose the selected model through an HTML application connected to a Python backend. The application will support refreshed forecasts, scenario analysis and monitoring while communicating uncertainty and limitations.
