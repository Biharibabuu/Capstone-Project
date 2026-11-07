# M3 / D3 — Review Notes and M4 Handoff

**Status:** Done  
**Target:** EBITDA margin only

## Data panel

The M3 milestone contains [EDA_ANALYSIS_EBITDA_ONLY_38Q.csv](data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv), an eight-field quarterly extract with 38 observations (2017–2026 Q2). It excludes PAT and carries the USD/INR, CPI, WPI and daily/monthly Dated Brent benchmark proxies supplied in the EDA workbook.

## Main controls

1. Validate EBITDA and Revenue from Operations definitions and the calculation denominator against the underlying company statements.
2. Exclude estimated or unavailable financial rows from realised targets.
3. Use a unique chronological quarter key; convert calendar quarter to Indian fiscal-quarter labels for modelling only after agreeing the convention.
4. Preserve source observation dates and known publication/availability dates.
5. Dated Brent is an oil benchmark proxy, not aviation turbine fuel or IndiGo's actual fuel price.
6. The analysis is observational and exploratory; correlation does not prove causality.
7. No passenger count, load factor, yield, RPK/ASK, capacity or route-mix dataset is present in the supplied panel.

## Hypothesis framework

- H1: USD/INR and EBITDA margin association.
- H2: monthly oil benchmark proxy and EBITDA margin association.
- H3: CPI and EBITDA margin association.
- H4: WPI and EBITDA margin association.
- H5: EBITDA margin differences across calendar-quarter groups.

Use paired sample sizes and Spearman effect sizes/p-values where appropriate. Avoid interpreting small-sample p-values as proof of business causation.

## Notebook publication note

The older notebook source currently in the repository still contains legacy PAT language and must not be presented as the approved EBITDA-only notebook. The latest uploaded notebook has 34 cells and saved outputs in its uploaded copy, but the raw notebook binary has not yet been published to the repository. Until it is corrected and committed, use the M3 EBITDA-only CSV and this review note as the scope-controlled data handoff.

## Handoff to M4

M4 owns the modelling data snapshot, features, chronological splits, training code, experiment log, model comparison, predictions and model-selection report. Do not use the old PAT experiment as evidence of an EBITDA-margin model.
