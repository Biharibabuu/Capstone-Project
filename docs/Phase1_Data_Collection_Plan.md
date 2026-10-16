# Phase 1 — Data Collection Plan

**Project:** IndiGo Profitability Intelligence System  
**Primary target:** Next-quarter PAT margin (%)  
**Team:** Nikhil Raj, Krishan Sharma, K. Shreya  
**Status:** Collection plan and templates; data have not yet been populated or modelled.

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

## Step 4 — Collect ATF price proxy

**Source:** [IndianOil historical domestic ATF prices](https://www.iocl.com/atf-domestic-airlines). It reports previous ATF prices in rupees per kilolitre by metro.

For the starter dataset, choose one consistently available series (for example, Delhi domestic ATF price in INR/kL) and use it throughout. Record the chosen metro in the source register. This is a public market price proxy—not IndiGo's actual negotiated or blended fuel procurement cost. If a future analysis uses a metro average, calculate it consistently from the same cities in every month and document the exact formula.

Fields: month_start/effective date, atf_price_inr_per_kl, atf_published_on, source_url and proxy_definition.

## Step 5 — Collect USD/INR

**Sources:** [RBI reference-rate archive](https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx), [RBI statistics](https://www.rbi.org.in/scripts/statistics.aspx/BS_ViewMMO.aspx), and [FBIL](https://www.fbil.org.in/).

RBI documents that FBIL took over publication of the USD/INR and other reference rates effective 10 July 2018. Record the provider and any source/methodology transition. Collect a daily or otherwise consistent official series, then use the latest rate available by the forecast cutoff (or a quarterly average built strictly from observations published by that cutoff, if that measure is chosen in advance).

Fields: observation_date, usd_inr, fx_published_on and source_url.

## Step 6 — Collect CPI / inflation

**Source:** [MoSPI CPI data catalogue](https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI).

Choose the All-India Combined General CPI series and document the base year. You may use the CPI index, the published year-on-year inflation rate, or both if data coverage is consistent. CPI is published monthly and release timing matters; a CPI value for a month must not be used before its publication date. Do not join historical CPI only by month label and assume it was known at month-end.

Fields: month_start, cpi_index, cpi_inflation_yoy_pct, cpi_published_on and source_url.

## Step 7 — Normalize input files

Put normalized, manually transcribed or downloaded-and-cleaned source extracts in data/raw/ using the exact column names in data/templates/:

- financial_quarterly.csv
- operational_monthly.csv
- atf_monthly.csv
- usd_inr_daily.csv
- cpi_monthly.csv

Keep raw files unmodified where practical. Preserve a separately processed copy and a source register. Do not invent publication dates. When a historical publication date cannot be verified, document that limitation and use a conservative lag / availability rule instead of pretending the data were known earlier.

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
