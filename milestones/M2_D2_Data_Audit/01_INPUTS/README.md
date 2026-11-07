# M2 — Inputs and Source Links

## Raw CP source workbook
- [CP(4).xlsx — canonical raw Bloomberg workbook](../../../data/raw/CP%284%29.xlsx)
- The latest local upload `CP(6).xlsx` is byte-identical to the repository file.
- SHA-256: `208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e`.
- Financial statement source tab: `IS` (Revenue, Net Income GAAP and EBITDA).
- Other tabs: `usd inr`, `cpi`, `wpi`, `co new`, `co new monthly`.

## Master indicator workbook
- [CP Master Data(3).xlsx — canonical master workbook](../../../data/raw/CP%20Master%20Data%283%29.xlsx)
- The latest local upload `CP Master Data(5).xlsx` is byte-identical to this repository file.
- SHA-256: `30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474`.

## Final quarterly derived data
- [Final_Quarterly_Data(1).xlsx — D4-v1 pinned dataset](../../../data/processed/Final_Quarterly_Data%281%29.xlsx)
- D4-v1 SHA-256: `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c`.
- New local candidate `Final_Quarterly_Data(3).xlsx` SHA-256: `87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970`. It contains `Final_Quarterly_Data` (38 records; 12 columns), `Calculation Audit` (196 data rows; 13 columns) and `Data Quality Checks` (20 data rows; 6 columns).
- Candidate (3) is not uploaded and is not an approved replacement. Reconcile it with raw CP `IS` and indicator tabs before new modelling.

See [Phase 1 Data Collection Plan](../../../docs/Phase1_Data_Collection_Plan.md), [collection tracker](../../../data/collection_tracker.csv), [source register](../../../data/source_register.csv), and [Data Collection Register](../../../data/DATA_COLLECTION_REGISTER.md).
