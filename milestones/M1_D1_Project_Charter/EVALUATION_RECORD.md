# M1 / D1 — Project Charter: Evaluation Record

**Status:** Completed — D1 PDF received and reviewed; GitHub binary upload pending  
**Team:** Nikhil Raj, Krishan Sharma and K. Shreya

## Project definition
**Project:** IndiGo Profitability Intelligence System.

**Business problem:** quarterly profitability may be affected by fuel-price movements, USD/INR, inflation and operating/demand conditions. The capstone tests whether historical financial performance and selected market indicators can support a one-quarter-ahead profitability forecast and scenario planning.

**Analytics question:** Can information available before a target quarter estimate IndiGo's next-quarter PAT margin?

**Target:** PAT margin (%) = PAT / Revenue from Operations × 100. This is profitability forecasting, not a share-price forecast.

**Decision use:** provide a transparent estimate with input context, limitations and low/base/high sensitivity scenarios.

## Scope and boundaries
- Historical financials and selected external indicators; audit, source lineage, quarter alignment, cleaning, EDA, baseline and challenger testing.
- Chronological evaluation, explainability where supported, scenario analysis and a local HTML/API prototype.
- Target-quarter unpublished PAT/revenue are labels, never predictors.
- Correlation is not causation; this is not guaranteed forecasting or investment advice.

## Team and course sequence
The charter's role split and responsibility matrix are in [Project_Charter.md](Project_Charter.md). Course checkpoints: D1 16-Oct; D2 23-Oct; D3 28-Oct; D4 course checkpoint 2-Nov (D4-v1 actually executed 7-Nov); D5 5-Nov (pending); D6 6-Nov (scaffold exists); D7 11-Nov (planned). Use the course portal for formally revised dates.

## Files in this milestone
- Project_Charter.md — full problem, target, scope, team and risk record.
- README.md and MILESTONE_MANIFEST.csv — folder guide and file register.
- Shared integrated plan: [docs/Master_Project_Plan.md](../../docs/Master_Project_Plan.md).
- [Course and artifact inventory](../ARTIFACT_INVENTORY_2026-11-07.csv) records original charter PDF/DOCX and course-outline DOCX; the editable Markdown charter/plan are canonical in GitHub.


## Submitted D1 PDF — received 8 November 2026

The submitted file is `IndiGo_Macroeconomic_Profitability_Capstone_M1.pdf`, a nine-page Module 1 Project Charter Foundation document. Original upload SHA-256: `408f2a67f038013b124c5ef4e9818c3e56b1866dd4601a7eb792797342f02676`.

The PDF frames IndiGo's profitability forecasting problem using public company financial information and macroeconomic indicators. It defines PAT margin (PAT / Revenue from Operations × 100) as the primary one-quarter-ahead target and EBITDAR margin as a secondary indicator. It includes business context, an HBI problem-framing application, a problem statement, decision/analytics questions, four working hypotheses, scope boundaries, initial data plan, modelling approach, stakeholders, feasibility risks and public-data references.

The source PDF has been received and inspected but its binary has not been committed to GitHub through the current write connection. See [M1 deliverables README](03_DELIVERABLES/README.md) for the transparent upload status.
