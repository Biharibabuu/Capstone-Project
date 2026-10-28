# Notebooks workflow

## Current D3 notebook

- [`03_eda.ipynb`](03_eda.ipynb) — exploratory analysis of IndiGo profitability and available market indicators. Includes pre-specified hypotheses, original and cleaned-data quality checks, representativeness/bias checks, distributions, trends, Spearman/Kruskal–Wallis tests, an insight log and modelling recommendations.

## Local data setup

Place the authorized input workbooks at these paths in your local clone:

- `data/raw/CP.xlsx` — raw Bloomberg export with the multi-row-header `IS` sheet.
- `data/processed/CP Master Data.xlsx` — market indicators by monthly/daily frequency.

These files are intentionally excluded from the public repository. The public notebook has execution outputs cleared; run it locally to produce tables and figures. Do not publish workbook exports or rendered HTML that embeds Bloomberg-derived values unless the applicable licence permits redistribution.

## Important controls in the D3 notebook

- Reconstructs Revenue, `Net Income, GAAP` and EBITDA from the raw `IS` sheet, rather than using the two-quarter-shifted `Financial source` sheet in the master workbook.
- Excludes Bloomberg rows marked `Est` from actual historical outcomes.
- Aligns quarter ends to Indian fiscal quarters with `Q-MAR`.
- Labels oil data as a proxy unless the security/source is verified as Indian ATF.
- Treats same-quarter market means as descriptive EDA only, not automatically valid forecasting inputs.

## Suggested next notebooks

1. D2 data audit / master-data rebuild.
2. D3 EDA (current notebook).
3. Baseline and time-ordered evaluation.
4. Candidate model experiments.
5. Evaluation, uncertainty and model limitations.

Keep raw data unchanged locally. Record source URLs, field definitions, units, publication dates, revisions, feature sets and evaluation splits. Avoid random quarter shuffling and never fit preprocessing on future validation/test rows.
