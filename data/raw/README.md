# Raw Source Data
### M2 / D2 — Data Audit ownership

This folder contains unchanged original company and macro/market source exports. M2 / D2 is the data steward for provenance, definitions, units, period coverage, quality and rights.

## Current source workbooks

| File | Contents | Source identifiers | Frequency |
|---|---|---|---|
| [CP(4).xlsx](CP%284%29.xlsx) | IndiGo financial statement (IS), USD/INR, CPI, WPI and Dated Brent daily/monthly sheets | INDIGO IN, USDINR REGN Curncy, INFUTOTY Index, INBGWPIY Index, EUCRBRDT Index | Quarterly / monthly / daily |
| [CP Master Data(3).xlsx](CP%20Master%20Data%283%29.xlsx) | Consolidated historical indicators and legacy financial-source sheet | Same project source series | Mixed |

These are original source exports, not modelling-ready panels. Preserve their bytes and filenames; record retrieval date, field ID, sheet, original units, coverage and SHA-256.

## Target and use controls

The current project target is next-quarter EBITDA Margin = EBITDA / Revenue from Operations × 100. Original company statement files may contain other financial lines for audit/reconciliation; their presence does not make them model targets or features.

The master workbook's Financial source tab was found to be shifted by two quarters relative to raw IS. Rebuild financial labels from raw IS dates and values; do not use the misaligned tab for modelling.

## Source controls

- Do not edit or overwrite raw files.
- Exclude rows marked Est from realised target labels.
- Verify EBITDA and Revenue from Operations definitions against company reports.
- Record observation and publication/availability dates separately.
- Confirm redistribution permissions before publishing licensed exports.
- Compare new files against existing source hashes before promotion.
- Maintain the repository-level source register and collection tracker.

## Milestone use

M2 audits and approves this source package. M3 uses approved source definitions for the EBITDA-only EDA panel. M4 builds a versioned modelling table from approved actuals and indicators. M5–M7 reference upstream versions and do not duplicate raw sources.