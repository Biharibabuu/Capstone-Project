# M2 / D2 — Data Audit

Status: Completed. This folder records dataset provenance, definitions, coverage, known gaps, quality checks, governance and model-readiness limitations.

Data categories: IndiGo quarterly revenue/PAT/EBITDA; USD/INR; CPI; WPI; Dated Brent crude benchmark. Brent is a proxy, not IndiGo's realised ATF cost. The supplied company data contain EBITDA, not EBITDAR.

Files include the D2 audit summary, feasibility audit, data package manifest, source register, collection tracker and data dictionary.

Canonical raw and processed workbooks remain in the repository's data/raw and data/processed folders to avoid duplicate competing copies. Their names, sizes and checksums are recorded in Data_Package_Manifest.md.

Key limitations: D2 notes issues with the supplied derived financial alignment and estimate rows. D4 uses the identified workbook and filters to records marked Reported (original value). Historical publication timestamps remain unavailable.