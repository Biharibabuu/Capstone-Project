# IndiGo Airline Profitability Intelligence System
## D1 Project Charter

**Course:** PGDM Business Analytics Capstone  
**Linked outcomes:** CO1, CO6  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya

## 1. Problem statement

For a hypothetical airline finance-planning decision-maker, can a model using information available at the forecast date predict IndiGo's next-quarter Profit After Tax (PAT) margin with at least 10% lower mean absolute error (MAE) than a last-quarter-persistence baseline on chronological holdout quarters?

**Business decision:** Use a forecast and scenario analysis to support quarterly financial planning and risk discussion.  
**Decision-maker:** Hypothetical Finance Planning / FP&A lead.  
**Target:** `PAT margin (%) = PAT / Revenue × 100`.

This is an academic prototype using public and aggregate information. It is not commissioned by or endorsed by IndiGo and is not an official company forecast.

## 2. Stakeholder map

| Stakeholder | Role / interest |
|---|---|
| Hypothetical Finance Planning / FP&A lead | Decision-maker; reviews forecast and scenarios |
| Project team | Builds the dataset, analysis, model and prototype |
| IndiGo investor-relations / reporting team | Publishes financial and operational disclosures; not a project partner |
| PPAC, RBI, MoSPI and DGCA | Candidate providers of public economic and aviation data |
| Course faculty / evaluator | Reviews methods, documentation and deliverables |
| Public / management audiences | Potentially affected by interpretations; results must be labelled as estimates |

## 3. Success metrics and acceptance criteria

| Measure | Proposed acceptance criterion | Baseline / comparison |
|---|---|---|
| Forecast MAE | Selected model MAE at least 10% lower | Last-quarter-persistence baseline, same chronological holdout |
| Forecast RMSE | No worse than baseline | Same quarters and target definition |
| Data completeness | At least 95% in selected modelling fields after alignment | Master dataset audit |
| Quarter integrity | Zero duplicate fiscal-quarter keys | Unique-quarter validation |
| Leakage control | All predictors available at forecast date | Publication-date / forecast-origin review |
| Application usability | User can select a scenario, request a prediction, view metrics and limitations | End-to-end demo checklist |

These are proposed targets and must be reviewed after the data audit. If the model does not outperform the baseline, report that result honestly.

## 4. Scope and assumptions

**In scope:** public financial and operating data collection; selected ATF, USD/INR and CPI indicators; data-quality log; EDA; baseline and candidate models; chronological evaluation; explainability; base/bear/bull scenarios; local web-app prototype; monitoring plan and final report.

**Out of scope:** passenger-level or other personal data; internal or paid company data; live airline operations; automated investment/trading recommendations; claims of causal impact; official forecasts for IndiGo.

**Assumptions:** public data is sufficient for a feasibility test; financial and operational definitions can be aligned; the sample may be small, so model complexity will depend on available observations.

## 5. Data plan

| Candidate source | Fields / purpose | Access and controls |
|---|---|---|
| [IndiGo quarterly results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html) | Revenue, PAT, EBITDAR and financial disclosures | Public access assumed; record release date and units |
| [IndiGo investor relations](https://www.goindigo.in/information/investor-relations.html) | Passenger volume and load factor where available | Public disclosures; harmonize periods and definitions |
| [PPAC](https://ppac.gov.in/) | Consistent ATF price proxy | Public source; document series, geography and aggregation |
| [RBI DBIE](https://data.rbi.org.in/DBIE/) | USD/INR indicator | Public source; document quarterly aggregation rule |
| [MoSPI](https://www.mospi.gov.in/) | CPI / inflation | Public source; keep series and base year consistent |
| [DGCA](https://www.dgca.gov.in/) | Optional aviation-statistics cross-check | Use only comparable published measures |

**Expected size:** planning estimate of approximately 35–45 quarterly records after alignment plus monthly raw economic observations; actual usable size will be confirmed during the audit. Record URL, retrieval date, publication date, period, units and revisions. Do not upload raw files to a public repository unless redistribution rights are clear; link to the source when unsure. Use aggregate public data only and do not collect personal data.

## 6. Feasibility and key risks

| Risk | Mitigation |
|---|---|
| Too few quarterly observations | Start with a simple baseline; use rolling-origin validation; avoid overfitting |
| Look-ahead data leakage | Record publication dates and use only values available at each forecast origin |
| Different units / accounting definitions | Maintain a source register; reconcile definitions and unit conversions |
| Missing or revised observations | Log gaps and revisions; document justified treatment; test sensitivity |
| Complex model gives misleading confidence | Compare with baseline; report MAE/RMSE, limitations and uncertainty; avoid causal claims |

## 7. Milestones and deliverables

| Milestone | Deliverable / exit check |
|---|---|
| D1 — Charter and setup | Approved problem, scope, stakeholder map, metrics, risks, roles, repository and README |
| D2 — Data feasibility | Source register, data dictionary, aligned master table and quality checks |
| D3 — EDA and baseline | EDA findings, baseline forecast, leakage review and modelling go/no-go decision |
| Modelling checkpoint | Reproducible training pipeline and documented candidate-model results |
| E1 — Evaluation memo | Chronological model comparison, MAE/RMSE, explainability and scenario tests |
| Deployment and monitoring plan | Local prototype design, input/output description, drift/error checks and retraining triggers |
| E2 — Draft report and dry run | Draft report, model card, working demo and presentation rehearsal |

## 8. Responsibility matrix

Each team member leads at least two deliverables.

| Deliverable | Lead owner | Support |
|---|---|---|
| D1 charter and repository setup | Nikhil Raj | Krishan Sharma, K. Shreya |
| D2 data audit and datasheet | Krishan Sharma | Nikhil Raj, K. Shreya |
| D3 EDA and insight summary | K. Shreya | Nikhil Raj, Krishan Sharma |
| Modelling checkpoint | Nikhil Raj | Krishan Sharma, K. Shreya |
| E1 evaluation memo | Krishan Sharma | Nikhil Raj, K. Shreya |
| Deployment and monitoring plan | K. Shreya | Nikhil Raj, Krishan Sharma |
| Draft report, model card and dry run | Nikhil Raj | Krishan Sharma, K. Shreya |

## Appendix A — Meeting log

| Meeting | Date | Attendees | Decisions / actions | Owner and due |
|---|---|---|---|---|
| Kick-off | To be completed after meeting | Nikhil Raj; Krishan Sharma; K. Shreya | Confirm target, responsibilities and data approach | Team to complete |
| Data feasibility review | To be completed after meeting | Team | Review source coverage, data quality and feasibility | Team to complete |

Record actual meeting dates, decisions and action items; do not enter meetings that have not occurred.

## Appendix B — Repository and README

Repository: [Biharibabuu/Capstone-Project](https://github.com/Biharibabuu/Capstone-Project)  
README: [Open project README](../README.md)  
Data dictionary: [Open data dictionary](../IndiGo_Data_Dictionary.csv)

Required PDF submission filename should be updated to the actual course team number before final submission.