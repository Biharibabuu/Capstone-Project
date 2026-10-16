# Master Dataset Schema — Phase 1

The master dataset is target-quarter based: each row represents a quarter whose PAT margin is being forecast, with a forecast cutoff on the final calendar day before that quarter begins.

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
| latest_reported_ebitdar_inr_mn | EBITDAR from latest report if consistently available | Candidate predictor |
| latest_financial_source_url | Source URL of latest reported financial data | Provenance only |
| latest_operational_month | Latest operational month available by cutoff | Metadata |
| latest_operational_published_on | Publication date for selected operational record | Metadata / leakage audit |
| latest_passengers_carried | Passenger count from the selected comparable operational series | Candidate predictor |
| latest_passenger_load_factor_pct | Reported or correctly recomputed load factor | Candidate predictor |
| latest_operational_data_scope | Whether operational input is domestic-only or combined domestic/international | Metadata / scope audit |
| latest_operational_source_url | Source URL for selected operational record | Provenance only |
| latest_atf_month | Effective month of ATF price observation | Metadata |
| latest_atf_published_on | Publication date/availability of selected ATF input | Metadata / leakage audit |
| latest_atf_price_inr_per_kl | Chosen metro's domestic ATF price proxy | Candidate predictor |
| latest_atf_proxy_definition | Description of selected ATF series/city basis | Metadata / provenance |
| latest_atf_source_url | Source URL for ATF price | Provenance only |
| latest_fx_observation_date | Date of selected USD/INR observation | Metadata |
| latest_fx_published_on | Publication date/availability of USD/INR observation | Metadata / leakage audit |
| latest_usd_inr | INR per USD under the selected official series | Candidate predictor |
| latest_fx_source_url | Source URL for exchange rate | Provenance only |
| latest_cpi_month | Reference month for selected CPI value | Metadata |
| latest_cpi_published_on | CPI release date | Metadata / leakage audit |
| latest_cpi_index | Index level for consistent All-India Combined General CPI series | Candidate predictor |
| latest_cpi_inflation_yoy_pct | Published year-on-year CPI inflation, where available | Candidate predictor |
| latest_cpi_series_base_year | CPI base-year metadata to prevent accidental series mixing | Metadata / quality control |
| latest_cpi_source_url | Source URL for CPI | Provenance only |
| target_revenue_inr_mn | Target quarter's revenue from operations | Label/supporting outcome only |
| target_pat_inr_mn | Target quarter's PAT | Label/supporting outcome only |
| target_pat_margin_pct | Target quarter's PAT margin, percent | Label only |
| target_financial_published_on | When target outcome became public | Label/provenance only |
| target_financial_source_url | Source URL for target outcome | Provenance only |

## Input CSV templates

All normalized source files live under data/raw/ and follow templates under data/templates/.

### financial_quarterly.csv

Required: quarter_end, revenue_inr_mn, pat_inr_mn, financial_published_on, source_url.  
Optional: ebitdar_inr_mn.

Use quarter-end dates at 31 March, 30 June, 30 September or 31 December. Use actual publication dates, not quarter-end dates.

### operational_monthly.csv

Required: month_start, passengers_carried, operational_published_on, source_url. Include passenger_load_factor_pct OR both passenger_km_thousand and available_seat_km_thousand. When combining domestic and international series, combine volumes and calculate load factor from total passenger-kilometres divided by total available seat-kilometres.

### atf_monthly.csv

Required: month_start, atf_price_inr_per_kl, atf_published_on, source_url, proxy_definition. Use one consistent official price series, such as IndianOil domestic ATF price for Delhi.

### usd_inr_daily.csv

Required: observation_date, usd_inr, fx_published_on, source_url.

### cpi_monthly.csv

Required: month_start, cpi_index, cpi_published_on, source_url. Optional: cpi_inflation_yoy_pct. Keep the CPI series and base year consistent.

## Timing rules

For each target quarter, forecast_as_of_date = target_quarter_start - 1 day. Every predictor must satisfy both:
1. observation period is strictly earlier than target_quarter_start; and
2. the value's actual publication/availability date is on or before forecast_as_of_date.

The target-quarter financial result must have been published after forecast_as_of_date. Use it to calculate the target label only; never treat it as known input information.

## Small-sample policy

Start with a baseline and limit the initial predictor count. No random shuffle of quarterly rows. Perform chronological/rolling-origin evaluation. Any imputation or scaling must be fitted only inside each training fold. Do not interpolate targets or fill missing targets. Record feature missingness and source coverage before selecting the modelling subset.
