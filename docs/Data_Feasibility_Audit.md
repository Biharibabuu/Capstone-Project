# D2 Data Feasibility Audit — IndiGo Profitability Intelligence

**Audit date:** 20 October 2026  
**Purpose:** establish source coverage and collection rules before the master dataset, EDA or model training.  
**Status:** desk review of official source pages completed; normalized raw extracts have not yet been collected and validated in this audit.

## 1. Decision summary

The project remains feasible as a quarterly PAT-margin forecasting study, but each input series must pass a coverage, definition, publication-date and rights check. Do not treat the existence of a source webpage as evidence that its entire historical series has already been downloaded.

| Dataset | Initial feasibility finding | Collection decision |
|---|---|---|
| IndiGo quarterly financials | Official IR page lists FY2015-16 through FY2026-27 and shows available results beginning with Q3 FY2015-16 | Collect quarter-end, revenue from operations, PAT, EBITDAR where consistently disclosed, financial-statement basis, units, result type and actual public release date |
| IndiGo operating statistics | Official IR pages provide monthly domestic/international statistics and historical financial-year selectors | Collect a consistent scope; prefer a verified consolidated series if available, otherwise combine only aligned domestic and international volumes and recompute load factor correctly |
| Indian ATF | IndianOil's visible prior-price table currently shows April 2024–March 2026 and the current April 2026 price | Treat as a short-history India-specific reference series; do not assume pre-April 2024 values exist on the inspected page |
| Longer-history fuel proxy | EIA publishes a monthly US Gulf Coast kerosene-type jet-fuel spot-price history extending back to 1990 | Candidate only; not Indian ATF. Compare its overlapping months with Indian ATF and disclose geography/unit limitations before deciding whether to use it |
| USD/INR | RBI provides a date-filtered Reference Rate Archive with Excel download; RBI says FBIL took over USD/INR reference-rate publication from 10 July 2018 | Collect RBI values through 9 July 2018 and FBIL values from 10 July 2018, documenting any source/method transition and publication timing |
| CPI | MoSPI eSankhyiki provides monthly CPI catalogue records and identifies current 2024-base releases | Prefer a documented All-India Combined General inflation series; record the series base year and release date; do not splice index levels from different base years without an official comparable back series |

## 2. Official sources

- **IndiGo Quarterly Financial Results:** https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html
- **IndiGo domestic operational statistics:** https://www.goindigo.in/information/investor-relations/operational-statistics/domestic.html
- **IndiGo international operational statistics:** https://www.goindigo.in/information/investor-relations/operational-statistics/international.html
- **IndianOil domestic ATF prices:** https://iocl.com/atf-domestic-airlines
- **EIA monthly jet-fuel spot-price proxy:** https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=m&n=pet&s=eer_epjk_pf4_rgc_dpg
- **RBI Reference Rate Archive:** https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx
- **FBIL:** https://www.fbil.org.in/#/home
- **MoSPI CPI catalogue:** https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI

## 3. Collection rules

### Financials
1. Use the same consolidated or standalone reporting basis for all quarters. Do not mix the two.
2. Capture the exact line items for Revenue from Operations and Profit After Tax, reported units and whether the result is unaudited, audited or revised.
3. Record the quarter end separately from the actual date the results became public.
4. Calculate PAT margin only after validating the units and confirming revenue is greater than zero: PAT margin (%) = PAT / Revenue from Operations × 100.
5. Record source report filename/URL for each observation. Keep EBITDAR optional if definition and coverage are consistent.

### Operations
1. Record monthly passenger count, passenger-kilometres (RPK), available seat-kilometres (ASK), publication/availability date, source URL and data scope.
2. If domestic and international observations are combined, sum passengers, RPK and ASK, then calculate load factor as total RPK / total ASK × 100. Do not take a simple mean of percentages.
3. If only a domestic series is available for a period, label it as a domestic proxy; do not imply it covers all IndiGo operations.
4. Define the aggregation method for the forecast quarter only after reviewing historical availability. Never use operating data published after the forecast cutoff.

### Fuel
1. First retain the India-specific ATF series as a documented reference. Use one city consistently if selected (Delhi is the starter candidate), and identify it as a proxy rather than IndiGo's actual purchase price.
2. IndianOil's website terms state that content may not be copied, modified, republished or uploaded without prior written permission. Therefore do not commit a bulk copied IndianOil price history into the public GitHub repository without permission; keep a source link and access notes.
3. The EIA series is a possible long-history fallback, not a drop-in equivalent. It reports US Gulf Coast spot jet-fuel price in USD/gallon. Keep it in its own schema and unit, compare overlapping dates with Indian ATF, and include it in modelling only if the data audit supports its use.
4. Do not blend Indian ATF and EIA proxy values into one unlabelled column.

