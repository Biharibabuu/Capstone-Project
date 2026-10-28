# Phase 1 — Data Collection Plan

**Project:** IndiGo Profitability Intelligence System  
**Primary target:** Next-quarter PAT margin (%)  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya  
**Status (28 October 2026):** Source workbooks have been collected locally and the D3 source notebook has been added to the repository. The workbooks are not committed publicly while Bloomberg redistribution permission remains unconfirmed. The current flat master is not model-ready: the legacy financial sheet is shifted by two quarters, estimates must be excluded from actual outcomes, fiscal-quarter labels need to follow the Indian fiscal calendar, and the current raw CPI series runs through 2026-09-30; the earlier malformed-date concern was not reproduced in the latest file. No model has been trained.

## Phase 1 objectives

1. Establish repeatable source collection and source-level provenance.
2. Create one row per forecast target quarter with an explicit forecast cutoff date.
3. Align reported financials, operational statistics, ATF, USD/INR and CPI data without future information.
4. Audit coverage, definitions, units, duplicates, missingness and publication timing.
5. Decide whether the available quarterly sample can support forecasting before advancing to EDA/model experiments.

## Step 1 — Create a source register

Maintain one row for every source file or series with these fields: source_id, variable_name, publisher, source_url, source_document_title, period_start, period_end, observation_frequency, units, definition, release_date_rule, retrieval_date, revision_policy, rights_or_access_notes, local_filename, and quality_notes.

Use the official sources below. Save the downloaded raw files unchanged whenever their terms permit. If a source cannot be redistributed, keep it locally and place its URL and retrieval details in the register instead of committing its raw data to GitHub.

## Step 2 — Collect the quarterly financial statements

**Source:** [IndiGo quarterly financial results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html).

For each available quarter, extract:
- quarter end;
- revenue from operations;
- PAT;
- EBITDAR, if consistently defined and reported;
- the actual date the result was published;
- source URL and source file/report name.

Use the same consolidated/standalone basis across every quarter. Prefer consolidated company performance if it is consistently reported, and document the choice. Confirm the financial statement line item definition for revenue and PAT; do not mix revenue from operations with another revenue definition. Store the original reported units, then convert to one standard unit (suggested: INR million) in a separate processed column. Record whether results are unaudited, audited, restated or revised.

**Important:** quarter_end is not the date a result became public. The field financial_published_on must be the actual release/publication date used for historical availability checks.

## Step 3 — Collect airline operating statistics

