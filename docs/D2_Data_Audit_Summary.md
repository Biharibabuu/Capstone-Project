# D2 Data Audit Summary — IndiGo Profitability Intelligence

**Version:** `data-v1.0`  
**Audit access/inspection date:** 23 October 2026  
**Linked outcomes:** CO2, CO6  
**Purpose:** Prepare a reproducible quarterly dataset for one-quarter-ahead IndiGo PAT-margin forecasting.

## Dataset snapshot

- **38 quarterly observations**, from **2017-03-31 to 2026-06-30**.
- **19 analytical fields** in the cleaned analytical master.
- **33 model-training rows** after required lag/target completeness checks.
- Primary outcome: PAT margin (%).
- Secondary outcome: EBITDA margin (%).
- Candidate external inputs: USD/INR, CPI inflation, WPI inflation and an oil benchmark proxy.

## Critical source-alignment finding

The `Financial source` sheet in the supplied `CP Master Data.xlsx` is misaligned by two quarters relative to the raw Bloomberg `IS` sheet. Values displayed against dates in the master correspond to raw financial values from two quarters earlier. For example, the master row dated 2017-09-30 carries the PAT-margin value matching raw IS quarter 2017-03-31.

**Treatment:** rebuild quarterly financial outcomes from the raw Bloomberg `IS` sheet and recompute PAT margin as Net Income / Revenue × 100 and EBITDA margin as EBITDA / Revenue × 100. Do not use the misaligned `Financial source` sheet for modelling.

The extreme COVID-period negative PAT margin is retained because it is reproducible from the supplied financial inputs and is not demonstrated to be a data-entry error.

## Data-quality decisions

| Check | Finding | Treatment |
|---|---|---|
| CPI date integrity | The 5.54 observation has a malformed final date in the master | Reconcile to 2026-09-30 using the raw Bloomberg export |
| Duplicates | No duplicate rows in supplied master sheets | No deduplication required |
| Missingness | Market source series are complete on PX_LAST; lags/targets have structural missing values | Do not impute structural NA values |
| Outliers | Extreme oil and profitability observations detected by the 1.5×IQR diagnostic | Retain economically plausible observations; flag and document rather than winsorise |
| Temporal integrity | Raw USD/INR export includes a 2026-10-30 record, later than the 2026-10-23 audit date | Exclude the future-dated record from v1.0 |
| Financial cut-off | Latest included historical financial quarter is 2026-06-30 | Exclude future/unverified estimates |

## Source, access and licence

The audit uses two user-supplied workbooks: `CP.xlsx` (raw Bloomberg export) and `CP Master Data.xlsx` (user-derived master). The files were accessed for this audit on 23 October 2026; the original terminal export timestamps are not embedded in the workbooks.

Bloomberg data are proprietary and subject to the applicable institutional subscription terms. Do not place raw licensed exports in a public repository unless redistribution is permitted. Keep raw exports in authorised private storage and confirm whether derived extracts may be publicly shared with the institution/library or faculty.

## DPDP Act, 2023 and purpose limitation

The reviewed workbooks contain corporate financial and market time series; no direct personal data was identified. Use is limited to forecasting IndiGo quarterly profitability and evaluating model performance. If personal data is added later, minimise it, restrict access, retain it only as necessary, and review the applicable lawful basis and purpose-limitation requirements under the DPDP Act, 2023 and institutional policy.

## Representativeness and bias

- This is a single-company dataset and does not represent the Indian airline industry.
- Passenger demand/load factor and explicit operational-disruption flags are not present in the supplied workbooks.
- The oil benchmark is a proxy, not a verified India-specific aviation turbine fuel (ATF) price series.
- Only 38 quarterly outcomes are available; use parsimonious models and chronological validation.
- Assess sensitivity to COVID-period observations during modelling without automatically deleting them.

## Feature engineering and leakage controls

| Feature | Logic | Control |
|---|---|---|
| `lag1_pat_margin_pct` | PAT margin shifted by one quarter | Uses prior-quarter value only |
| `lag4_pat_margin_pct` | PAT margin shifted by four quarters | Uses same fiscal quarter in the prior year |
| `usd_inr_avg`, `cpi_avg_pct`, `wpi_avg_pct`, `oil_benchmark_avg_usd` | Mean market value within the forecast-origin quarter | Use only observations available at the forecast cutoff |
| `usd_inr_qoq_pct`, `oil_qoq_pct`, `cpi_qoq_pct`, `wpi_qoq_pct` | Current-quarter average relative to previous quarter | Require as-of aggregation and release-date checks |
| `target_next_quarter_pat_margin_pct` | PAT margin shifted one quarter forward | Target only; never include in predictor matrix |

For historical evaluation, simulate the information available at each forecast origin. Do not leak later-published data into predictors.

## Expected repository artifacts

- `reports/ANCP_T##_D2_v1.pdf` — audit report (up to 8 pages) plus 3-page datasheet appendix.
- `data/cleaned/indigo_profitability_master_data-v1.0.csv`
- `data/cleaned/indigo_profitability_master_data-v1.0.xlsx`
- `data/metadata/data_dictionary_data-v1.0.csv`
- `data/metadata/source_log_data-v1.0.csv`
- `data/metadata/SHA256_data-v1.0.txt`
- `scripts/clean_indigo_data_v1_0.py`

The raw Bloomberg export should remain outside the public repository unless the licence expressly permits it. Re-run the cleaning script and verify the checksum for every versioned release.

**CO2 / CO6:** reproducible data acquisition and preparation, data-quality assessment, responsible data use, bias awareness and documented analytics.
