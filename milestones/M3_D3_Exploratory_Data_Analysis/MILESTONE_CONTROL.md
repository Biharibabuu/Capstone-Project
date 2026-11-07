# M3 / D3 — Milestone Control

**Administrative status:** Done (EDA handoff accepted for the current project scope).  
**Target:** EBITDA Margin only.  
**Canonical notebook:** 02_WORKING/ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb  
**Canonical input:** data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv

## Purpose
Assess the 38-quarter dataset, describe EBITDA Margin and macro-market indicators, explore time trends and quarter patterns, test five predefined hypotheses and document implications for M4.

## Inputs
- M3 EBITDA-only 38-quarter CSV panel (eight columns).
- M2 source definitions and workbooks (source lineage only).
- The historical executed notebook upload, retained with 43 outputs.

## Work completed
- Committed the EBITDA-only panel in M3/data.
- Updated the executed notebook's business framing and CSV input path.
- Preserved 34 cells, 14 code cells and 43 prior output records.
- Recorded scope, hypotheses, limitations and M4 handoff.

## Known reproducibility caveat
The notebook's original output cells were retained from the uploaded executed file; they were not regenerated after correcting the input path. A fresh execution from a clean clone is still recommended to independently confirm the visible results.

## Acceptance and next gate
M3's current accepted handoff is the 38-quarter EBITDA-only panel and analysis. M4 must verify the target denominator, period definitions, data availability, missingness and chronological modelling protocol before training.

## Risks
Only 38 observations are available. Time dependence, omitted operational drivers and ambiguous oil benchmark units limit interpretation. Dated Brent must not be called IndiGo's realised ATF cost. No passenger load factor, passenger yield, capacity, fuel consumption or route mix is present.
