# M4 / D4 — Modelling and Forecasting

**Status:** IN PROGRESS

## 1. Purpose
Build transparent forecasting baselines and candidate models for the approved next-quarter profitability target.

## 2. Inputs and dependencies
M2 approved data snapshot, M3 EDA insights, target/feature definitions and chronological split protocol.

## 3. Required outputs
Training pipeline, baseline and candidate models, tuning log, reproducible notebook, tests, metrics, predictions, model-selection report and environment/data manifests.

## 4. Acceptance criteria
No leakage; chronological validation; baseline comparison; reproducible run; limitations and model-selection rationale documented.

## 5. Governance and reproducibility
- Keep source files immutable; create versioned derived outputs.
- Record file name, source, retrieval date, observation period, units, owner, access/redistribution decision and SHA-256 for each dataset.
- Keep code, notebooks, reports, test evidence and data manifests in their designated subfolders.
- Never commit credentials, tokens, personal data or source material without redistribution authorization.
- Record all scope or data-definition changes in the project change log and update affected milestone documents.

## 6. Current next action
Current active milestone: continue D4 modelling work, preserve prior experiment snapshots and record every run in the experiment log.
