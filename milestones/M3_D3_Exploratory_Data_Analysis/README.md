# M3 / D3 — Exploratory Data Analysis

**Status:** DONE — EBITDA-only EDA handoff completed.

## Brief
M3 explores the distribution, time pattern and macro/market associations of IndiGo's quarterly EBITDA margin. It is an explanatory/diagnostic milestone; it does not train or validate the forecasting model.

## Dataset used
[EDA_ANALYSIS_EBITDA_ONLY_38Q.csv](data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv) — 38 quarterly observations from 2017 to 2026 Q2, with EBITDA Margin and five macro/market indicator series. PAT is not included as an outcome.

## Canonical notebook
[Executed EBITDA-only EDA notebook](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb). It retains 34 cells, 14 executed code cells and 43 outputs. Its file input was corrected to point to the committed M3 CSV. Previously captured outputs remain embedded; a clean re-run is a recommended independent verification step.

## Workflow
1. Load the versioned M3 CSV panel.
2. Check rows, columns, duplicates, missingness and quarter coverage.
3. Standardise column names/types and create chronological quarter-end dates.
4. Describe EBITDA margin and indicator distributions.
5. Examine time trends, correlations and calendar-quarter differences.
6. Test five pre-specified hypotheses; report n/effect/p-value cautiously.
7. Record insights, limitations and modelling recommendations.
8. Hand the approved EDA input and caveats to M4.

## Folder map
- 01_INPUTS/ — input register and data-use notes.
- 02_WORKING/ — canonical executed notebook.
- 03_DELIVERABLES/ — evaluator-facing output index.
- 04_EVIDENCE/ — outputs and clean-run verification evidence.
- 05_REFERENCES/ — data and method references.
- data/ — exact 38-quarter EBITDA-only input panel.

## Limitations
Only 38 observations; time-series dependence; no passenger operating metrics; oil series identity and units are not specified in this workbook and must be treated as proxies. Associations are not causation or forecast-performance evidence.

## Handoff
M4 is the active milestone. Use this EBITDA-only input and confirm target construction, date alignment, fiscal-quarter labels, feature availability and chronological validation before modelling.
