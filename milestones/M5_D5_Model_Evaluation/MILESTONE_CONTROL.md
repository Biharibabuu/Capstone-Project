# M5 / D5 — Model Evaluation and Robustness

**Status:** TODO

## 1. Purpose
Evaluate forecast performance robustly over time and across regimes.

## 2. Inputs and dependencies
Frozen D4 model candidates, approved dataset vintages, release-date metadata and baseline.

## 3. Required outputs
Rolling-origin backtest, error analysis, uncertainty assessment, robustness memo and model card draft.

## 4. Acceptance criteria
Time-aware evaluation is reproducible; point-in-time limitations and baseline-relative performance are explicit.

## 5. Governance and reproducibility
- Keep source files immutable; create versioned derived outputs.
- Record file name, source, retrieval date, observation period, units, owner, access/redistribution decision and SHA-256 for each dataset.
- Keep code, notebooks, reports, test evidence and data manifests in their designated subfolders.
- Never commit credentials, tokens, personal data or source material without redistribution authorization.
- Record all scope or data-definition changes in the project change log and update affected milestone documents.

## 6. Current next action
Start only after D4 model candidates and split protocol are stable.
