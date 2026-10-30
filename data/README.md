# Data folder

Keep downloaded/source data separate from processed/model-ready data.

- raw/: source copies, preserved unchanged when permitted.
- processed/: validated data aligned to the fiscal-quarter key.
- Document source URL, publication date, retrieval date, units, period, definitions and any revisions.

Do not commit personal data, access credentials, or raw files unless the source's redistribution terms permit it. When rights are unclear, keep data local and link to the original source instead. The latest Bloomberg workbooks have been committed to this repository with the user's confirmation of permission to publish. Raw source workbook: `data/raw/CP(4).xlsx`; master indicator workbook: `data/raw/CP Master Data(3).xlsx`; derived workbooks: `data/processed/Final_Quarterly_Data(1).xlsx` and `data/processed/EDA ANALYSIS(2).xlsx`. The D2 33-row modelling count is not approved because the financial source sheet was shifted by two quarters. Rebuild targets from raw actual financials, exclude estimates, compare derived dates against the latest raw CPI observations (through 2026-09-30), and then recompute the usable row count. See [D3 review notes](../reports/D3_eda/README.md).


## Bloomberg input mapping templates

The current source inventory records these Bloomberg security IDs: `INDIGO IN` (financials), `USDINR REGN Curncy` (monthly FX), `INFUTOTY Index` (monthly CPI inflation indicator), `INBGWPIY Index` (monthly WPI inflation indicator), and `EUCRBRDT Index` (Dated Brent crude, daily and monthly). Header-only mapping templates live in `data/templates/`.

These templates do not contain licensed data. The source workbooks stay local/private. The importer/master-builder mapping is not yet complete: do not run the current builder directly on the raw Bloomberg Excel workbook or assume the current quarterly output is model-ready.
