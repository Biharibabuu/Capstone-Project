# Capstone Milestone Archive

**Project:** IndiGo Profitability Intelligence System  
**D1 charter primary target:** Next-quarter PAT margin (secondary indicator: EBITDAR margin)  
**Active milestone:** M4 / D4 — Modelling

This is the evaluator-facing delivery archive. Each milestone has its own brief, workflow, evidence checklist, control record and manifest. Each README explains purpose, inputs, outputs, workflow, acceptance gate and data/artifacts used.

## Milestone status

| Order | Milestone | Status | Primary folder |
|---:|---|---|---|
| M1 | D1 Project Charter | Done | [M1_D1_Project_Charter](M1_D1_Project_Charter/) |
| M2 | D2 Data Audit | Done | [M2_D2_Data_Audit](M2_D2_Data_Audit/) |
| M3 | D3 EBITDA-only EDA | Completed as supplementary EBITDA-focused analysis; PAT-target alignment remains a review item | [M3_D3_Exploratory_Data_Analysis](M3_D3_Exploratory_Data_Analysis/) |
| M4 | D4 Modelling | **In Progress** | [M4_D4_Modelling](M4_D4_Modelling/) |
| M5 | D5 Model Evaluation | Todo — not started | [M5_D5_Model_Evaluation](M5_D5_Model_Evaluation/) |
| M6 | D6 Deployment and Monitoring | Todo — not started | [M6_D6_Deployment_Monitoring](M6_D6_Deployment_Monitoring/) |
| M7 | D7 Final Communication | Todo — not started | [M7_D7_Final_Communication](M7_D7_Final_Communication/) |

## Standard structure

Every milestone includes:
- `README.md` — brief, workflow, inputs, outputs and status.
- `MILESTONE_CONTROL.md` — scope, acceptance criteria, risks and next gate.
- `DELIVERABLES_CHECKLIST.md` — completion checklist.
- `MILESTONE_MANIFEST.csv` — specific evidence, dataset and artifact inventory.
- Supporting folders (where relevant): `data/`, `notebooks/`, `src/`, `tests/`, `experiments/`, `reports/`, `references/`, `presentation/`, `demo/`.

## Data placement and ownership

- M1: no analytical data; charter only.
- M2: raw/source data and audit records.
- M3: exact EDA input panel and EDA notebook/review evidence.
- M4: exact modelling input snapshot, features, run evidence, predictions and model outputs.
- M5: frozen evaluation input vintage, rolling-origin predictions and error analysis.
- M6: approved model package and deployment/configuration evidence; no duplicate training dataset.
- M7: final approved reports/slides/demo and version references.

Where a source file is shared, M2 holds the source and downstream milestones hold a clearly identified snapshot or data index with source version and SHA-256. Do not silently copy, rename or alter licensed source data.

## Registers and governance

- [Milestone register](MILESTONE_REGISTER.csv)
- [Artifact audit](ARTIFACT_AUDIT_2026-11-07.md)
- [Artifact inventory](ARTIFACT_INVENTORY_2026-11-07.csv)
- [Project board workflow](../docs/GITHUB_PROJECT_BOARD.md)
- [Project status and work log](../docs/PROJECT_STATUS_AND_WORKLOG.md)

M5-M7 are planning folders only until evidence is produced. Do not describe checklists, templates or placeholders as completed deliverables.


## D1 — Project Charter deliverable

The submitted M1 charter defines one-quarter-ahead PAT margin as the primary analytical output and EBITDAR margin as the secondary operating indicator. It frames the problem as public-data company-level forecasting and scenario planning, with a simple historical baseline as the required comparator. See [M1 README](M1_D1_Project_Charter/README.md), [D1 evaluation record](M1_D1_Project_Charter/EVALUATION_RECORD.md) and [M1 deliverables index](M1_D1_Project_Charter/03_DELIVERABLES/README.md).
