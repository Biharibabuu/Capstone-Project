# Capstone milestone archive

This directory is the evaluation-ready record for the IndiGo Profitability Intelligence System. Each milestone has its own scope, deliverable record, files, version notes and status.

| Milestone | Deliverable | Status | Folder |
|---|---|---|---|
| M1 | D1 Project Charter | Completed | [M1_D1_Project_Charter](M1_D1_Project_Charter/) |
| M2 | D2 Data Audit | Completed; source and data limitations documented | [M2_D2_Data_Audit](M2_D2_Data_Audit/) |
| M3 | D3 Exploratory Data Analysis | Reviewed notebook and notes recorded | [M3_D3_Exploratory_Data_Analysis](M3_D3_Exploratory_Data_Analysis/) |
| M4 | D4 Modelling Checkpoint | D4-v1 report, code, tests and experiment evidence | [M4_D4_Modelling](M4_D4_Modelling/) |
| M5 | D5 Model Evaluation | Planned; checklist and pending evidence | [M5_D5_Model_Evaluation](M5_D5_Model_Evaluation/) |
| M6 | D6 Deployment and Monitoring | API/frontend scaffold exists; evaluation integration pending | [M6_D6_Deployment_Monitoring](M6_D6_Deployment_Monitoring/) |
| M7 | D7 Final Communication | Planned; final report and presentation pending | [M7_D7_Final_Communication](M7_D7_Final_Communication/) |

## Repository conventions
- Original source files remain in data/raw; processed datasets remain in data/processed.
- Milestone folders contain the milestone-specific documents, code, logs and evaluation evidence. Large source data are referenced rather than duplicated.
- Every run records its date, dataset hash/version, features, parameters, random seed and metric.
- Never commit .env files, API keys, passwords or other secrets.
- A milestone marked Planned is not represented as completed.