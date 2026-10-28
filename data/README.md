# Data folder

Keep downloaded/source data separate from processed/model-ready data.

- raw/: source copies, preserved unchanged when permitted.
- processed/: validated data aligned to the fiscal-quarter key.
- Document source URL, publication date, retrieval date, units, period, definitions and any revisions.

Do not commit personal data, access credentials, or raw files unless the source's redistribution terms permit it. When rights are unclear, keep data local and link to the original source instead. The Bloomberg workbooks and the working master dataset are held locally pending licence confirmation and reconciliation; they are intentionally not committed to the public repository. The D2 33-row modelling count is not approved because the financial source sheet was shifted by two quarters. Rebuild targets from raw actual financials, exclude estimates, compare derived dates against the latest raw CPI observations (through 2026-09-30), and then recompute the usable row count. See [D3 review notes](../reports/D3_eda/README.md).


## Bloomberg input mapping templates

The current source inventory records these Bloomberg security IDs: `INDIGO IN` (financials), `USDINR REGN Curncy` (monthly FX), `INFUTOTY Index` (monthly CPI inflation indicator), `INBGWPIY Index` (monthly WPI inflation indicator), and `EUCRBRDT Index` (Dated Brent crude, daily and monthly). Header-only mapping templates live in `data/templates/`.

These templates do not contain licensed data. The source workbooks stay local/private. The importer/master-builder mapping is not yet complete: do not run the current builder directly on the raw Bloomberg Excel workbook or assume the current quarterly output is model-ready.
