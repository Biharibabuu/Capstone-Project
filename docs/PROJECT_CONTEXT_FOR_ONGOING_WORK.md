# Ongoing Project Context — Working Instructions

Use this file as the persistent working brief for future tasks on the IndiGo Profitability Intelligence capstone.

## Project identity
- Project: IndiGo Profitability Intelligence System.
- Course: PGDM Business Analytics capstone, modules M1–M7 / deliverables D1–D7.
- Team: Nikhil Raj, Krishan Sharma and K. Shreya.
- Adopted target: one-quarter-ahead EBITDA Margin, defined as EBITDA divided by Revenue from Operations × 100.
- Purpose: forecast IndiGo business profitability, not stock price.

## Current source of truth
1. GitHub repository: [Biharibabuu/Capstone-Project](https://github.com/Biharibabuu/Capstone-Project), branch `main`.
2. [Project Status and Work Log](PROJECT_STATUS_AND_WORKLOG.md) for completed, in-progress and planned work.
3. [Workflow and Data Governance](WORKFLOW_AND_DATA_GOVERNANCE.md) for data definitions, time rules, quality controls, versioning and architecture.
4. [Milestone register](../milestones/MILESTONE_REGISTER.csv) for milestone status.
5. [D4-v1 record](../milestones/M4_D4_Modelling/README.md) for the locked first modelling experiment.
6. [30-Oct data package manifest](Data_Package_Manifest.md) for the earlier four-workbook version committed to GitHub.

## Non-negotiable project rules
- Preserve raw data unchanged.
- Preserve D4-v1 input `Final_Quarterly_Data(1).xlsx` with SHA-256 `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c`.
- Never substitute a newer file into an old experiment. New inputs require a new version, hash, run log and metrics.
- Do not treat rows marked `Est` as realised actuals.
- Do not treat repeated PAT/EBITDA margins in the first two rows of the latest derived quarterly workbook as real outcomes; its status field says unavailable.
- Do not use the legacy `Financial source` master sheet as authoritative financial labels. Reconcile directly to raw Bloomberg `IS` periods and dates.
- Use Indian fiscal quarters: Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar. Keep calendar-quarter and fiscal-quarter labels distinct.
- Forecast features must be available by the forecast as-of date. Observation date alone does not establish publication/availability.
- Label `EUCRBRDT Index` as Dated Brent crude proxy, not Indian ATF.
- The currently reviewed data do not contain passenger count, passenger load factor, RPK or ASK. Do not say these have been collected.
- The current financial export establishes EBITDA, not EBITDAR. EBITDA Margin is the adopted modelling target; do not substitute EBITDAR Margin or PAT Margin.
- Keep Bloomberg raw or derived data private unless redistribution rights for that exact dataset and output are confirmed.
- Do not claim an artifact has been uploaded or deployed unless the exact repository path/commit or running test is verified.

## Current confirmed modelling result
D4-v1 has been executed and documented. It used 35 supervised observations with train/validation/test sizes 21/6/8. Validation MAE/RMSE were:
- Persistence baseline: 12.18 / 13.92 percentage points.
- Best Ridge: 42.62 / 43.94 percentage points.
- Best Random Forest: 51.95 / 54.15 percentage points.

Persistence was selected. Locked-test MAE/RMSE were 11.53 / 14.20 percentage points, with 0% improvement over persistence. No trained ML artifact was selected. Be transparent about this result.

## Current work priority
1. Finish M2 reconciliation of the latest quarterly derivative from raw financial periods.
2. Freeze the fiscal-quarter and as-of-date master dataset, with a checksum and calculation audit.
3. Rerun M3 EDA on that approved dataset.
4. Complete M5 rolling-origin, point-in-time, error and uncertainty evaluation.
5. Integrate the D5-approved rule/model into the existing M6 API/frontend scaffold.
6. Complete M7 report, model card, presentation, speaker notes and demonstration.

## How to maintain the project record
For every new user upload, code change, decision, experiment or submission:
- Record the received/created date.
- Record exact filename and repository/local location.
- Record SHA-256 for binary data.
- Record worksheet names, row/column dimensions and date coverage for workbooks.
- Classify it as raw source, derived candidate, approved dataset, experiment output, report or final deliverable.
- Record what changed, why it changed, what was validated, known limitations and next action.
- Update the milestone register and README when project status changes.
- Keep a chronological work log; do not silently replace earlier decisions or evidence.

When explaining any step, use clear business-school language and explain finance/data terminology in plain language. Prefer evidence tables, explicit decisions and reproducible instructions over unsupported claims.


## Adopted target scope (8 November 2026)

The project team's adopted primary modelling target is next-quarter EBITDA Margin (%) = EBITDA / Revenue from Operations × 100. The original D1 PDF retains its initial PAT-margin proposal as historical submission evidence; the subsequent scope decision is recorded in the M1 evaluation record and editable Project Charter. D3 EDA is EBITDA-focused. The current M4 experiment must be independently built for EBITDA Margin; the older D4-v1 code and results are PAT-target legacy evidence and must not be represented as EBITDA performance.
