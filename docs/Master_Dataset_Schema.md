# Master Dataset Schema — Phase 1

The master dataset is target-quarter based: each row represents a quarter whose PAT margin is being forecast, with a forecast cutoff on the final calendar day before that quarter begins.

> **Current source alignment note (28 October 2026):** this is the intended normalized output schema, not the raw Bloomberg workbook layout. The currently collected Bloomberg inputs are `INDIGO IN` quarterly financials; `USDINR REGN Curncy` monthly FX; `INFUTOTY Index` monthly CPI inflation; `INBGWPIY Index` monthly WPI inflation; and `EUCRBRDT Index` daily/monthly Dated Brent crude. The current data do **not** contain Indian ATF or airline passenger/load-factor fields. Do not treat the old ATF/daily-FX templates as the source of the current data; map the new header-only templates to this normalized schema and update/test the builder before use. Exact Bloomberg security definitions and publication dates must be retained.

## Target definition

target_pat_margin_pct = target_pat_inr_mn / target_revenue_inr_mn × 100

The target-quarter result is label information only. Never use target_revenue_inr_mn, target_pat_inr_mn, target_pat_margin_pct or target_financial_published_on as model predictors.

## Output column groups

| Column | Meaning | Model use |
|---|---|---|
| forecast_as_of_date | Last calendar day before the target quarter begins | Time/availability key, not automatically a predictor |
| target_quarter | Fiscal-quarter label, e.g. FY2024-25_Q1 | ID only |
| target_quarter_start / target_quarter_end | Start and end of quarter to predict | ID only |
| latest_reported_fiscal_quarter | Most recent earlier financial quarter published by cutoff | Metadata |
| latest_reported_financial_quarter_end | Quarter-end date for latest available company financials | Metadata |
| latest_reported_financial_published_on | Publication date for selected financial record | Metadata / leakage audit |
| latest_reported_revenue_inr_mn | Revenue from operations from latest report available by cutoff | Candidate predictor |
| latest_reported_pat_inr_mn | PAT from latest report available by cutoff | Candidate predictor |
| latest_reported_pat_margin_pct | PAT / revenue for latest report available by cutoff | Candidate predictor |
| latest_reported_ebitda_inr_mn | EBITDA from the raw Bloomberg `IS` sheet, if reconciled and comparable | Candidate predictor |
| latest_financial_source_url | Source URL of latest reported financial data | Provenance only |
| latest_operational_month | Latest operational month available by cutoff | Metadata |
| latest_operational_published_on | Publication date for selected operational record | Metadata / leakage audit |
| latest_passengers_carried | Passenger count from the selected comparable operational series | Candidate predictor |
| latest_passenger_load_factor_pct | Reported or correctly recomputed load factor | Candidate predictor |
| latest_operational_data_scope | Whether operational input is domestic-only or combined domestic/international | Metadata / scope audit |
| latest_operational_source_url | Source URL for selected operational record | Provenance only |
| latest_brent_observation_period | Daily observation date or monthly period for the Dated Brent proxy | Metadata |
| latest_brent_published_on | Publication/availability date of selected Bloomberg observation, when verified | Metadata / leakage audit |
| latest_dated_brent_px_last | PX_LAST value from EUCRBRDT Index; unit must be confirmed in Terminal | Candidate predictor / market proxy |
| latest_brent_source_security_id | Bloomberg security identifier (EUCRBRDT Index) | Metadata / provenance |
| latest_brent_source_field_id | Bloomberg field mnemonic (PX_LAST) | Metadata / provenance |
| latest_brent_unit | Unit confirmed from Bloomberg field description | Metadata / quality control |
| latest_brent_source_reference | Bloomberg Terminal/Data product reference, not a direct public series URL | Provenance only |
| latest_fx_observation_date | Date of selected USD/INR observation | Metadata |
| latest_fx_published_on | Publication date/availability of USD/INR observation | Metadata / leakage audit |
| latest_usd_inr | INR per USD under the selected official series | Candidate predictor |
| latest_fx_source_url | Source URL for exchange rate | Provenance only |
| latest_cpi_month | Reference month for selected CPI value | Metadata |
| latest_cpi_published_on | CPI release date | Metadata / leakage audit |
| latest_cpi_inflation_pct | CPI inflation indicator from INFUTOTY Index (exact series definition to be confirmed in Terminal) | Candidate predictor |
| latest_cpi_source_security_id | Bloomberg security identifier (INFUTOTY Index) | Metadata / provenance |
| latest_cpi_source_field_id | Bloomberg field mnemonic (PX_LAST) | Metadata / provenance |
| latest_wpi_month | Reference month for WPI observation | Metadata |
| latest_wpi_published_on | Actual public release/availability date, when verified | Metadata / leakage audit |
| latest_wpi_inflation_pct | WPI inflation indicator from INBGWPIY Index (verify series/base linkage) | Candidate predictor |
| latest_wpi_source_security_id | Bloomberg security identifier (INBGWPIY Index) | Metadata / provenance |
| latest_wpi_source_field_id | Bloomberg field mnemonic (PX_LAST) | Metadata / provenance |
| latest_cpi_series_base_year | CPI base-year metadata to prevent accidental series mixing | Metadata / quality control |
| latest_cpi_source_url | Source URL for CPI | Provenance only |
| target_revenue_inr_mn | Target quarter's revenue from operations | Label/supporting outcome only |
| target_pat_inr_mn | Target quarter's PAT | Label/supporting outcome only |
| target_pat_margin_pct | Target quarter's PAT margin, percent | Label only |
| target_financial_published_on | When target outcome became public | Label/provenance only |
| target_financial_source_url | Source URL for target outcome | Provenance only |

