# IndiGo Airline Profitability Intelligence System

**PGDM Business Analytics Capstone | D1 Project Charter | Linked outcomes: CO1 and CO6**

## Project overview

This project proposes an end-to-end analytics system to forecast IndiGo's next-quarter Profit After Tax (PAT) margin using public financial, operating and macroeconomic indicators. The workflow will include data preparation, exploratory data analysis (EDA), baseline comparison, machine-learning experiments, evaluation, explainability, scenario analysis, deployment planning and monitoring.

This is an academic prototype based on public/aggregate information. It is not commissioned by or endorsed by IndiGo and is not an official company forecast or a substitute for professional financial advice.

## Business problem

For a hypothetical airline finance-planning decision-maker, can a model using only information available at the forecast date predict next-quarter PAT margin with at least 10% lower mean absolute error (MAE) than a last-quarter-persistence baseline on chronological holdout quarters?

**Target:** `pat_margin_pct = (PAT / Revenue) * 100`

The target is next-quarter PAT margin, expressed in percentage points. Predictors must be available by the forecast date to avoid look-ahead leakage.

## Project lifecycle

1. **Business understanding:** problem statement, decision-maker, stakeholders, scope and acceptance criteria.
2. **Data understanding:** source register, data dictionary, units, publication dates, completeness and row counts.
3. **Data preparation:** clean and align fiscal quarters; validate duplicates, missing values and units.
4. **Modelling:** compare a simple last-quarter baseline with suitable regression/tree-based candidates if sample size supports them.
5. **Evaluation:** chronological or rolling-origin validation using MAE and RMSE; no random split.
6. **Explainability and scenarios:** summarize key model drivers and run clearly labelled base/bear/bull scenarios.
7. **Deployment planning:** local application prototype with prediction inputs, outputs and limitations.
8. **Monitoring and reporting:** forecast-error/drift checks, model card, final report and demonstration.

## Success criteria

- Candidate model MAE at least 10% below baseline MAE on the same chronological holdout quarters.
- Candidate model RMSE no worse than baseline RMSE.
- At least 95% completeness in selected modelling fields after alignment, with no duplicate fiscal-quarter keys.
- All predictors pass availability-at-forecast-date checks.
- A local demo allows a user to choose a scenario, request a prediction and view metrics and limitations.

These are proposed targets, to be confirmed after the D2 data audit. If no model beats the baseline, report that result honestly.

## Candidate data sources

- [IndiGo quarterly financial results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html): Revenue, PAT, EBITDAR and financial disclosures.
- [IndiGo investor relations](https://www.goindigo.in/information/investor-relations.html): operational statistics and supporting disclosures.
- [Petroleum Planning & Analysis Cell](https://ppac.gov.in/): a consistent aviation turbine fuel (ATF) price proxy.
- [RBI Database on Indian Economy](https://data.rbi.org.in/DBIE/): documented USD/INR exchange-rate series.
- [MoSPI](https://www.mospi.gov.in/): CPI/inflation.
- [DGCA](https://www.dgca.gov.in/): optional cross-check of published airline traffic indicators.

Expected size is a planning estimate of roughly 35–45 quarterly observations after alignment, plus monthly raw economic observations. The usable sample and completeness will be confirmed during the data audit. Record source URL, retrieval/publication date, units, fiscal period and any revisions.

## Privacy, rights and assumptions

Use only public aggregate financial, operating and macroeconomic data. Do not collect passenger-level records or personal information. Check source terms before redistributing files in a public repository; if rights are unclear, link to the source instead of committing the raw data. Quarterly observations may be limited and affected by exceptional events, so begin with a baseline and report uncertainty. Scenario outputs are conditional estimates, not causal claims or guaranteed outcomes.

## Milestones

| Milestone | Planned output |
|---|---|
| D1 – Charter and setup | Problem statement, target, scope, stakeholders, metrics, risks, roles, repository and README |
| D2 – Data feasibility | Source register, data dictionary, aligned master table and quality checks |
| D3 – EDA and baseline | EDA findings, baseline forecast, leakage review and modelling go/no-go decision |
| E1 – Model and evaluation | Reproducible model comparison, chronological metrics, explainability and scenario tests |
| E2 – Integration and review | Local web app, final report/dashboard, monitoring plan and final demo |

## Team

- Nikhil Raj
- Krishan Sharma
- K. Shreya

The project charter contains the responsibility matrix and meeting-log appendix. Each member should lead at least two deliverables; record actual meeting details in the meeting log.

## Repository files

- [Four-page D1 project charter (PDF)](IndiGo_D1_Project_Charter_4_Pages_Final.pdf)
- [Editable project charter (DOCX)](IndiGo_D1_Project_Charter_4_Pages_Final.docx)
- [Data dictionary](IndiGo_Data_Dictionary.csv)

## D1 checklist

- Confirm team number and required submission filename with the course instructions.
- Confirm milestone labels against the course schedule.
- Ensure every team member leads at least two deliverables.
- Keep data-source rights and privacy considerations documented.
- Do not claim model performance until experiments have been run and evaluated.
