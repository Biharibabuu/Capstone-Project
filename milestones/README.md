# Capstone Milestone Archive
### IndiGo Profitability Intelligence System

**Project objective:** Develop a reproducible forecasting workflow for IndiGo's next-quarter **EBITDA Margin**.  
**Primary target:** EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.  
**Current active milestone:** M4 / D4 — Modelling.

---

## Executive milestone overview

| Phase | Deliverable | Focus | Status | Workspace |
|---|---|---|---|---|
| **01 · Project Foundation** | **D1 · Project Charter (M1)** | Business problem, EBITDA target, scope, stakeholders, risks and delivery plan | **Done** | [M1 workspace](M1_D1_Project_Charter/) |
| **01 · Project Foundation** | **D2 · Data Audit (M2)** | Source register, definitions, data quality, lineage, data dictionary and approval controls | **Done** | [M2 workspace](M2_D2_Data_Audit/) |
| **02 · Analysis & Modelling** | **D3 · EBITDA Margin EDA (M3)** | 38-quarter exploratory analysis, distributions, hypotheses, insights and modelling handoff | **Done¹** | [M3 workspace](M3_D3_Exploratory_Data_Analysis/) |
| **02 · Analysis & Modelling** | **D4 · EBITDA Margin Modelling (M4)** | Target construction, baseline/challenger models, chronological validation and experiment tracking | **In Progress** | [M4 workspace](M4_D4_Modelling/) |
| **03 · Evaluation & Delivery** | **D5 · Model Evaluation (M5)** | Rolling-origin backtesting, robustness, error analysis and uncertainty | **Todo** | [M5 workspace](M5_D5_Model_Evaluation/) |
| **03 · Evaluation & Delivery** | **D6 · Deployment & Monitoring (M6)** | D5-approved model integration, API/UI testing, refresh and monitoring | **Todo** | [M6 workspace](M6_D6_Deployment_Monitoring/) |
| **03 · Evaluation & Delivery** | **D7 · Final Communication (M7)** | Final report, model card, presentation, speaker notes and reproducible demo | **Todo** | [M7 workspace](M7_D7_Final_Communication/) |

¹ M3 analysis handoff and saved notebook outputs are retained. A clean rerun remains pending the exact source workbook and reconciliation of the noted quarterly discrepancy. See the M3 README for the reproducibility caveat.

---

## Delivery workflow

```text
PHASE 01 · PROJECT FOUNDATION
D1 Project Charter  →  D2 Data Audit
          │
          ▼
PHASE 02 · ANALYSIS & MODELLING
D3 EBITDA Margin EDA  →  D4 EBITDA Margin Modelling
                                      │
                                      ▼
PHASE 03 · EVALUATION & DELIVERY
D5 Model Evaluation  →  D6 Deployment & Monitoring  →  D7 Final Communication
```

**Execution rule:** M1–M3 are complete, with the stated M3 reproducibility caveat. M4 is the only active workstream. M5–M7 are planned and must remain Todo until their deliverables are produced and reviewed.

---

## Standard milestone workspace

Every milestone follows the same formal structure:

| File / folder | Required contents |
|---|---|
| `README.md` | Brief, objective, status, inputs, workflow, outputs, limitations and next gate |
| `MILESTONE_CONTROL.md` | Scope, dependencies, acceptance criteria, risks and closure conditions |
| `DELIVERABLES_CHECKLIST.md` | Reviewable completion checklist |
| `MILESTONE_MANIFEST.csv` | File-level inventory, exact paths, artifact status and evidence |
| `01_INPUTS/` | Brief, source data, input register and data contract |
| `02_WORKING/` | Notebooks, scripts, transformations and working records |
| `03_DELIVERABLES/` | Formal milestone submission files (PDF, DOCX, XLSX, notebook or application deliverables as relevant) |
| `04_EVIDENCE/` | Outputs, tests, metrics, review and verification evidence |
| `05_REFERENCES/` | Data sources, methodology, citations and technical references |
| `data/` | Exact milestone-specific dataset or versioned snapshot, where applicable |

