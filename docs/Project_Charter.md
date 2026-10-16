# IndiGo Profitability Intelligence System
## D1 Project Charter

**Course:** PGDM Business Analytics Capstone  
**Linked outcomes:** CO1, CO6  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya

## 1. Problem statement

Develop and evaluate a machine-learning model that uses historical IndiGo financial performance and publicly available market and operating indicators to forecast the company's next-quarter PAT margin, and determine whether the selected model improves predictive performance over a simple historical baseline on unseen quarters.

**Business decision:** Use the forecast and scenario analysis to support quarterly financial planning and risk discussion.  
**Decision-maker:** Business/finance decision-makers, analysts and project stakeholders.  
**Target:** PAT Margin (%) = Profit After Tax / Revenue from Operations × 100.  
**Forecast horizon:** One quarter ahead.

This is an academic prototype using public and aggregate information. It is not commissioned by or endorsed by IndiGo and does not reveal unpublished actual results.

## 2. Stakeholder map

| Stakeholder | Role / interest |
|---|---|
| Business / finance decision-maker | Uses forecast for planning and risk assessment; needs forecast, scenarios, reliability information and limitations |
| Project team | Builds, validates and documents the data, model and prototype |
| Public data suppliers | Provide financial, macroeconomic and operating information; source definitions, dates, units and access conditions must be documented |
| Faculty / evaluator | Assesses analytical rigor and course outcomes through charter, evidence, evaluation, report and presentation |
| Prototype users | Interact with the HTML application and receive validated inputs and prediction outputs |

IndiGo public investor-relations disclosures and external data providers are sources of public data, not project partners.

## 3. Success metrics and acceptance criteria

| Measure | Acceptance check | Comparison / evidence |
|---|---|---|
| Forecast error | Calculate MAE and RMSE on unseen later quarters | Compare selected model with a simple historical baseline on the same quarters |
| Directional accuracy | Report if defined consistently and useful for the data | Predicted versus actual direction of PAT-margin movement |
| Baseline improvement | Determine whether ML adds value; do not assume it will | Out-of-sample performance versus baseline |
| Data quality | Document missingness, duplicates, inconsistent units and revisions | D2 data audit and source register |
| Leakage control | Every feature must have been available at the forecast date | Publication-date checks and chronological/rolling-origin validation |
| Application behaviour | Validate inputs, show forecast and relevant limitations, warn on missing/stale inputs | End-to-end HTML → API → ML → prediction demonstration |
| Reproducibility | Store source details, transformations, model version and experiment record | Repository, source register and experiment log |

The final feature list and any data-completeness thresholds will be decided during the data audit. If the model does not outperform the baseline, report that result honestly instead of claiming ML superiority.

## 4. Scope and assumptions

**In scope:** public financial and operating data; selected ATF/fuel-price, USD/INR and CPI indicators; source register and data dictionary; data quality; EDA; baseline and candidate models; time-ordered evaluation; explainability; low-cost/favourable, base and high-cost/adverse scenarios; a local HTML web application with a Python API; data refresh where reliable; monitoring and final reporting.

**Out of scope:** passenger-level personal data; internal or paid company data; stock-price prediction; live airline operations; automated investment/trading recommendations; claims of causal impact; official forecasts for IndiGo; use of future information in historical evaluation.

**Assumptions:** enough comparable historical observations may be available; financial and operational definitions can be aligned; the data audit and EDA will determine the final feature list and model complexity. The model cannot know unpublished actual current-quarter profit.

## 5. Data plan

