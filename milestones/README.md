# Capstone Milestone Archive

**Project:** IndiGo Profitability Intelligence System  
**Adopted project target:** Next-quarter EBITDA Margin = EBITDA / Revenue from Operations × 100  
**Active milestone:** M4 / D4 — Modelling

This is the evaluator-facing delivery archive. Each milestone has its own brief, workflow, evidence checklist, control record and manifest. Each README explains purpose, inputs, outputs, workflow, acceptance gate and data/artifacts used.

## Milestone status

| Order | Milestone | Status | Primary folder |
|---:|---|---|---|
| M1 | D1 Project Charter | Done — original PDF records initial PAT proposal; adopted project target is EBITDA Margin | [M1_D1_Project_Charter](M1_D1_Project_Charter/) |
| M2 | D2 Data Audit | Done | [M2_D2_Data_Audit](M2_D2_Data_Audit/) |
| M3 | D3 EBITDA Margin EDA | Completed — aligned with adopted project target | [M3_D3_Exploratory_Data_Analysis](M3_D3_Exploratory_Data_Analysis/) |
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
- Supporting folders: `01_INPUTS/`, `02_WORKING/`, `03_DELIVERABLES/`, `04_EVIDENCE/`, `05_REFERENCES/`.

## Data placement and ownership

- M1: project charter, target definition and scope decisions.
- M2: raw/source data and audit records.
- M3: exact EDA input panel and EBITDA Margin EDA notebook/review evidence.
- M4: exact modelling input snapshot, features, run evidence, predictions and model outputs for EBITDA Margin. The earlier PAT-margin D4-v1 is retained as legacy evidence only.
- M5: frozen evaluation input vintage, rolling-origin predictions and error analysis for EBITDA Margin.
- M6: approved EBITDA model package and deployment/configuration evidence; no duplicate training dataset.
- M7: final approved reports/slides/demo and version references.

Where a source file is shared, M2 holds the source and downstream milestones hold a clearly identified snapshot or data index with source version and SHA-256. Do not silently copy, rename or alter licensed source data.

## D1 initial proposal and adopted project scope

The submitted M1 PDF originally proposed PAT Margin as the primary analytical output and EBITDAR Margin as a secondary operating indicator. The project team subsequently adopted **EBITDA Margin** as the primary target for all subsequent project work (D3–D7). The PDF is preserved unchanged; this scope decision is recorded in [M1 Evaluation Record](M1_D1_Project_Charter/EVALUATION_RECORD.md) and [editable Project Charter](../docs/Project_Charter.md). EBITDA and EBITDAR must not be treated as the same measure.

## Registers and governance

- [Milestone register](MILESTONE_REGISTER.csv)
- [Artifact audit](ARTIFACT_AUDIT_2026-11-07.md)
- [Artifact inventory](ARTIFACT_INVENTORY_2026-11-07.csv)
- [Project board workflow](../docs/GITHUB_PROJECT_BOARD.md)
- [Project status and work log](../docs/PROJECT_STATUS_AND_WORKLOG.md)

M5–M7 are planning folders only until evidence is produced. Do not describe checklists, templates or placeholders as completed deliverables.
