# M2 / D2 — Data Package

**Purpose:** Preserve the audited source datasets, data definitions, quality controls and provenance that support later milestones.

## Files stored in this milestone

| File | Role | SHA-256 |
|---|---|---|
| [CP(4).xlsx](raw/CP%284%29.xlsx) | Raw Bloomberg export: statement, FX, CPI, WPI and dated Brent source sheets | 208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e |
| [CP Master Data(3).xlsx](raw/CP%20Master%20Data%283%29.xlsx) | Consolidated monthly/daily indicator series and legacy financial-source sheet | 30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474 |
| [Final_Quarterly_Data(1).xlsx](processed/Final_Quarterly_Data%281%29.xlsx) | Quarterly derived data and calculation/quality audit; 38 observations + two audit sheets | 87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970 |

## Data definitions and lineage

- Company: InterGlobe Aviation / IndiGo (INDIGO IN); Revenue, Net Income (GAAP), EBITDA.
- Currency: USD/INR (USDINR REGN Curncy, monthly).
- CPI: INFUTOTY Index.
- WPI: INBGWPIY Index.
- Oil proxy: Dated Brent (EUCRBRDT Index), daily and monthly; this is not IndiGo's realised ATF price.
- Field IDs, units, frequency and coverage are recorded in the [data dictionary](../IndiGo_Data_Dictionary.csv), [source register](../source_register.csv) and [package manifest](../Data_Package_Manifest.md).

## Audit rules

1. Treat source workbooks as immutable evidence.
2. Use actual/reported financial periods only; exclude estimates from realised outcomes.
3. Use Indian fiscal quarters consistently: Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar.
4. Retain observation date, publication/availability date where known, source identifier, field, unit and quality flag.
5. Record a checksum for every new derived dataset and retain parent source hashes.
6. Newer or unreconciled workbooks stay quarantined until documented comparison and approval.

## Data handoff

- M3 uses the EBITDA-only quarterly analysis panel in the M3 data folder.
- M4 uses the approved quarterly snapshot and documented macro/market features; its exact input snapshot is also stored under M4/data.
- M5 and later milestones must record the exact M4/D5 model-ready data vintage they consume.
