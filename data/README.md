# Data folder

Keep downloaded/source data separate from processed/model-ready data.

- raw/: source copies, preserved unchanged when permitted.
- processed/: validated data aligned to the fiscal-quarter key.
- Document source URL, publication date, retrieval date, units, period, definitions and any revisions.

Do not commit personal data, access credentials, or raw files unless the source's redistribution terms permit it. When rights are unclear, keep data local and link to the original source instead. The Bloomberg workbooks and the working master dataset are held locally pending licence confirmation and reconciliation; they are intentionally not committed to the public repository. The D2 33-row modelling count is not approved because the financial source sheet was shifted by two quarters. Rebuild targets from raw actual financials, exclude estimates, resolve the CPI date anomaly and then recompute the usable row count. See [D3 review notes](../reports/D3_eda/README.md).
