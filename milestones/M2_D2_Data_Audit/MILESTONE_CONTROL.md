# M2 / D2 — Data Collection and Audit

**Status:** DONE

## 1. Purpose
Record provenance, definitions, units, coverage, quality, rights and fitness of each dataset.

## 2. Inputs and dependencies
Authorized raw company financial and macro/market source workbooks, source register and collection tracker.

## 3. Required outputs
Data dictionary, source register, collection tracker, data-quality report, package manifest, checksum register and approved/rejected dataset decisions.

## 4. Acceptance criteria
Every input has provenance, units, date/frequency, quality flags, rights decision and a reproducible version/hash; unresolved limitations are visible.

## 5. Governance and reproducibility
- Keep source files immutable; create versioned derived outputs.
- Record file name, source, retrieval date, observation period, units, owner, access/redistribution decision and SHA-256 for each dataset.
- Keep code, notebooks, reports, test evidence and data manifests in their designated subfolders.
- Never commit credentials, tokens, personal data or source material without redistribution authorization.
- Record all scope or data-definition changes in the project change log and update affected milestone documents.

## 6. Current next action
Use the audited canonical inputs for M4; any newer workbook remains quarantined until reconciled and rights-cleared.
