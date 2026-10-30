# Capstone Data Package — 30 October 2026

This manifest describes the latest four Excel workbooks supplied for the IndiGo Profitability Intelligence capstone. A local archive named `IndiGo_Capstone_Project_Data_Pack.zip` was prepared with the workbooks unchanged, plus `README_DATA_PACK.md`, `manifest.json` and `SHA256SUMS.txt`.

**Repository visibility:** this GitHub repository is public. The original Bloomberg export and Bloomberg-derived data workbooks are therefore not committed here unless the applicable Bloomberg/institutional agreement expressly permits public redistribution. The archive is available as a downloadable attachment in the current ChatGPT conversation.

## Package contents

| Package path | Workbook | Sheets | Sheet dimensions (data rows × columns) |
|---|---|---|---|
| `01_Raw_Bloomberg_Export/CP(4).xlsx` | Raw Bloomberg export | `IS`, `usd inr`, `cpi`, `wpi`, `co new`, `co new monthly` | IS: 59 × 42; USD/INR: 148 × 3; CPI: 147 × 3; WPI: 246 × 3; Brent daily: 3,000 × 3; Brent monthly: 148 × 3 |
| `02_Master_Indicators/CP Master Data(3).xlsx` | Master indicator workbook | `USD INR`, `CPI inflation`, `WPI inflation`, `Oil benchmark(DAILY)`, `Oil benchmark(MONTHLY)`, `Financial source` | 117 × 2; 117 × 2; 117 × 2; 2,484 × 2; 117 × 2; 36 × 3 |
| `03_Quarterly_Derived/Final_Quarterly_Data(1).xlsx` | Final quarterly derived workbook | `Final_Quarterly_Data`, `Calculation Audit`, `Data Quality Checks` | 38 × 12; 196 × 13; 20 × 6 |
| `04_EDA_Analysis/EDA ANALYSIS(2).xlsx` | Flat EDA input | `Sheet1` | 38 × 9 |

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
| `EDA ANALYSIS(2).xlsx` | 13,233 | `8aef5dde95d243aa01e7026c6ea1a977964a1af0da1241a2c1db19f07482b77e` |

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
- [D3 EDA notebook](../notebooks/03_eda.ipynb)

