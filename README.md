# IndiGo Airline Profitability Intelligence System

**PGDM Business Analytics Capstone | D1 Project Charter | CO1 and CO6**

## Overview
This project proposes an end-to-end analytics system to forecast IndiGo's next-quarter Profit After Tax (PAT) margin using public financial, operating and macroeconomic indicators. The lifecycle covers data preparation, EDA, baseline comparison, model experiments, chronological evaluation, explainability, scenario analysis, deployment planning and monitoring.

This is an academic prototype based on public/aggregate information. It is not commissioned by or endorsed by IndiGo and is not an official company forecast.

## Business problem
For a hypothetical airline finance-planning decision-maker, can a model using information available at the forecast date predict next-quarter PAT margin with at least 10% lower MAE than a last-quarter-persistence baseline on chronological holdout quarters?

**Target:** `pat_margin_pct = (PAT / Revenue) * 100`

All predictors must be available at the forecast date to avoid look-ahead leakage.

## Project files
- [D1 Project Charter (Markdown)](docs/Project_Charter.md) — scope, stakeholder map, measurable acceptance criteria, data plan, risks, milestones, team roles, meeting log and responsibility matrix.
- [Data dictionary (CSV)](IndiGo_Data_Dictionary.csv) — proposed field definitions, data sources and quality controls.

The formatted four-page PDF is prepared for course submission in the project workspace. Add the PDF to this repository using GitHub's web interface if a PDF copy is required in the repository itself.

## Success criteria
- Candidate model MAE at least 10% below the baseline on the same chronological holdout quarters.
- Candidate model RMSE no worse than baseline RMSE.
- At least 95% completeness in selected modelling fields after alignment and no duplicate fiscal-quarter keys.
- All predictors pass availability-at-forecast-date checks.
- A local demo lets a user select a scenario, request a prediction and view metrics and limitations.

These are proposed targets to confirm after the D2 data audit. If no candidate beats the baseline, report that result honestly.

## Candidate public data sources
- [IndiGo quarterly financial results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html): revenue, PAT, EBITDAR and financial disclosures.
- [IndiGo investor relations](https://www.goindigo.in/information/investor-relations.html): operational statistics and supporting disclosures.
- [PPAC](https://ppac.gov.in/): consistent aviation turbine fuel (ATF) price proxy.
- [RBI DBIE](https://data.rbi.org.in/DBIE/): USD/INR exchange-rate series.
- [MoSPI](https://www.mospi.gov.in/): CPI/inflation.
- [DGCA](https://www.dgca.gov.in/): optional cross-check of published airline traffic indicators.

The expected size is a planning estimate of roughly 35–45 quarterly observations after alignment, plus monthly raw economic observations. Confirm usable size during the data audit and record URLs, retrieval/publication dates, units and reporting periods.

## Privacy and limitations
Use aggregate public data only. Do not collect passenger-level records or personal information. Review publisher terms before redistributing data; where rights are unclear, link to the original source instead. Quarterly observations may be limited, so begin with a baseline and report uncertainty. Scenario outputs are conditional estimates, not causal claims or guaranteed outcomes.

## Milestones (no calendar dates)
| Milestone | Planned output |
|---|---|
| D1 — Charter and setup | Problem, scope, stakeholders, metrics, risks, roles, repository and README |
| D2 — Data feasibility | Source register, data dictionary, aligned dataset and quality checks |
| D3 — EDA and baseline | EDA, baseline forecast, leakage review and modelling go/no-go |
| Modelling checkpoint | Reproducible training pipeline and candidate-model results |
| E1 — Evaluation memo | Chronological model comparison, metrics, explainability and scenario tests |
| Deployment and monitoring plan | Prototype plan, monitoring checks and retraining triggers |
| E2 — Draft report and dry run | Draft report, model card, demo and presentation rehearsal |

## Team
- Nikhil Raj
- Krishan Sharma
- K. Shreya

The charter's responsibility matrix assigns each member at least two lead deliverables. Fill the meeting log with actual meeting details only.

## D1 checklist
- Confirm the team number and required PDF filename with the course instructions.
- Confirm milestone labels against the course schedule.
- Ensure every team member leads at least two deliverables.
- Document source rights and privacy considerations.
- Do not claim model performance before experiments are run and evaluated.