### USD/INR
1. Use the RBI Reference Rate Archive for the RBI-published period; continue with FBIL from 10 July 2018.
2. A market observation date and a public release date are not automatically identical for point-in-time backtesting. Preserve whichever publication/availability metadata can be verified.
3. To produce quarter-level features, use a documented summary (for example, the latest eligible rate or a mean of observations actually available before cutoff). Do not use the target quarter's realised average when the forecast is supposed to be made before that quarter starts.

### CPI
1. Capture reference month, the exact All-India Combined General series, index base year, published year-on-year inflation, release date, URL and provisional/final status.
2. The current catalogue contains 2024-base releases. Do not concatenate 2012-base and 2024-base CPI index values as if they were one continuous index.
3. For each historic forecast, use only the latest CPI record released by the forecast cutoff; the latest reference month will normally lag the calendar date.

## 4. Point-in-time rule for the master dataset

Each modelling row represents the quarter whose PAT margin is to be predicted. The forecast cutoff is the last calendar day before that target quarter begins. A candidate predictor is eligible only when:
- its observation period is before the target quarter starts; and
- its publication/availability date is on or before the forecast cutoff.

The target quarter's PAT, revenue, PAT margin and target result release date are labels/provenance only and must never enter its predictors. Never fill an unavailable historical predictor using information released later.

## 5. Minimum checks before moving to EDA

- Count available and missing quarters for each source, and report the final complete-case sample size.
- Check unique date/quarter keys, duplicates, numeric fields, non-finite values and consistent units.
- Confirm financial reporting basis and definitions have not changed silently.
- Report gaps and excluded periods with reasons. Do not invent or impute target values.
- Fit any imputation/scaling only within training windows after chronological splits.
- Freeze the candidate predictor set only after coverage and publication timing have been reviewed.

## 6. Current limitation

This is a source-feasibility assessment, not a declaration that the historical files have been collected. The next step is to download/export the source records, enter the collection outcomes in `data/collection_tracker.csv`, normalize the source extracts into the templates under `data/templates/`, and then run the master-dataset builder and its tests.


## Data-workbook follow-up — 28 October 2026

This section records a later review of the actual supplied workbooks. It complements—but does not rewrite—the earlier source-page desk review above.

- Raw Bloomberg exports and the master workbooks have been received for local analysis; they are not committed to the public repository while redistribution permissions remain unconfirmed.
- The `Financial source` sheet in `CP Master Data.xlsx` is shifted by two quarters relative to the raw `IS` sheet. Rebuild the outcome series from the raw statement and recompute margins.
- Rows labelled `Est` in the raw financial export are estimates, not actual outcomes. Exclude these rows from training targets and historical evaluation.
- The earlier 33-row training count is provisional and not approved; recompute it after rebuilding the master.
- In the latest `CP(3).xlsx`, CPI observations run to 2026-09-30 and the earlier malformed-date concern was not reproduced. Verify derived dates against raw observations. The oil series is identified as `EUCRBRDT Index` (Dated Brent crude); it remains a proxy, not Indian ATF.
- The uploaded flat EDA output repeats early-quarter margins where the separate quarterly file marks results unavailable. Rebuild those rows from the raw financial statement.
- Use Indian fiscal-quarter alignment (Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar) consistently. The current D3 notebook encodes this convention.

The D3 implementation and outstanding findings are documented in [the D3 notebook](../notebooks/03_eda.ipynb) and [D3 status note](../reports/D3_eda/README.md).

**Decision:** data collection has advanced, but the final master remains **not model-ready** until the financial reconciliation, CPI date check, fiscal-quarter alignment and historical availability audit are complete. No model has yet been trained or validated on the reconciled data.


**Actual Bloomberg series IDs in the uploaded files:**
- Financials: `INDIGO IN` / BBG GAAP; `SALES_REV_TURN`, `NET_INCOME`, `EBITDA`.
- USD/INR: `USDINR REGN Curncy` (monthly).
- CPI inflation indicator: `INFUTOTY Index` (monthly, `PX_LAST`).
- WPI inflation indicator: `INBGWPIY Index` (monthly, `PX_LAST`).
- Dated Brent crude benchmark: `EUCRBRDT Index` (daily and monthly, `PX_LAST`).

Bloomberg source/access references: [Bloomberg Terminal](https://professional.bloomberg.com/products/bloomberg-terminal/), [Bloomberg DATA](https://data.bloomberg.com/), [InterGlobe Aviation Bloomberg profile](https://www.bloomberg.com/profile/company/INDIGO%3AIN). Exact terminal exports have no public unauthenticated series download URL. Official pages listed in the original source desk audit should be treated as independent cross-checks, not as the source of these uploaded values.