| Candidate source | Fields / purpose | Access and controls |
|---|---|---|
| [IndiGo quarterly results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html) | Revenue from operations, PAT, EBITDAR and financial disclosures | Record publication date, fiscal period, definitions and units |
| [IndiGo investor relations](https://www.goindigo.in/information/investor-relations.html) | Passengers carried, passenger load factor and operating disclosures where available | Verify comparability across periods |
| [PPAC](https://ppac.gov.in/) | ATF price or verified fuel-price proxy | Document series, geography, units and aggregation |
| [RBI DBIE](https://data.rbi.org.in/DBIE/) | USD/INR | Document source series and quarterly aggregation rule |
| [MoSPI](https://www.mospi.gov.in/) | CPI / inflation | Keep series and base year consistent |
| [DGCA](https://www.dgca.gov.in/) | Optional cross-check of published aviation statistics | Use only comparable published measures |

Expected historical coverage, dataset size, access rights, privacy considerations and final variable inclusion will be recorded in D2. Record source URL, publication/retrieval dates, period, units and revisions. Keep raw data unchanged and separate raw from processed data. Do not commit source data publicly unless redistribution terms allow it; link to the source if rights are unclear. No passenger-level personal data is needed.

## 6. Feasibility and key risks

| Risk | Mitigation |
|---|---|
| Small quarterly sample | Start with a simple baseline, use time-based validation and avoid excessive model complexity |
| Future-information leakage | Record publication dates; only use values available at the forecast origin |
| Inconsistent units / definitions | Maintain a source register and data dictionary; reconcile definitions and conversions |
| Missing, revised or stale observations | Log gaps and revisions; validate input freshness and completeness; warn or delay prediction if inputs are invalid |
| API/access limitations | Support verified file import and document any manual refresh process |
| Exceptional events or changing relationships | Review unusual periods, run robustness checks and state limitations |
| ML underperformance | Keep the baseline as a formal comparator; simplify if necessary |
| Integration delay | Stage development and freeze the evaluated model before UI integration |

## 7. Milestones and deliverables

| Milestone | Deliverable / exit check |
|---|---|
| D1 — Charter and setup | Problem, scope, stakeholder map, metrics, risks, roles, repository and README |
| D2 — Data audit | Source register, definitions, coverage, missingness, quality/access notes, cleaned dataset and data dictionary |
| D3 — EDA and insights | Trends, relationships, hypotheses, anomalies, seasonality and business insights |
| Modelling checkpoint (D4) | Baseline, candidate models, experiment design and documented model results |
| E1 — Evaluation memo (D5) | Chronological model comparison, MAE/RMSE, leakage checks, error analysis, uncertainty and limitations |
| Deployment and monitoring plan (D6) | HTML/API architecture or prototype, refresh workflow, data health, monitoring and retraining triggers |
| E2 — Draft report and dry run (D7) | Draft/final report, model card, presentation, demonstration and Q&A preparation |

No calendar dates are included in this milestone table. Use the course schedule separately to manage due dates.

## 8. Responsibility matrix

Each team member leads at least two deliverables.

| Deliverable | Lead owner | Support |
|---|---|---|
| D1 charter and repository setup | Nikhil Raj | Krishan Sharma, K. Shreya |
| D2 data audit and datasheet | Krishan Sharma | Nikhil Raj, K. Shreya |
| D3 EDA and insight summary | K. Shreya | Nikhil Raj, Krishan Sharma |
| Modelling checkpoint (D4) | Nikhil Raj | Krishan Sharma, K. Shreya |
| E1 evaluation memo (D5) | Krishan Sharma | Nikhil Raj, K. Shreya |
| Deployment and monitoring plan (D6) | K. Shreya | Nikhil Raj, Krishan Sharma |
| Draft report, model card and dry run (D7) | Nikhil Raj | Krishan Sharma, K. Shreya |

## Appendix A — Meeting log

| Meeting | Date | Attendees | Decisions / actions | Owner and due |
|---|---|---|---|---|
| Kick-off | Complete after meeting | Nikhil Raj; Krishan Sharma; K. Shreya | Confirm target, responsibilities and data approach | Team to complete |
| Data feasibility review | Complete after meeting | Team | Review source coverage, data quality and feasibility | Team to complete |

Enter only meetings that have actually occurred. Record the actual date, decisions and assigned action items.

## Appendix B — Repository and documentation

- [GitHub repository](https://github.com/Biharibabuu/Capstone-Project)
- [README](../README.md)
- [Master project plan](Master_Project_Plan.md)
- [Data dictionary](../IndiGo_Data_Dictionary.csv)

Confirm the required team number and PDF filename against the course submission instructions before submitting.
