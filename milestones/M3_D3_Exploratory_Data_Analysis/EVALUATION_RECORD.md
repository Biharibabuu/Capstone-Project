# M3 / D3 — EDA: Evaluation Record

**Status:** Latest D3 notebook uploaded to the M3 folder as a source-only public copy. The analysis code and markdown are retained; saved outputs are cleared to avoid republishing Bloomberg-derived figures or values.

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
- [ANCP_T##_D3_eda.ipynb](ANCP_T##_D3_eda.ipynb) — latest D3 notebook; all 35 cells are retained, with 69 saved outputs and 15 execution counters cleared in the public copy.
- [D3_Review_Notes.md](D3_Review_Notes.md) — source lineage, findings and modelling handoff.
- [README.md](README.md) and [MILESTONE_MANIFEST.csv](MILESTONE_MANIFEST.csv) — folder guide and file inventory.
- Shared notebook mirror: [notebooks/03_eda.ipynb](../../notebooks/03_eda.ipynb), synchronized with the M3 notebook.

The original output-rich uploaded file remains the local source copy. The public repository copy omits saved tables and charts to avoid redistributing Bloomberg-derived values. Rerun the notebook locally using authorised data to regenerate outputs for evaluation.
