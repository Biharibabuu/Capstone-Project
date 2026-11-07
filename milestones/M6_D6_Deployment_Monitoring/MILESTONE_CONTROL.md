# M6 / D6 — Deployment and Monitoring

**Status:** TODO

## 1. Purpose
Expose the D5-approved forecast through a tested interface and monitor data/model health.

## 2. Inputs and dependencies
D5-approved model, API/frontend scaffold, live-source contracts and deployment configuration.

## 3. Required outputs
Integrated API/UI, refresh/store workflow, API tests, monitoring thresholds, logs, release instructions and demo evidence.

## 4. Acceptance criteria
End-to-end tested; secrets protected; freshness, missingness, failures, model version and forecast records monitored.

## 5. Governance and reproducibility
- Keep source files immutable; create versioned derived outputs.
- Record file name, source, retrieval date, observation period, units, owner, access/redistribution decision and SHA-256 for each dataset.
- Keep code, notebooks, reports, test evidence and data manifests in their designated subfolders.
- Never commit credentials, tokens, personal data or source material without redistribution authorization.
- Record scope or data-definition changes in the project change log and update affected milestone documents.

## 6. Current next action
Do not integrate an unapproved D4 candidate; wait for D5 approval.
