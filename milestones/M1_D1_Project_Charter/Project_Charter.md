# IndiGo Profitability Intelligence System
## M1 / D1 — Project Charter

**Status:** Done  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya  
**Forecast horizon:** One quarter ahead  
**Current outcome:** IndiGo next-quarter EBITDA margin

## 1. Problem statement

Develop and evaluate an analytical forecasting system that uses historical IndiGo financial performance and available macroeconomic/market indicators to estimate next-quarter EBITDA margin, compare candidate models with a simple baseline, and communicate forecast limitations to finance/business stakeholders.

**Business decision:** Support quarterly financial planning and risk discussion.  
**Target:** EBITDA margin (%) = EBITDA / Revenue from Operations × 100, subject to final source-line reconciliation and a documented denominator.  
**Forecast horizon:** One quarter ahead.

This is an academic prototype. It is not commissioned by or endorsed by IndiGo and must not present estimates as unpublished company results.

## 2. Stakeholders

| Stakeholder | Interest / responsibility |
|---|---|
| Finance/business user | Understand forecast, assumptions, scenarios and reliability |
| Project team | Build, validate and document data, model and prototype |
| Bloomberg data provider | Supplies licensed exports; source IDs, field definitions, units and usage restrictions must be recorded |
| Faculty/evaluator | Assesses analytical rigor, evidence and communication |
| Prototype user | Interacts with the eventual HTML/API application |

## 3. Scope

**In scope:** Quarterly IndiGo financials; USD/INR; CPI; WPI; Dated Brent crude as a cost proxy; data audit; EDA; EBITDA-margin forecasting; chronological validation; scenario analysis where defensible; API/UI prototype; monitoring plan; final reporting.

**Out of scope:** Stock-price prediction; live airline operating data not supplied; automated trading/investment advice; causal claims; fabricated load factor, passenger yield, RPK/ASK or ATF values.

## 4. Data plan

| Category | Available fields / source | Usage and limitation |
|---|---|---|
| IndiGo financials | Bloomberg INDIGO IN; SALES_REV_TURN, NET_INCOME, EBITDA | Reconcile Revenue from Operations and EBITDA definitions; exclude estimates from realised labels |
| USD/INR | USDINR REGN Curncy, PX_LAST (monthly) | Macro/currency predictor; respect publication/availability date |
| CPI | INFUTOTY Index, PX_LAST | Verify exact series definition and base |
| WPI | INBGWPIY Index, PX_LAST | Verify exact series definition and base |
| Oil benchmark | EUCRBRDT Index, PX_LAST; daily and monthly Dated Brent | Proxy only; not Indian ATF or IndiGo's realised fuel cost |

Raw workbook data are stored in M2. The EDA panel is stored in M3. M4 keeps its exact modelling snapshot and derived features in its own folder. Do not duplicate datasets across milestones without a versioning reason.

## 5. Success criteria

- Data provenance, units, dates, estimates and limitations are explicit.
- EBITDA target and denominator are reproducible.
- Features are available by the historical forecast origin; no look-ahead leakage.
- Candidate models are compared with a chronological baseline on held-out quarters.
- MAE/RMSE and limitations are reported honestly.
- Training and forecast outputs are reproducible.
- API/UI prototype is tested before claiming deployment readiness.

No model improvement is assumed in advance. If ML fails to beat a simple baseline, that is a valid result.

## 6. Risks and controls

| Risk | Control |
|---|---|
| Small quarterly sample | Start with simple baselines and constrain model complexity |
| Misaligned financial lines | Reconcile source statement dates and definitions |
| Future information leakage | Store observation and availability dates; use chronological validation |
| Brent mistaken for ATF | Always describe as Dated Brent proxy |
| Licensed data redistribution | Confirm rights before publishing workbooks or output-rich notebooks |
| Legacy PAT experiment confused with current target | Keep old D4-v1 results clearly labelled as legacy PAT-margin evidence |

## 7. Milestone sequence

M1 Charter — Done; M2 Data Audit — Done; M3 EDA — Done; M4 Modelling — In Progress; M5 Evaluation — Todo; M6 Deployment/Monitoring — Todo; M7 Final Communication — Todo.

## 8. Change control

Any change to target, horizon, source, feature set or data rights must be recorded in the project change log and reflected in the README, data dictionary, milestone manifests and affected experiment records.