**Source:** [IndiGo domestic operational statistics](https://www.goindigo.in/information/investor-relations/operational-statistics/domestic.html) and [international operational statistics](https://www.goindigo.in/information/investor-relations/operational-statistics/international.html). The site labels the operational series as reported by DGCA.

Collect monthly passenger counts and load-factor support fields with:
- month_start;
- passengers_carried;
- passenger_km_thousand;
- available_seat_km_thousand;
- operational_published_on;
- source URL and data scope.

Keep the series' scope consistent with the target financial reporting scope. If domestic and international statistics are combined, sum passengers, passenger kilometres and available seat kilometres; recompute the overall load factor as total passenger kilometres / total available seat kilometres × 100. Do not take a simple arithmetic average of domestic and international load factors. If only a domestic series is available, label it clearly as a domestic operational proxy and document the mismatch with company-wide financials.

## Step 4 — Oil-price indicator actually collected

**Current source:** licensed Bloomberg Terminal export. The uploaded workbook identifies the series as `EUCRBRDT Index`, field `PX_LAST`, exported in both daily (`co new`) and monthly (`co new monthly`) sheets.

This is the **Dated Brent crude benchmark**, not Indian ATF and not IndiGo's negotiated fuel procurement cost. Use the terms “Dated Brent” or “oil benchmark proxy” in the dataset and report. The daily series has observations from 2 Jan 2015 through 19 Oct 2026; the monthly series runs from Jan 2015 through Sep 2026. The raw workbook records USD as currency, but confirm the unit from the Bloomberg Terminal field description before using a precise price-unit label.

**Bloomberg references:** [Bloomberg Terminal](https://professional.bloomberg.com/products/bloomberg-terminal/) and [Bloomberg DATA](https://data.bloomberg.com/). These are access/product references, not direct public downloads of licensed series. The [ECB financial-market data catalogue](https://data.ecb.europa.eu/data/datasets/FM) provides a separate reference to the Dated Brent series family.

The earlier IndianOil ATF plan is not the currently collected series. An India-specific ATF series can be considered later only if collected consistently and documented separately.

## Step 5 — USD/INR actually collected

**Current source:** Bloomberg Terminal export with security ID `USDINR REGN Curncy`, period `M`, and fields `PX_LAST` and `PX_BID`. The current quarterly workbook uses `PX_LAST` for the quarterly mean.

The export starts in Jan 2015 and contains a 30 Oct 2026 row, which is after the 28 Oct 2026 review date and must be excluded from an as-of-28-Oct analysis. It is a **monthly** series, not a daily series. Do not describe it as a daily RBI/FBIL series; those are possible cross-check sources only.

**References:** [Bloomberg Terminal](https://professional.bloomberg.com/products/bloomberg-terminal/), [Bloomberg DATA](https://data.bloomberg.com/), and [RBI's reference-rate archive](https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx) for independent comparison. For historical prediction evaluation, the observation date is not sufficient: verify publication/availability timing or apply a documented conservative lag.

## Step 6 — CPI and WPI inflation actually collected

The current raw Bloomberg workbook contains two monthly inflation indicators:

- **CPI:** `INFUTOTY Index`, field `PX_LAST`, observations Jan 2015–Sep 2026.
- **WPI:** `INBGWPIY Index`, field `PX_LAST`, observations Oct 2006–Sep 2026.

Confirm the exact security descriptions, geographic/series definitions and field units in Bloomberg Terminal before finalizing their names in the model. The current raw CPI series has month-end observations through 30 Sep 2026; the earlier malformed-date concern was not reproduced in the latest `CP(3).xlsx` file. Check generated/derived dates against the raw observations rather than editing a source date manually.

Use the official [MoSPI CPI catalogue](https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI) and [Office of the Economic Adviser WPI data](https://eaindustry.nic.in/download_data_2223.asp) for independent validation. They are not the source of the uploaded Bloomberg values. Record publication/release dates separately from reference months.

## Step 7 — Normalize the actual Bloomberg inputs

Raw Bloomberg workbook sheets should remain unchanged in authorized local storage. Map them to documented, normalized CSVs before model building:

- `financial_bloomberg_quarterly.csv` — raw-period financial fields and exact Bloomberg field IDs.
- `usd_inr_monthly.csv` — `USDINR REGN Curncy`, monthly.
- `cpi_inflation_monthly.csv` — `INFUTOTY Index`, monthly.
- `wpi_inflation_monthly.csv` — `INBGWPIY Index`, monthly.
- `brent_daily.csv` — `EUCRBRDT Index`, daily.
- `brent_monthly.csv` — `EUCRBRDT Index`, monthly.

These headers-only mapping templates are for traceable transformation of the current exports. The existing `src/build_master_dataset.py` expects the earlier standardized CSV contracts and does not yet import these Bloomberg workbook sheets directly; it must be updated/tested after the mapping and financial reconciliation are finalized. Do not treat the current derived quarterly workbook as a validated master.

No passenger counts, passenger load factor, RPK/ASK or event flags are present in the current workbook set. If operational indicators are added later, put them in a separate source file and include scope, definition, observation date and actual publication date.


## Step 8 — Fiscal-quarter alignment

Use Indian financial-year quarters:
- Q1: April–June;
- Q2: July–September;
- Q3: October–December;
- Q4: January–March.

Quarter ends should be 30 June, 30 September, 31 December or 31 March. Quarter labels in the processed dataset use the financial year in which Q1 starts, e.g. FY2024-25_Q1 ends 30 June 2024 and FY2024-25_Q4 ends 31 March 2025.

The master dataset is **target-quarter based**. For a target quarter, set forecast_as_of_date to the final calendar day before that quarter begins. The target is the target quarter's PAT divided by its revenue from operations × 100. Inputs are chosen only from records with an observation period before the target quarter and a publication/effective date no later than forecast_as_of_date.

For the financial predictors, select the most recent earlier quarter whose financial result was already published by the forecast cutoff. Do not automatically use the immediately preceding quarter if its result was still unpublished. For monthly/daily market and operating inputs, select the latest eligible value by observation period subject to publication timing. This can mean inputs have different last-observation dates; retain those dates in the dataset.

## Step 9 — Master dataset structure

The exact output columns are documented in Master_Dataset_Schema.md. Main groups:
- identifiers and target period: forecast_as_of_date, target_quarter, target_quarter_start/end;
- latest reported financial values and their quarter/publication metadata;
- latest available monthly operational values and publication metadata;
- latest available ATF price proxy and metadata;
- latest available USD/INR and metadata;
- latest available CPI and metadata;
- labels: target_revenue_inr_mn, target_pat_inr_mn, target_pat_margin_pct, target_financial_published_on;
- source URLs, where available.

## Step 10 — Cleaning and acceptance checks

Required checks:
1. All dates parse successfully; quarterly end dates are quarter ends.
2. One financial record per quarter_end; one operational/ATF/CPI record per month_start; one FX record per observation_date. Aggregate domestic/international operational records before building the master table.
3. Required target revenue is numeric and strictly positive; PAT may be negative.
4. Numeric values must be finite. Keep negative PAT when reported; investigate surprising values rather than deleting them automatically.
5. Units and reporting basis are consistent, with all conversions documented.
6. Every input publication/effective timestamp is at or before the forecast cutoff.
7. Every input observation period is strictly before target_quarter_start.
8. The target quarter's own financial result is used only as the label, never as a predictor.
9. Check missingness by column and quarter, source coverage, unusual changes and revisions.
10. Do not interpolate or forward-fill labels. If an input is missing, preserve/report it and handle imputation inside each training fold only.

## Step 11 — Small-sample modelling decision

Quarterly history is likely to be a small sample (actual usable rows to be measured, not assumed). Start with descriptive diagnostics and a simple baseline. Limit the initial feature set; five sources with multiple lags can quickly create more predictors than the data can support. Use chronological holdout or rolling-origin evaluation, no random train/test split. Do not use deep learning. Consider Ridge/Elastic Net and a nonlinear model only if the number of usable quarters supports them. Report the baseline even if the model performs worse.

## Phase 1 outputs

- normalized raw-source CSVs and source register;
- master dataset CSV with one row per forecast target quarter;
- data-quality report showing available rows, missing features and rejected rows;
- data dictionary and documented alignment/availability rules;
- feasibility decision for D2/D3, before model training.

## Privacy and usage

Only public, aggregate company/market data are planned. Do not collect passenger-level personal information, credentials or private internal records. Check source usage terms before publishing downloads. In the GitHub repository, commit templates, metadata and derived data only when redistribution is permitted.


## Source-feasibility findings (checked 20 October 2026)

The current official-source desk audit is documented in [Data Feasibility Audit](Data_Feasibility_Audit.md) and tracked in [data/collection_tracker.csv](../data/collection_tracker.csv). The results page lists historical financial reports beginning with Q3 FY2015-16; operational-statistics pages include historical fiscal-year selectors. The visible IndianOil domestic ATF history is much shorter than the financial history, so a long-history EIA jet-fuel proxy is being treated as a candidate only, not as equivalent to Indian ATF. RBI's reference-rate series transitions to FBIL from 10 July 2018. MoSPI CPI base-year changes must be handled explicitly. No model should be trained until the source records have been collected, date-aligned and audited.


## Follow-up from D3 review — 28 October 2026

The source workbook review found that the `Financial source` sheet in `CP Master Data.xlsx` is shifted by two quarters relative to the raw Bloomberg `IS` sheet. The raw `IS` sheet must be the basis for the target financial series; recompute PAT margin as Net Income / Revenue × 100 and EBITDA margin as EBITDA / Revenue × 100, excluding rows marked `Est` from actual outcomes.

The separate `EDA ANALYSIS` workbook should be regenerated: its first two quarters repeat margin values while the quarterly dataset indicates that these financial observations were unavailable. The project uses fiscal-quarter convention Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar; calendar-quarter labels must not be used for fiscal-seasonality claims.

The supplied oil series is labelled an oil benchmark and is not yet verified as Indian ATF or the airline's realised fuel cost. The latest raw CPI sheet has observations through 2026-09-30; compare the derived workbook's dates against raw observations instead of changing source dates manually. The raw series IDs are `USDINR REGN Curncy` (monthly), `INFUTOTY Index` (CPI), `INBGWPIY Index` (WPI), and `EUCRBRDT Index` (Dated Brent crude, daily/monthly). Keep missing values visible and exclude the 2026-10-30 USD/INR record from analyses dated 2026-10-28.

See [the D3 status note](../reports/D3_eda/README.md) and [D3 notebook](../notebooks/03_eda.ipynb). Do not freeze the feature set or begin model training until the reconciled master, source dates, definitions and availability cutoffs have passed review.
