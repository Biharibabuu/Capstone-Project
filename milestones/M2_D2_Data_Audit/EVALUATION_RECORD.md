# M2 / D2 — Data Audit: Evaluation Record

**Status:** Completed for the 30-Oct-2026 workbook package. Newer 7-Nov receipts are listed but not reconciled.

## Data inventory
| Data group | Bloomberg identifier | Intended use | Limitation |
|---|---|---|---|
| IndiGo financials | INDIGO IN; Revenue and EBITDA (Net Income retained as source audit field only) | Primary target: EBITDA margin = EBITDA / Revenue from Operations × 100 | EBITDAR is not established in the supplied data |
| USD/INR | USDINR REGN Curncy | Currency indicator | Historical release timing to verify |
| CPI | INFUTOTY Index | Inflation | Series/base and release timing to verify |
| WPI | INBGWPIY Index | Inflation | Series/base and release timing to verify |
| Oil | EUCRBRDT Index, Dated Brent | Fuel-price proxy | Not Indian ATF/realised airline fuel cost |

The audited package does not include passenger counts, passenger load factor, RPK or ASK.

## Audit findings and controls
1. The master workbook's legacy Financial source sheet is shifted by **two quarters** relative to raw Bloomberg IS. Rebuild financial outcomes directly from raw IS.
2. Rows marked Est are estimates, not realised EBITDA-margin labels.
3. The earlier 33-row training count was provisional. D4 documents 38 source rows, two excluded rows and 35 supervised examples for its pinned snapshot.
4. Lag/target missingness can be structural; do not mechanically impute.
5. Retain plausible extreme oil/profitability events, including COVID losses, with documented sensitivity review.
6. Preserve source dates. Historical publication timestamps are missing for some variables; lagging does not prove as-of availability.

## Files in the M2 folder / canonical paths
- D2_Data_Audit_Summary.md — audit findings and quality decisions.
- Data_Feasibility_Audit.md — source feasibility.
- Data_Package_Manifest.md — 30-Oct sheet inventory and checksums.
- IndiGo_Data_Dictionary.csv — variable definitions/units.
- source_register.csv and collection_tracker.csv — provenance and collection status.
- Canonical workbooks: [data/raw](../../data/raw/) and [data/processed](../../data/processed/).

## New 7-Nov receipts not uploaded
CP(5).xlsx (157,304 bytes), CP Master Data(4).xlsx (71,747), Final_Quarterly_Data(2).xlsx (99,836), EDA ANALYSIS(3).xlsx (13,233). Same size does not prove identical content. Final_Quarterly_Data(2).xlsx differs from D4's input. Binary export was not available in this session, so these are catalogued in [the inventory](../ARTIFACT_INVENTORY_2026-11-07.csv), not falsely marked as uploaded.

D4-v1 remains pinned to Final_Quarterly_Data(1).xlsx, SHA-256 85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c. Reconcile/checksum a new workbook before creating another experiment version.

## Licensing
docs/Data_Package_Manifest.md records permission for the earlier 30-Oct four-workbook package. That does not automatically establish permission for newer versions or rendered outputs. Confirm Bloomberg/institutional terms before publishing further derived data.


## 7 November 2026 — CP source sheet and Final Quarterly Data links

- The local `CP(6).xlsx` is byte-identical to GitHub's [CP(4).xlsx](../../data/raw/CP%284%29.xlsx), SHA-256 `208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e`. It contains `IS`, `usd inr`, `cpi`, `wpi`, `co new` and `co new monthly`. Use `IS` for quarterly Revenue, Net Income GAAP and EBITDA.
- The local `CP Master Data(5).xlsx` is byte-identical to GitHub's [CP Master Data(3).xlsx](../../data/raw/CP%20Master%20Data%283%29.xlsx), SHA-256 `30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474`.
- [Final_Quarterly_Data(1).xlsx — D4-v1 source link](../../data/processed/Final_Quarterly_Data%281%29.xlsx) remains the immutable D4-v1 input. SHA-256: `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c`.
- The new local candidate `Final_Quarterly_Data(3).xlsx` has SHA-256 `87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970`; its three sheets are `Final_Quarterly_Data`, `Calculation Audit` and `Data Quality Checks`. It is not uploaded or approved for modelling.
- See [Data Collection Register](../../data/DATA_COLLECTION_REGISTER.md) and [Phase 1 Data Collection Plan](../../docs/Phase1_Data_Collection_Plan.md) for the complete workbook/source map.
