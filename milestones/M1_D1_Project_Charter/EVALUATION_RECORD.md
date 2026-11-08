# M1 / D1 — Project Charter: Evaluation Record

**Status:** Revised EBITDA-focused D1 content reviewed; DOCX binary upload pending.  
**Team:** Nikhil Raj, Krishan Sharma and K. Shreya

## Project definition
**Project:** IndiGo Profitability Intelligence System.

**Business problem:** quarterly profitability may be affected by fuel-price movements, USD/INR, inflation and operating/demand conditions. The capstone tests whether historical financial performance and selected market indicators can support a one-quarter-ahead profitability forecast and scenario planning.

**Adopted project target:** **EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.** This is profitability forecasting, not a share-price forecast.

## Current D1 document
- Filename: `IndiGo_Macroeconomic_Profitability_Capstone_M1.docx`
- Format: DOCX, 9 pages
- Received: 8 November 2026
- SHA-256: `d96c5cddecd2cb33e5eaceca61c7387b43468481c1d22d0a68f8a295c0a52e9f`
- Page 3 explicitly identifies EBITDA Margin as the primary analytical output.
- Page 7 lists EBITDA Margin as the company-profitability target.
- Page 8 describes baseline/model comparison, chronological validation, out-of-sample MAE/RMSE and low/base/high-cost scenario analysis.

## Scope and boundaries
- Historical financials and selected external indicators; audit, source lineage, quarter alignment, cleaning, EDA, baseline and challenger testing.
- Chronological evaluation, explainability where supported, scenario analysis and a local HTML/API prototype.
- Target-quarter EBITDA and Revenue from Operations are labels used to calculate EBITDA Margin, never predictors.
- Correlation is not causation; this is not guaranteed forecasting or investment advice.

## Repository file status
The revised DOCX has been received and reviewed locally, but the DOCX binary is not yet committed to GitHub. No D1 PDF is retained in the M1 folder or in the milestone manifest. The editable charter and README identify the EBITDA Margin target.
