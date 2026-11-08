# M1 / D1 — Project Charter: Evaluation Record

**Status:** Revised D1 content received and reviewed; GitHub binary upload pending.  
**Team:** Nikhil Raj, Krishan Sharma and K. Shreya

## Project definition
**Project:** IndiGo Profitability Intelligence System.

**Business problem:** quarterly profitability may be affected by fuel-price movements, USD/INR, inflation and operating/demand conditions. The capstone tests whether historical financial performance and selected market indicators can support a one-quarter-ahead profitability forecast and scenario planning.

**Adopted project target:** **EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.** This is profitability forecasting, not a share-price forecast.

**Decision use:** provide a transparent estimate with input context, limitations and low/base/high sensitivity scenarios.

## Current D1 source document — revised DOCX
- Filename: `IndiGo_Macroeconomic_Profitability_Capstone_M1.docx`
- Format: DOCX, 9 pages
- Received: 8 November 2026
- Original file SHA-256: `d96c5cddecd2cb33e5eaceca61c7387b43468481c1d22d0a68f8a295c0a52e9f`
- Page 3 explicitly lists EBITDA margin as the primary analytical output, using a consistent published definition (including ex-forex where comparable).
- Page 7's initial data plan lists EBITDA margin as the target for company profitability.
- Page 5 frames the analytics question around forecasting next-quarter operating profitability against a simple historical baseline.
- Page 8 describes baseline/model comparison, chronological validation, out-of-sample MAE/RMSE and low/base/high-cost scenario analysis.

## Scope and boundaries
- Historical financials and selected external indicators; audit, source lineage, quarter alignment, cleaning, EDA, baseline and challenger testing.
- Chronological evaluation, explainability where supported, scenario analysis and a local HTML/API prototype.
- Target-quarter EBITDA and Revenue from Operations are labels used to calculate EBITDA Margin, never predictors.
- Correlation is not causation; this is not guaranteed forecasting or investment advice.

## Team and course sequence
The charter's role split and responsibility matrix are in [Project_Charter.md](Project_Charter.md). Course checkpoints and revised course dates should be confirmed against the course portal.

## Project target governance
The revised D1 DOCX is the current D1 version for the adopted EBITDA Margin scope. The earlier PDF is superseded and should not be used as the active charter target. The editable charter and the D1 deliverables index now identify EBITDA Margin as the target.

## GitHub file status
The revised DOCX has been received, rendered and checked locally, but the DOCX binary has not been committed to GitHub. The repository records its exact filename/hash and intended location so the remaining upload can be verified without confusing it with the superseded PDF.
