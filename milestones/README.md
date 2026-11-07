# Capstone milestone archive — evaluator guide

**Project:** IndiGo Profitability Intelligence System  
**Audit date:** 7 November 2026

Each milestone has its own evaluation record and file manifest. Shared code and data remain at canonical repository paths and are referenced instead of duplicated.

| Order | Milestone | Deliverable | Status | Evaluation record |
|---:|---|---|---|---|
| 1 | M1 | D1 Project Charter | Completed | [M1 record](M1_D1_Project_Charter/EVALUATION_RECORD.md) |
| 2 | M2 | D2 Data Audit | Completed for 30-Oct package; 7-Nov workbooks need reconciliation | [M2 record](M2_D2_Data_Audit/EVALUATION_RECORD.md) |
| 3 | M3 | D3 EDA | Reviewed; source-only notebook public, output-rich exports local | [M3 record](M3_D3_Exploratory_Data_Analysis/EVALUATION_RECORD.md) |
| 4 | M4 | D4 Modelling | D4-v1 executed 7-Nov-2026 | [M4 record](M4_D4_Modelling/EVALUATION_RECORD.md) |
| 5 | M5 | D5 Evaluation | Planned; report/backtest pending | [M5 record](M5_D5_Model_Evaluation/EVALUATION_RECORD.md) |
| 6 | M6 | D6 Deployment/Monitoring | API/frontend/connectors scaffold exists; integration pending | [M6 record](M6_D6_Deployment_Monitoring/EVALUATION_RECORD.md) |
| 7 | M7 | D7 Final Communication | Planned; final package pending | [M7 record](M7_D7_Final_Communication/EVALUATION_RECORD.md) |

## Evaluation controls

- Target: next-quarter PAT margin = PAT / Revenue from Operations × 100; not stock-price forecasting.
- D4-v1 is pinned to data/processed/Final_Quarterly_Data(1).xlsx, SHA-256 85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c. Do not silently replace it.
- D4 selected persistence because Ridge and Random Forest did not beat it on validation.
- Historical release timestamps are unavailable for every input; one-quarter lagging does not prove exact point-in-time availability.
- Brent is a crude benchmark proxy, not IndiGo's realised ATF cost. The audited package has EBITDA, not confirmed EBITDAR, and no passenger count/load-factor records.
- Planned milestones are not represented as completed.

## Registers

- [Milestone status register](MILESTONE_REGISTER.csv)
- [File-by-file inventory — all 61 Project Library files](ARTIFACT_INVENTORY_2026-11-07.csv)
- [Audit and upload decisions](ARTIFACT_AUDIT_2026-11-07.md)

Repository convention: raw/processed data, source code, reports and notebooks retain canonical locations. Each milestone manifest lists shared files. Do not commit secrets or unlicensed Bloomberg exports/output-rich analysis without permission.
