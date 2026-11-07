# M2 / D2 — Data Audit

Status: Done. This folder records dataset provenance, definitions, coverage, known gaps, quality checks, governance and model-readiness limitations.

Data categories: IndiGo quarterly revenue/PAT/EBITDA; USD/INR; CPI; WPI; Dated Brent crude benchmark. Brent is a proxy, not IndiGo's realised ATF cost. The supplied company data contain EBITDA, not EBITDAR.

Files include the D2 audit summary, feasibility audit, data package manifest, source register, collection tracker and data dictionary.

Canonical raw and processed workbooks remain in the repository's data/raw and data/processed folders to avoid duplicate competing copies. Their names, sizes and checksums are recorded in Data_Package_Manifest.md.

Key limitations: D2 notes issues with the supplied derived financial alignment and estimate rows. D4 uses the identified workbook and filters to records marked Reported (original value). Historical publication timestamps remain unavailable.
## Standard folder structure

- `data/` — canonical dataset index and approval/quarantine rules.
- `reports/` — audit report and review records.
- `references/` — source definitions and supporting documentation.
- `MILESTONE_CONTROL.md` — scope, inputs, outputs, acceptance criteria and next action.
- `DELIVERABLES_CHECKLIST.md` — review and closure checklist.
- `MILESTONE_MANIFEST.csv` — file-by-file record.

The raw workbooks are stored once under the repository's `data/raw/` folder and processed datasets under `data/processed/`; the `data/README.md` in this milestone links to those canonical copies. Do not duplicate or overwrite them.


## Standard evaluation structure

- [01_INPUTS](01_INPUTS/README.md)
- [02_WORKING](02_WORKING/README.md)
- [03_DELIVERABLES](03_DELIVERABLES/README.md)
- [04_EVIDENCE](04_EVIDENCE/README.md)
- [05_REFERENCES](05_REFERENCES/README.md)

See MILESTONE_CONTROL.md, DELIVERABLES_CHECKLIST.md, EVALUATION_RECORD.md and MILESTONE_MANIFEST.csv.