**Artifact rule:** a folder, checklist or README is not proof that a deliverable exists. The manifest must distinguish committed files, received-but-not-uploaded files, missing inputs, placeholders and completed artifacts. Never claim a PDF/DOCX/XLSX/notebook has been uploaded unless it exists at the stated GitHub path.

---

## Milestone-by-milestone data and document allocation

| Milestone | Required files and data in this workspace |
|---|---|
| **M1 · D1 Project Charter** | Current EBITDA-focused charter (DOCX/PDF if submitted), editable charter, scope decision, roles/responsibility matrix, meeting log, assumptions and risk register. No analytical dataset required. |
| **M2 · D2 Data Audit** | Raw/source workbooks, quarterly source snapshot, data dictionary, source register, collection tracker, audit summary, feasibility audit, data-quality evidence, workbook inventory and SHA-256 manifest. |
| **M3 · D3 EBITDA EDA** | Exact 38-quarter EBITDA-only input panel, executed EDA notebook, charts/tables/statistical outputs, hypotheses, insight log, review notes and M4 handoff. |
| **M4 · D4 EBITDA Modelling** | Approved M2/M3 data snapshots, target/feature engineering, modelling notebook/scripts, baseline and challenger experiments, tests, environment/data manifests, run logs, metrics, predictions and modelling report. |
| **M5 · D5 Model Evaluation** | Frozen M4 model and dataset version, rolling-origin notebook/scripts, prediction/error files, metrics, robustness tests, uncertainty analysis and evaluation report. |
| **M6 · D6 Deployment & Monitoring** | D5-approved model package, feature contract, API/backend, frontend, refresh/store workflow, API/UI tests, monitoring thresholds, logs, runbook and demo evidence. |
| **M7 · D7 Final Communication** | Final report, executive summary, model card, presentation deck, speaker notes, demo runbook, references and release record. |

### Data ownership and target governance

The current project's only primary forecasting target is:

**EBITDA Margin (%) = EBITDA / Revenue from Operations × 100**

- M2 owns the audited raw source data and provenance records.
- M3 owns the exact EDA analysis input and outputs.
- M4 owns the versioned modelling dataset and all model experiments.
- M5 freezes and evaluates the selected M4 model and its exact data vintage.
- M6 consumes the D5-approved model and feature contract; it does not independently redefine the target.
- M7 reports only approved, traceable evidence and results.
- Net Income may appear in original source statements for audit/reconciliation, but it is not the project's forecasting target or a model feature.
- Dated Brent is a crude-oil benchmark proxy, not IndiGo's realised ATF price.
- Every new data version must record source, units, observation period, availability date where known, transformation, approval status and SHA-256.
- Do not mix dataset versions or use information unavailable at the historical forecast origin.

---

## Project registers and governance

- [Milestone register](MILESTONE_REGISTER.csv) — status, evidence, limits and next gate for D1–D7.
- [GitHub project-board workflow](../docs/GITHUB_PROJECT_BOARD.md) — Todo, In Progress and Done tracking.
- [Project status and work log](../docs/PROJECT_STATUS_AND_WORKLOG.md) — execution record.
- [Workflow and data governance](../docs/WORKFLOW_AND_DATA_GOVERNANCE.md) — data lineage, point-in-time and reproducibility controls.
- [Artifact audit](ARTIFACT_AUDIT_2026-11-07.md) · [Artifact inventory](ARTIFACT_INVENTORY_2026-11-07.csv).

---

## Review and closure rules

1. M4 remains the only active milestone until its EBITDA-margin modelling and experiment evidence meet the exit criteria.
2. M5 begins only after M4 has a frozen, documented candidate/baseline and modelling data version.
3. M6 begins only after M5 approves the model and feature contract.
4. M7 is completed only after evaluation and deployment evidence are available.
5. A milestone is marked Done only when its deliverables exist at the manifest paths, have been reviewed and are reproducible to the extent stated in its README.
6. Update the milestone README, register, GitHub issue and project board together whenever a status changes.
