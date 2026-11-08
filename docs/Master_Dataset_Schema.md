# Master Dataset Schema — Phase 1

The master dataset is target-quarter based: each row represents a quarter whose EBITDA Margin is being forecast, with a forecast cutoff on the final calendar day before that quarter begins.

> **Current source alignment note (8 November 2026):** this is the intended normalized output schema, not the raw Bloomberg workbook layout. The currently collected Bloomberg inputs are `INDIGO IN` quarterly financials; `USDINR REGN Curncy` monthly FX; `INFUTOTY Index` monthly CPI inflation; `INBGWPIY Index` monthly WPI inflation; and `EUCRBRDT Index` daily/monthly Dated Brent crude. The current data do not contain Indian ATF. The adopted modelling target is EBITDA Margin. Exact Bloomberg security definitions and publication dates must be retained.

## Target definition

`target_ebitda_margin_pct = target_ebitda_inr_mn / target_revenue_inr_mn × 100`

The target-quarter result is label information only. Never use `target_revenue_inr_mn`, `target_ebitda_inr_mn`, `target_ebitda_margin_pct` or `target_financial_published_on` as model predictors. PAT target fields, if retained, are supplementary/reference labels only.

## Output column groups

| Column | Meaning | Model use |
|---|---|---|
| forecast_as_of_date | Last calendar day before the target quarter begins | Time/availability key, not automatically a predictor |
| target_quarter | Fiscal-quarter label, e.g. FY2024-25_Q1 | ID only |
| target_quarter_start / target_quarter_end | Start and end of quarter to predict | ID only |
| target_revenue_inr_mn | Target quarter's Revenue from Operations | Label/supporting outcome only |
| target_ebitda_inr_mn | Target quarter's EBITDA | Label/supporting outcome only |
| target_ebitda_margin_pct | Target quarter's EBITDA Margin, percent | **Primary label only** |
| target_pat_inr_mn | Target quarter's PAT, if available and reconciled | Optional secondary/reference outcome |
| target_pat_margin_pct | Target quarter's PAT Margin, percent | Optional secondary/reference label only |
| target_financial_published_on | When target outcome became public | Label/provenance only |
| target_financial_source_url | Source URL for target outcome | Provenance only |

## Input CSV templates

The following header-only templates record the actual Bloomberg-export shape. They do not contain proprietary data:

- `financial_bloomberg_quarterly.csv`: raw quarter-end, Bloomberg header, Revenue, Net Income (GAAP), EBITDA, field IDs and result status. Reconcile EBITDA to its source definition and Revenue to Revenue from Operations before populating the primary EBITDA Margin target fields. Net Income/PAT may be retained separately as a reference financial measure.
- `usd_inr_monthly.csv`: monthly `USDINR REGN Curncy` values (`PX_LAST`, `PX_BID`).
- `cpi_inflation_monthly.csv`: monthly CPI inflation values and source metadata.
- `wpi_inflation_monthly.csv`: monthly WPI inflation values and source metadata.
- `brent_daily.csv` and `brent_monthly.csv`: Dated Brent benchmark values and source metadata.

### Normalized target fields

- Predictor fields: lagged/reported EBITDA Margin, lagged financial values, USD/INR, CPI, WPI, Dated Brent and justified seasonal/event variables, subject to point-in-time availability.
- Financial source fields: `revenue_inr_mn`, `ebitda_inr_mn`, `ebitda_margin_pct`; PAT fields may be retained separately as reference measures.
- Target-quarter fields: `target_revenue_inr_mn`, `target_ebitda_inr_mn`, `target_ebitda_margin_pct`; optional PAT fields remain reference labels.
- Metadata: fiscal quarter, forecast cutoff, publication dates, source URL, input vintage and data-quality flags.

## Point-in-time rule

For each target quarter, `forecast_as_of_date = target_quarter_start - 1 day`. Every predictor must satisfy both:

1. Observation period is strictly earlier than `target_quarter_start`.
2. Source publication/availability date is no later than `forecast_as_of_date`.

The target-quarter EBITDA and revenue outcome must have been published after `forecast_as_of_date`. Use them to calculate the EBITDA Margin label only; never treat them as known input information.

## Validation and reproducibility

Start with a baseline and limit the initial predictor count. Do not randomly shuffle quarterly rows. Perform chronological/rolling-origin evaluation. Any imputation or scaling must be fitted only inside each training fold. Do not interpolate targets or fill missing targets. Record feature missingness and source coverage before selecting the modelling subset.

## Adopted primary target and code status — 8 November 2026

The adopted primary target is `target_ebitda_margin_pct` = target-quarter EBITDA / target-quarter Revenue from Operations × 100. `target_pat_margin_pct` may be retained as a separate supporting/diagnostic outcome but is not the model target. EBITDAR must not be substituted for EBITDA.

The existing `src/build_master_dataset.py` currently creates PAT-margin labels and is not yet compliant with this adopted EBITDA target schema. It must be revised with tests before it is used to create the active model table. The existing `src/d4_train.py` is the legacy PAT-target D4-v1 implementation; use a separate, explicitly versioned EBITDA experiment and do not overwrite legacy evidence.