## Input CSV templates

The following header-only templates record the actual Bloomberg-export shape. They do not contain proprietary data:

- `financial_bloomberg_quarterly.csv`: raw quarter-end, Bloomberg header, Revenue, Net Income (GAAP), EBITDA, field IDs and result status. Reconcile Net Income to reported PAT and Revenue to Revenue from Operations before populating the normalized target fields.
- `usd_inr_monthly.csv`: monthly `USDINR REGN Curncy` values (`PX_LAST`, `PX_BID`).
- `cpi_inflation_monthly.csv`: monthly `INFUTOTY Index` `PX_LAST` values; exact series definition must be confirmed in Terminal.
- `wpi_inflation_monthly.csv`: monthly `INBGWPIY Index` `PX_LAST` values; series/base linkage must be verified.
- `brent_daily.csv` and `brent_monthly.csv`: daily/monthly `EUCRBRDT Index` `PX_LAST` values. This is Dated Brent crude, not Indian ATF.
- `operational_monthly.csv`: optional future input; passenger/load-factor/RPK/ASK data have not been collected yet.

Older templates `atf_monthly.csv`, `usd_inr_daily.csv` and `cpi_monthly.csv` reflect the earlier proposed source plan. They are not the current raw Bloomberg series. The existing master-data builder still expects its earlier standardized input contracts and must be mapped/tested against the current source templates before execution. Keep the raw Bloomberg Excel workbook unchanged in local authorized storage.

### Normalized target fields

After source reconciliation, the model-ready dataset should use:
- `quarter_end`, `fiscal_quarter`, `forecast_as_of_date`;
- `revenue_inr_mn`, `pat_inr_mn` (only after Net Income/PAT mapping is verified), `ebitda_inr_mn`, `pat_margin_pct`, `ebitda_margin_pct`;
- monthly-derived quarter summaries for USD/INR, CPI inflation, WPI inflation and Dated Brent (daily and/or monthly, if justified);
- financial and market availability dates, exact source IDs/fields and quality flags;
- target-quarter outcomes as labels only.

## Timing rules

For each target quarter, forecast_as_of_date = target_quarter_start - 1 day. Every predictor must satisfy both:
1. observation period is strictly earlier than target_quarter_start; and
2. the value's actual publication/availability date is on or before forecast_as_of_date.

The target-quarter financial result must have been published after forecast_as_of_date. Use it to calculate the target label only; never treat it as known input information.

## Small-sample policy

Start with a baseline and limit the initial predictor count. No random shuffle of quarterly rows. Perform chronological/rolling-origin evaluation. Any imputation or scaling must be fitted only inside each training fold. Do not interpolate targets or fill missing targets. Record feature missingness and source coverage before selecting the modelling subset.
