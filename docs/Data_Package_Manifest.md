# Capstone Data Package — 30 October 2026

This manifest records the original 30 October data package, the canonical CP raw workbooks and the immutable D4-v1 quarterly input. The current CP(6).xlsx upload and CP Master Data(5).xlsx upload have been hash-verified as identical to the raw source workbooks already in GitHub. The newer Final_Quarterly_Data(3).xlsx is tracked as a local candidate; it is not yet uploaded or approved.

**Repository visibility:** this GitHub repository is public. The user confirmed permission to publish the supplied Bloomberg-derived files. The four workbooks were uploaded on 30 October 2026 in commit `11bffd420d9396896452fd7f3c8a0b425a0a9746`.

## Package contents

| Package path | Workbook | Sheets | Sheet dimensions (data rows × columns) |
|---|---|---|---|
| [`data/raw/CP(4).xlsx`](../data/raw/CP%284%29.xlsx) | Raw Bloomberg export | `IS`, `usd inr`, `cpi`, `wpi`, `co new`, `co new monthly` | IS: 59 × 42; USD/INR: 148 × 3; CPI: 147 × 3; WPI: 246 × 3; Brent daily: 3,000 × 3; Brent monthly: 148 × 3 |
| [`data/raw/CP Master Data(3).xlsx`](../data/raw/CP%20Master%20Data%283%29.xlsx) | Master indicator workbook | `USD INR`, `CPI inflation`, `WPI inflation`, `Oil benchmark(DAILY)`, `Oil benchmark(MONTHLY)`, `Financial source` | 117 × 2; 117 × 2; 117 × 2; 2,484 × 2; 117 × 2; 36 × 3 |
| [`data/processed/Final_Quarterly_Data(1).xlsx`](../data/processed/Final_Quarterly_Data%281%29.xlsx) | Final quarterly derived workbook — D4-v1 | `Final_Quarterly_Data`, `Calculation Audit`, `Data Quality Checks` | 38 × 12; 196 × 13; 20 × 6 |


## Data scope

This package contains the five working data categories:
1. Company financials — InterGlobe Aviation / IndiGo (`INDIGO IN`), Revenue, Net Income (GAAP), EBITDA.
2. Oil-price indicator — Dated Brent crude (`EUCRBRDT Index`), daily and monthly.
3. WPI inflation — `INBGWPIY Index`, monthly.
4. CPI inflation — `INFUTOTY Index`, monthly.
5. USD/INR — `USDINR REGN Curncy`, monthly.

There are no passenger counts, load factor, RPK/ASK or operations data in this package.

## Integrity checksums

| File | Size (bytes) | SHA-256 |
|---|---:|---|
| `CP(4).xlsx` | 157,304 | `208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e` |
| `CP Master Data(3).xlsx` | 71,747 | `30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474` |
| `Final_Quarterly_Data(1).xlsx` | 99,448 | `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c` |


## Data-quality notes carried forward

- The legacy `Financial source` sheet in the master workbook was previously found to be shifted by two quarters relative to the raw Bloomberg `IS` sheet. Rebuild margin values from raw statement dates/fields before modelling.
- Rows marked `Est` are estimates and must not be treated as actual target observations.
- The derived quarterly file uses `Quarter (Calendar)`; convert the key to the project's Indian fiscal quarters (Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar) before modelling.
- `EUCRBRDT Index` is Dated Brent crude, not Indian ATF and not IndiGo's negotiated fuel cost.
- Confirm Bloomberg field definitions, units, financial statement line-item mapping and publication/availability dates before any historical forecasting evaluation.
- These workbooks are preserved as supplied, not represented as a final cleaned or model-ready dataset.

## Related project files

- [Main project README](../README.md)
- [Actual Bloomberg source register](../data/source_register.csv)
- [Collection tracker](../data/collection_tracker.csv)
- [D2 data audit summary](D2_Data_Audit_Summary.md)
- [Current D3 executed notebook](../milestones/M3_D3_Exploratory_Data_Analysis/02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb)



## 7 November 2026 — CP workbook and Final Quarterly Data source links

- [CP raw source workbook](../data/raw/CP%284%29.xlsx): local `CP(6).xlsx` is hash-identical (SHA-256 `208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e`). Its sheets are `IS`, `usd inr`, `cpi`, `wpi`, `co new` and `co new monthly`. The quarterly company financial source is the `IS` tab.
- [CP Master Data source workbook](../data/raw/CP%20Master%20Data%283%29.xlsx): local `CP Master Data(5).xlsx` is hash-identical (SHA-256 `30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474`).
- [Final_Quarterly_Data(1).xlsx — D4-v1 pinned data source link](../data/processed/Final_Quarterly_Data%281%29.xlsx): this remains the immutable D4-v1 input (SHA-256 `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c`).
- `Final_Quarterly_Data(3).xlsx` is a separate local candidate (SHA-256 `87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970`). It has `Final_Quarterly_Data`, `Calculation Audit` and `Data Quality Checks` tabs, but is not uploaded. Do not use the D4-v1 link above as a link to candidate (3).

For full sheet-level mapping and cross-check URLs, see the [Data Collection Register](../data/DATA_COLLECTION_REGISTER.md).
