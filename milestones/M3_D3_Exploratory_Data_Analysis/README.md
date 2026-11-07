# M3 / D3 — Exploratory Data Analysis

**Status:** Done — D3 analysis and review package completed. The public repository copy is source-only; analysis code and markdown are retained, while saved outputs are cleared to avoid republishing Bloomberg-derived figures or values.

## Milestone files

- [`ANCP_T##_D3_eda.ipynb`](ANCP_T##_D3_eda.ipynb) — latest uploaded D3 EDA notebook (35 cells; outputs cleared).
- [`D3_Review_Notes.md`](D3_Review_Notes.md) — source lineage, review findings, analytical controls and modelling handoff.
- [`EVALUATION_RECORD.md`](EVALUATION_RECORD.md) — D3 evaluation record, hypotheses and data-quality controls.
- [`MILESTONE_MANIFEST.csv`](MILESTONE_MANIFEST.csv) — file inventory and canonical-source references.

The shared notebook copy at [`notebooks/03_eda.ipynb`](../../notebooks/03_eda.ipynb) is synchronized with the milestone notebook.

## Data and reproducibility

The notebook expects authorized local copies of its input workbooks. The input workbooks are not embedded in this milestone folder. Keep raw source workbooks unchanged and local; record source definitions, units, observed dates and publication/availability dates before deriving the analysis panel.

The uploaded notebook contained rendered tables and charts. These saved outputs were removed from the public copy in accordance with the project's existing data-governance note. Run the notebook locally with authorized source data to regenerate the outputs. Do not publish Bloomberg exports or derived values unless redistribution is permitted by the applicable licence.

## Handoff to M4 / D4

Before promoting EDA findings into modelling, reconcile financial margins to the raw Bloomberg income-statement source, exclude estimated quarters from realised outcomes, use Indian fiscal-quarter labels, and check that every feature was available by the forecast cutoff. Exploratory association is not evidence of causation or forecast performance.

## Standard folder structure

- `notebooks/` — reproducible EDA notebook source.
- `data/` — input lineage and data-version references.
- `reports/` — review notes, insight log and summary.
- `references/` — source and method references.
- `MILESTONE_CONTROL.md` and `DELIVERABLES_CHECKLIST.md` — milestone governance and closure evidence.

The source-only notebook is the governed public artifact. Do not add Bloomberg-derived rendered outputs until redistribution permission is confirmed; preserve local reproducibility instructions and source lineage.
