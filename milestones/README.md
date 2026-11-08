# Capstone Milestone Archive
### IndiGo Profitability Intelligence System

**Project objective:** Develop a reproducible forecasting workflow for IndiGo's next-quarter **EBITDA Margin**.  
**Primary target:** EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.  
**Current active milestone:** M4 / D4 — Modelling.

---

## Executive milestone overview

| Phase | Deliverable | Focus | Status | Milestone workspace |
|---|---|---|---|---|
| **01 — Project Foundation** | **D1 · Project Charter (M1)** | Business problem, EBITDA target, scope, stakeholders, risks and project plan | <badge color="success">Done</badge> | [Open M1 workspace →](M1_D1_Project_Charter/) |
| **01 — Project Foundation** | **D2 · Data Audit (M2)** | Source register, definitions, data quality, lineage, data dictionary and approval controls | <badge color="success">Done</badge> | [Open M2 workspace →](M2_D2_Data_Audit/) |
| **02 — Analysis & Modelling** | **D3 · EBITDA Margin EDA (M3)** | 38-quarter exploratory analysis, descriptive statistics, hypotheses and modelling handoff | <badge color="success">Done¹</badge> | [Open M3 workspace →](M3_D3_Exploratory_Data_Analysis/) |
| **02 — Analysis & Modelling** | **D4 · Modelling (M4)** | EBITDA target construction, baselines, candidate models, chronological validation and experiment tracking | <badge color="warning">In Progress</badge> | [Open M4 workspace →](M4_D4_Modelling/) |
| **03 — Evaluation & Delivery** | **D5 · Model Evaluation (M5)** | Rolling-origin backtesting, robustness, error analysis and uncertainty | <badge>Todo</badge> | [Open M5 workspace →](M5_D5_Model_Evaluation/) |
| **03 — Evaluation & Delivery** | **D6 · Deployment & Monitoring (M6)** | D5-approved model integration, API/UI testing, refresh and monitoring | <badge>Todo</badge> | [Open M6 workspace →](M6_D6_Deployment_Monitoring/) |
| **03 — Evaluation & Delivery** | **D7 · Final Communication (M7)** | Final report, model card, presentation, speaker notes and reproducible demo | <badge>Todo</badge> | [Open M7 workspace →](M7_D7_Final_Communication/) |

¹ M3's analysis handoff and saved notebook outputs are retained. A clean rerun remains pending the exact source workbook and reconciliation of the noted quarterly discrepancy. See M3's README for the current reproducibility caveat.

---

## Delivery workflow

```text
PHASE 01 · PROJECT FOUNDATION
D1 Project Charter  →  D2 Data Audit
          │
          ▼
PHASE 02 · ANALYSIS & MODELLING
D3 EBITDA Margin EDA  →  D4 EBITDA Modelling
                                  │
                                  ▼
PHASE 03 · EVALUATION & DELIVERY
D5 Model Evaluation  →  D6 Deployment & Monitoring  →  D7 Final Communication
```

**Current execution rule:** M1, M2 and M3 are complete; M4 is the only active workstream. M5–M7 are planned and must remain Todo until their deliverables are produced and reviewed.

---

## Milestone workspace standard

Every milestone follows the same evaluator-friendly structure:

| File / folder | Purpose |
|---|---|
| `README.md` | Brief, objective, status, exact inputs, workflow, outputs, limitations and next gate |
| `MILESTONE_CONTROL.md` | Scope, dependencies, acceptance criteria, risks and closure conditions |
| `DELIVERABLES_CHECKLIST.md` | Reviewable completion checklist |
| `MILESTONE_MANIFEST.csv` | File-level evidence inventory, paths and artifact status |
| `01_INPUTS/` | Source files, data contracts, brief and input register |
| `02_WORKING/` | Notebooks, scripts, transformations and working records |
| `03_DELIVERABLES/` | Formal milestone submission files |
| `04_EVIDENCE/` | Outputs, test results, metrics, review and verification evidence |
| `05_REFERENCES/` | Data sources, methodology, citations and technical references |
| `data/` | Milestone-specific dataset or exact versioned data snapshot, where applicable |

A folder or checklist is not evidence that work is complete. Manifests must distinguish committed files, pending files, missing inputs, placeholders and completed deliverables.

---

## Data ownership and target governance

The primary financial target throughout the current project is **EBITDA Margin (%) = EBITDA / Revenue from Operations × 100**.

| Milestone | Data and artifact responsibility |
|---|---|
| M1 · D1 | Defines target, business scope and data requirements; no analytical dataset required |
| M2 · D2 | Owns raw source workbooks, source register, data dictionary, data-quality findings, checksums and approval history |
| M3 · D3 | Owns the exact EBITDA-only EDA input, executed EDA notebook and analysis handoff |
| M4 · D4 | Owns the versioned modelling snapshot, target/feature engineering, splits, code, experiments, predictions and model outputs |
| M5 · D5 | Freezes the selected M4 candidate and input vintage; owns rolling-origin predictions, metrics and error analysis |
| M6 · D6 | Uses the D5-approved model and feature contract; owns API/UI integration, refresh and monitoring evidence |
| M7 · D7 | References approved versioned evidence; owns the final report, model card, presentation and demo package |

**Data controls**
- Preserve source workbooks as immutable inputs and record SHA-256 hashes for each approved version.
- Any derived or transformed dataset must identify its parent source version, transformation, date, units and row coverage.
- Record actual versus estimate status and observation versus publication/availability dates.
- Do not use future or unpublished values in historical model features.
- Dated Brent is a benchmark proxy; do not describe it as IndiGo's realised ATF price.
- Net Income may exist in the original company statement source for audit/reconciliation, but it is not the project's target or a model feature.
- Do not silently substitute a different quarterly workbook or mix versions across EDA and modelling.

---

## Milestone registers and project governance

- [Milestone register](MILESTONE_REGISTER.csv) — status, evidence, limitations and next gate for D1–D7.
- [GitHub project-board workflow](../docs/GITHUB_PROJECT_BOARD.md) — Todo, In Progress and Done tracking.
- [Project status and work log](../docs/PROJECT_STATUS_AND_WORKLOG.md) — current execution record.
- [Workflow and data governance](../docs/WORKFLOW_AND_DATA_GOVERNANCE.md) — point-in-time, data lineage and reproducibility rules.
- [Artifact audit](ARTIFACT_AUDIT_2026-11-07.md) · [Artifact inventory](ARTIFACT_INVENTORY_2026-11-07.csv).

---

## Review and closure policy

1. Keep M4 as the only active milestone until its EBITDA-margin model development and experiment evidence meet the exit criteria.
2. Start M5 only when M4 has a frozen, documented candidate/baseline and modelling data version.
3. Start M6 only after M5 approves the model and feature contract.
4. Complete M7 only after evaluation and deployment evidence are available.
5. Mark a milestone Done only when its deliverables exist at the manifest paths, have been reviewed and are reproducible to the extent stated in the milestone README.
6. Update the milestone README, register, GitHub issue and project board together whenever status changes.

