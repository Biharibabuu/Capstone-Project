# Data Collection Register — IndiGo Profitability Intelligence

**Last updated:** 7 November 2026

## CP(6).xlsx — raw Bloomberg workbook

Latest local SHA-256: `208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e`. This is byte-identical to [CP(4).xlsx already stored in GitHub](https://github.com/Biharibabuu/Capstone-Project/blob/main/data/raw/CP%284%29.xlsx).

| Sheet | Dataset | Frequency | Fields / purpose |
|---|---|---|---|
| `IS` | IndiGo financial statements | Quarterly | Revenue (`SALES_REV_TURN`), Net Income GAAP (`NET_INCOME`), EBITDA (`EBITDA`) |
| `usd inr` | USD/INR | Monthly | `USDINR REGN Curncy` |
| `cpi` | CPI inflation indicator | Monthly | `INFUTOTY Index` |
| `wpi` | WPI inflation indicator | Monthly | `INBGWPIY Index` |
| `co new` | Dated Brent crude | Daily | `EUCRBRDT Index` |
| `co new monthly` | Dated Brent crude | Monthly | `EUCRBRDT Index` |

The `IS` tab is the financial source sheet in CP. The bottom source label identifies Bloomberg; it is not a separate worksheet. Exclude rows marked `Est` from realised outcomes.

## CP Master Data(5).xlsx

SHA-256: `30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474`, identical to [CP Master Data(3).xlsx in GitHub](https://github.com/Biharibabuu/Capstone-Project/blob/main/data/raw/CP%20Master%20Data%283%29.xlsx). Rebuild quarterly financial margins from raw CP `IS`; the legacy `Financial source` tab was found to be two quarters shifted.

## Final quarterly derived data — repository source link

**Pinned D4-v1 file:** [Final_Quarterly_Data(1).xlsx](https://github.com/Biharibabuu/Capstone-Project/blob/main/data/processed/Final_Quarterly_Data%281%29.xlsx).

SHA-256: `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c`. This is the immutable D4-v1 benchmark input.

**New local candidate:** `Final_Quarterly_Data(3).xlsx`; SHA-256 `87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970`. It has `Final_Quarterly_Data` (38 data records; 12 columns), `Calculation Audit` (196 data rows; 13 columns) and `Data Quality Checks` (20 data rows; 6 columns). It differs from D4-v1 and has not been uploaded to GitHub. Do not use the D4-v1 link as a link to candidate (3).

## Public validation sources
- [IndiGo quarterly financial results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html)
- [Bloomberg Terminal](https://professional.bloomberg.com/products/bloomberg-terminal/)
- [RBI Reference Rate Archive](https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx)
- [MoSPI CPI Catalogue](https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI)
- [Office of the Economic Adviser WPI Data](https://eaindustry.nic.in/download_data_2223.asp)

## Governance
Preserve raw workbooks; version every derived dataset; record hashes and transformations; separate observation dates from publication/availability dates; never overwrite D4-v1; confirm Bloomberg/institutional redistribution rights before publication.
