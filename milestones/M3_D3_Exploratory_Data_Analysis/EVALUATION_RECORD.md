# M3 / D3 — EDA Evaluation Record

**Status:** Done  
**Analysis scope:** EBITDA-margin EDA only  
**Dataset:** 38 quarterly observations, 2017–2026 Q2

## 1. Objective

Describe the quarterly distribution and movement of IndiGo EBITDA margin, examine its association with available macro/market indicators, test pre-specified hypotheses, and pass defensible insights and caveats to M4. This is exploratory analysis, not a causal study or forecast evaluation.

## 2. Exact analysis input

The milestone data folder contains [EDA_ANALYSIS_EBITDA_ONLY_38Q.csv](data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv), an eight-column analysis panel:
- Year
- Calendar Quarter
- EBITDA Margin
- USD/INR quarterly mean
- CPI quarterly mean
- WPI quarterly mean
- Daily oil-benchmark quarterly mean
- Monthly oil-benchmark quarterly mean

The source workbook most recently supplied was EDA ANALYSIS(6).xlsx; SHA-256: 0c2a79065faaee48cec6393f79ff330a98a9eb20c1add3e87e8a45dd7e1c0f46. The original workbook remains the authoritative binary for data; the CSV is the explicit EBITDA-only analysis extract.

## 3. Hypotheses

| ID | Hypothesis | Method |
|---|---|---|
| H1 | USD/INR is associated with EBITDA margin | Spearman correlation |
| H2 | Monthly oil benchmark proxy is associated with EBITDA margin | Spearman correlation |
| H3 | CPI is associated with EBITDA margin | Spearman correlation |
| H4 | WPI is associated with EBITDA margin | Spearman correlation |
| H5 | EBITDA margin differs across calendar-quarter groups | Kruskal-Wallis / non-parametric group comparison |

Report paired n, effect size and p-value. Treat significance tests as exploratory; small samples, trends, multiple tests and omitted variables limit interpretation. Do not infer causality.

## 4. Quality and interpretation controls

- Use only EBITDA margin as the EDA outcome; do not include PAT in this analysis.
- Verify target denominator, source period and actual/estimate status before forecasting.
- Preserve the supplied quarter labels in this EDA record; M4 must convert to the agreed fiscal-quarter key where required.
- The Brent field is a crude benchmark proxy, not Indian ATF or IndiGo's realised fuel spend.
- Do not claim load factor, passenger yield, RPK/ASK or passenger counts: those fields are not in this dataset.
- EDA associations are not evidence of future model performance.

## 5. Files and evidence

- `data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv` — analysis panel.
- `ANCP_T##_D3_eda.ipynb` — current published source-only notebook (legacy source currently retained; see README/known limitation).
- `D3_Review_Notes.md` — review and handoff.
- `MILESTONE_CONTROL.md`, `DELIVERABLES_CHECKLIST.md`, `MILESTONE_MANIFEST.csv`.

The user's latest executed EDA notebook (34 cells; 14 executed code cells with saved tables and charts) was supplied in this session. It has not yet been committed as a repository notebook binary. Use the source-only copy until the notebook is corrected and committed with the exact EDA data input.

## 6. Handoff to M4

Use the EBITDA-only 38-quarter extract and verified M2 source definitions. Recheck target construction, chronology, fiscal-quarter labels, data availability cut-offs, missingness and baseline performance before selecting a model.
