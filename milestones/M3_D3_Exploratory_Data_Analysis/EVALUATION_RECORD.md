# M3 / D3 — EDA: Evaluation Record

**Status:** Reviewed. GitHub includes a source-only notebook and review notes. Output-rich local exports are not published.

## Pre-specified hypotheses
- H1: Dated Brent and PAT margin are associated.
- H2: USD/INR and PAT margin are associated.
- H3: CPI inflation and PAT margin are associated.
- H4: WPI inflation and PAT margin are associated.
- H5: PAT margin differs across Indian fiscal quarters.
- H6: PAT and EBITDA margins move together.

Report sample sizes/effect sizes alongside statistical tests. Associations are exploratory, not causal claims or model-performance results.

## Analysis controls
- Rebuild financial results from raw Bloomberg IS; the legacy master Financial source is shifted by two quarters.
- Exclude estimated periods from realised outcome labels.
- Indian fiscal quarters: Q1 Apr-Jun, Q2 Jul-Sep, Q3 Oct-Dec, Q4 Jan-Mar.
- EUCRBRDT is Dated Brent, not Indian ATF/realised IndiGo fuel cost.
- Distinguish observation dates and publication/availability dates.
- EDA is not forecasting evaluation; model testing requires chronological splits and a baseline.

## Files
- 03_eda.ipynb — source-only notebook with outputs cleared.
- D3_Review_Notes.md — source lineage, findings and modelling handoff.
- README.md and MILESTONE_MANIFEST.csv — folder guide and file list.
- Shared canonical files: [notebooks/03_eda.ipynb](../../notebooks/03_eda.ipynb), [reports/D3_eda/README.md](../../reports/D3_eda/README.md).

The Library holds ANCP_T##_D3_eda(1).ipynb (1,079,048 bytes) and .html (1,022,352 bytes), plus earlier PDF/ZIP/HTML/notebook versions. They are catalogued centrally but not published because outputs may expose Bloomberg-derived figures/values. Rerun the source notebook locally using authorised data for private evaluation.
