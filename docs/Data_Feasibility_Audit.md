# D2 Data Feasibility Audit — Actual Bloomberg Dataset

**Project:** IndiGo Profitability Intelligence System  
**Review date:** 28 October 2026  
**Primary target:** Next-quarter PAT margin  
**Current dataset scope:** quarterly company financials, Dated Brent oil benchmark, WPI inflation, CPI inflation and USD/INR.

## 1. Actual collected source inventory

The working files reviewed are `CP(4).xlsx` (raw Bloomberg export), `CP Master Data(3).xlsx` (market series and legacy financial sheet), `Final_Quarterly_Data(1).xlsx` (derived quarterly panel and calculation audit) and `EDA ANALYSIS(2).xlsx` (flat EDA input). They remain in authorized local storage; Bloomberg-derived records are not committed to the public repository.

| Dataset | Bloomberg identifier / fields | Frequency and coverage in supplied export | Use and validation |
|---|---|---|---|
| Company financials | `INDIGO IN`, BBG GAAP; `SALES_REV_TURN`, `NET_INCOME`, `EBITDA` | Quarterly actuals 31 Mar 2017–30 Jun 2026; 30 Sep and 31 Dec 2026 marked `Est` | Revenue, Net Income (GAAP) and EBITDA. Recompute margins from raw `IS` values. Confirm Revenue definition against Revenue from Operations and Net Income against PAT using [IndiGo quarterly results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html). The current export contains EBITDA, not EBITDAR. |
| USD/INR | `USDINR REGN Curncy`; `PX_LAST`, `PX_BID` | Monthly, Jan 2015 onward | Monthly FX indicator. The 30 Oct 2026 observation is after the 28 Oct 2026 review date and must be excluded from an as-of-28-Oct analysis. [RBI reference-rate archive](https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx) is an independent comparison source, not the source of this export. |
| CPI inflation | `INFUTOTY Index`; `PX_LAST` | Monthly, Jan 2015–Sep 2026 | Confirm exact Terminal description, unit and release timing. [MoSPI CPI catalogue](https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI) is an independent definition/value cross-check, not the source of this export. |
| WPI inflation | `INBGWPIY Index`; `PX_LAST` | Monthly, Oct 2006–Sep 2026 | Confirm exact Terminal description and series/base linkage. [Office of the Economic Adviser WPI data](https://eaindustry.nic.in/download_data_2223.asp) is an independent cross-check, not the source of this export. |
| Oil benchmark | `EUCRBRDT Index`; `PX_LAST`; daily and monthly sheets | Daily 2 Jan 2015–19 Oct 2026; monthly Jan 2015–Sep 2026 | Identified as Dated Brent crude, not Indian ATF and not IndiGo's negotiated fuel cost. Keep it labelled as a Brent crude benchmark proxy; confirm exact price unit in Terminal. [Bloomberg Terminal](https://professional.bloomberg.com/products/bloomberg-terminal/) and [Bloomberg DATA](https://data.bloomberg.com/) are vendor access references, not public downloads. |

## 2. Source links and provenance

**Primary source for the uploaded data:** [Bloomberg Terminal](https://professional.bloomberg.com/products/bloomberg-terminal/) / [Bloomberg DATA](https://data.bloomberg.com/). The exact vendor security identifiers and field mnemonics are listed above and in [`data/source_register.csv`](../data/source_register.csv). [Bloomberg's InterGlobe Aviation company profile](https://www.bloomberg.com/profile/company/INDIGO%3AIN) identifies the listed company, but does not provide a public unauthenticated download of the licensed Terminal export.

Independent cross-check links:
- [IndiGo quarterly financial results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html)
- [RBI reference-rate archive](https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx)
- [MoSPI CPI catalogue](https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI)
- [Office of the Economic Adviser WPI data](https://eaindustry.nic.in/download_data_2223.asp)

These public links are validation references only; they were not the source of the uploaded Bloomberg values.

## 3. Data-quality and reconciliation findings

1. **Financial alignment:** the legacy `Financial source` sheet in `CP Master Data(3).xlsx` is shifted by two quarters relative to the raw Bloomberg `IS` sheet. Rebuild Revenue, Net Income and EBITDA from raw `IS` dates and values; do not use the legacy sheet as target labels.
2. **Actual versus estimates:** rows marked `Est` are estimates, not actual reported results. Exclude them from historical targets and model evaluation.
3. **Financial definition:** `NET_INCOME` is a provisional PAT component and `SALES_REV_TURN` a provisional Revenue component. Verify them against the exact company financial-statement line items before calculating PAT margin = PAT / Revenue from Operations × 100.
4. **EBITDA versus EBITDAR:** the supplied Bloomberg export contains EBITDA. Do not label it EBITDAR or substitute it for EBITDAR without a separate verified source.
5. **Oil benchmark:** `EUCRBRDT Index` is Dated Brent crude. It is not an India-specific aviation turbine fuel price and not IndiGo's realised purchase price.
6. **CPI dates:** the latest supplied raw CPI sheet has month-end observations through 30 Sep 2026. The earlier malformed-date concern was not reproduced in this raw sheet. Check derived quarterly dates against raw records and do not manually alter source dates.
7. **USD/INR cutoff:** the monthly export includes a 30 Oct 2026 record, which is later than the 28 Oct 2026 review date; exclude it from any dataset version with that as-of date.
8. **Quarter labels:** the existing derived workbook labels calendar quarters. Convert the time key to Indian fiscal quarters consistently: Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar.
9. **Small sample:** only the actual quarterly financial observations are potential target labels. Recompute complete-case and point-in-time eligible row counts after rebuilding the master; the earlier 33-row training count is not approved.

## 4. Point-in-time and modelling controls

For each target quarter, forecast cutoff is the last calendar day before the target quarter starts. Use only predictor observations whose periods precede the target quarter and whose values were available by the cutoff. Record publication/availability dates where verifiable. Quarter-end or reference-month dates do not automatically prove public availability.

Keep target-quarter revenue, PAT and PAT margin as labels only. Preserve missing values and source history. Use chronological holdout or rolling-origin validation, compare with a simple historical baseline, and fit imputation/scaling only inside each training window. Do not randomly shuffle quarterly observations.

## 5. Current decision and next step

The collected feature categories for this capstone are **company financials, Dated Brent oil benchmark, WPI inflation, CPI inflation and USD/INR**. The dataset is not yet model-ready because the financial alignment and financial-statement definitions must be reconciled, fiscal-quarter labels corrected, and publication availability audited.

Next: rebuild `Final_Quarterly_Data(1).xlsx` and the calculation audit from raw `IS` actual periods; validate financial line items; correct Indian fiscal-quarter labels; enforce the USD/INR date cutoff; and rerun the D3 EDA notebook. No ML model has been trained or validated on the reconciled data.


## Latest workbook package — 30 October 2026

The current review set consists of `CP(4).xlsx`, `CP Master Data(3).xlsx`, `Final_Quarterly_Data(1).xlsx` and `EDA ANALYSIS(2).xlsx`. Their sheet-level inventory and hashes are in [Data Package Manifest](Data_Package_Manifest.md), and unchanged local copies are in `IndiGo_Capstone_Project_Data_Pack.zip`.

The latest raw observations in this package extend to 2026-10-30 for monthly USD/INR, 2026-09-30 for CPI and WPI, 2026-10-19 for daily Dated Brent, and 2026-09-30 for monthly Dated Brent. Because the FX file does not carry intraday/publication timestamps, use the 2026-10-30 observation only when its availability by the model's forecast cutoff is established.
