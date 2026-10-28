# D3 — Exploratory Data Analysis: Review and Status

**Project:** IndiGo Profitability Intelligence System  
**Status:** Reproducible analysis notebook prepared; results should be regenerated after source reconciliation.

## Included in the public repository

- [`notebooks/03_eda.ipynb`](../../notebooks/03_eda.ipynb) — source-only notebook with pre-specified hypotheses, data-quality checks, distributions, fiscal-quarter segmentation, statistical tests, an insight log and modelling recommendations. Execution outputs are cleared so Bloomberg-derived values and figures are not republished in this public repository.
- This note records the source-alignment issues found during review.

## Local input files required

Place the authorized local workbooks at:

- `data/raw/CP.xlsx` — raw Bloomberg workbook containing the `IS` sheet.
- `data/processed/CP Master Data.xlsx` — market-indicator workbook containing `USD INR`, `CPI inflation`, `WPI inflation`, `Oil benchmark(MONTHLY)`, `Oil benchmark(DAILY)` and the legacy `Financial source` sheet.

These data paths are ignored by Git. Do not publish Bloomberg exports, embedded report outputs or derived values unless the applicable Bloomberg and institutional licence permits redistribution.

## Important findings from the file review

1. **The legacy financial sheet is shifted.** The margins in the master workbook's `Financial source` sheet match raw Bloomberg `IS` margin calculations two quarters earlier, rather than on the same quarter-end date. The notebook rebuilds Revenue, PAT and EBITDA margins from the raw `IS` sheet and displays a reconciliation check. It does not use the shifted sheet as the target source.
2. **Estimated quarters are not actual outcomes.** Rows whose Bloomberg quarter header is marked `Est` are excluded from the historical outcome panel. Estimates must not be used as realised PAT-margin labels for model training or evaluation.
3. **The supplied flat EDA analysis workbook needs rebuilding.** Its first two quarter rows repeat the same PAT and EBITDA margins even though the separate quarterly dataset marks financial observations for those periods as unavailable. These are not supported as two independent observed outcomes by that dataset; use the raw `IS` source and the reconciliation check instead.
4. **Use fiscal-quarter labels consistently.** The project schema uses Indian fiscal quarters: Q1 = Apr–Jun, Q2 = Jul–Sep, Q3 = Oct–Dec, Q4 = Jan–Mar. The notebook uses `Q-MAR` alignment; prior flat outputs labelled calendar quarters and should not be used for fiscal-seasonality conclusions.
5. **The oil series remains a proxy.** The sheet name is `Oil benchmark`; the provided files do not establish that this is Indian ATF or IndiGo's realised fuel cost. Describe it as an oil benchmark proxy unless the source/security identifier is verified.
6. **CPI date and coverage need source verification.** The supplied monthly CPI sheet contains a date irregularity around August 2026 and not every fiscal quarter has all market inputs. The notebook reports missingness rather than inventing or silently imputing observations.
7. **The EDA is not model evaluation.** Same-quarter relationships are exploratory. For actual forecasting, every feature must be available by the forecast cutoff, and candidate models must be compared with a baseline using chronological validation.

## Hypotheses documented before results

- H1: oil benchmark and PAT margin are associated.
- H2: USD/INR and PAT margin are associated.
- H3: CPI inflation and PAT margin are associated.
- H4: WPI inflation and PAT margin are associated.
- H5: PAT margin differs across Indian fiscal quarters.
- H6: PAT and EBITDA margins move together.

The notebook computes paired sample sizes and effect sizes alongside p-values, repeats coverage/missingness checks on the cleaned panel, creates plots and distributions, and produces an insight log with decision implications and confidence notes. No causal claim or model-performance claim is made by the EDA.

## Next steps

1. Rebuild `Final_Quarterly_Data.xlsx` and its calculation audit from the raw `IS` source using actual quarters only and fiscal-quarter labels.
2. Verify financial definitions and published-result dates against official filings.
3. Re-run `notebooks/03_eda.ipynb` locally and review the generated evidence.
4. Carry only defensible predictors into the D4 baseline and candidate-model experiments.
