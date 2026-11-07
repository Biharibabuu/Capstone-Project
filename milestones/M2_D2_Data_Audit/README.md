# M2 / D2 — Data Audit

**Status:** DONE

## Brief
Audit data provenance, definitions, units, period coverage, missingness, duplicates, financial status, quality and permitted use before analysis/model development.

## Data used and stored
- Raw source workbook: `data/raw/CP(4).xlsx` and the milestone copy at [data/raw/CP(4).xlsx](data/raw/CP%284%29.xlsx).
- Master indicators: `data/raw/CP Master Data(3).xlsx` and the milestone copy at [data/raw/CP Master Data(3).xlsx](data/raw/CP%20Master%20Data%283%29.xlsx).
- Quarterly snapshot: [data/processed/Final_Quarterly_Data(1).xlsx](data/processed/Final_Quarterly_Data%281%29.xlsx).
- Audit evidence, data dictionary, source register and collection tracker are listed in MILESTONE_MANIFEST.csv.

## Workflow
1. Register all source files and source identifiers.
2. Record fields, units, frequency, coverage and collection date.
3. Check missingness, duplicates, invalid dates, estimates and data alignment.
4. Reconcile derived financial lines against raw statement fields.
5. Record checksums, quality issues, rights/redistribution status and approval decisions.
6. Publish the approved source package and handoff limitations to M3.

## Key findings and limits
- Raw financial and macro/market data cover revenue, net income, EBITDA, USD/INR, CPI, WPI and Dated Brent.
- Brent is a proxy, not IndiGo's realised ATF cost.
- The data lack passenger load factor, passenger yield, RPK/ASK and other operating measures.
- Historical release/availability timestamps are incomplete and must be treated as a limitation in forecasting.
- Newer file versions should be compared and rights-cleared before replacing approved data.

## Folder map
01_INPUTS source files and registers; 02_WORKING audit and data checks; 03_DELIVERABLES audit reports and dictionary; 04_EVIDENCE hashes/quality findings; 05_REFERENCES source definitions and validation sources; data/ stores milestone data copies.

## Handoff
M3 uses the approved data definitions and source data to create the EBITDA-only EDA panel. Do not use unapproved workbook versions without documented reconciliation.
