# GitHub Project Board and Delivery Workflow

**Project:** IndiGo Profitability Intelligence  
**Current active milestone:** M4 / D4 — Modelling  
**Board columns:** Todo · In Progress · Done

## Done

| Work item | Record | Evidence |
|---|---|---|
| M1 / D1 — Project Charter | [Issue #1](../issues/1) | `milestones/M1_D1_Project_Charter/` |
| M2 / D2 — Data Audit | [Issue #2](../issues/2) | `milestones/M2_D2_Data_Audit/` |
| M3 / D3 — EBITDA-only EDA | [Issue #3](../issues/3) | `milestones/M3_D3_Exploratory_Data_Analysis/` |

## In Progress

| Work item | Record | Current focus |
|---|---|---|
| M4 / D4 — EBITDA-margin Modelling | [Issue #4](../issues/4) | Build current EBITDA-target modelling pipeline; legacy PAT D4-v1 results remain historical only |

## Todo

| Work item | Record | Planned output |
|---|---|---|
| M5 / D5 — Model Evaluation | [Issue #6](../issues/6) | Rolling-origin backtest, point-in-time controls, error analysis and uncertainty |
| M6 / D6 — Deployment and Monitoring | [Issue #5](../issues/5) | Integrate D5-approved model; API/UI tests, freshness/data health, logging and monitoring |
| M7 / D7 — Final Communication | [Issue #7](../issues/7) | Final report, model card, presentation, speaker notes and demo |

## Workflow

M1 Charter → M2 Data Audit → M3 EBITDA EDA → M4 Modelling → M5 Evaluation → M6 Deployment/Monitoring → M7 Final Communication.

## Board rules

1. The GitHub Project Status field controls the visible columns; issue open/closed state is separate.
2. M1, M2 and M3 are Done. M4 is the only active milestone. M5, M6 and M7 are Todo.
3. Close an issue and move its card to Done only after deliverables are committed, reproducible and reviewed.
4. Treat D4-v1 as a historical PAT experiment; do not label it as an EBITDA model or carry its metrics forward as current-model performance.
5. Keep README, this workflow, milestone register and issue bodies synchronized.
