# M4 / D4 — Modelling Input Data

**Status:** M4 is In Progress. This folder contains the modelling snapshot; do not overwrite it in place.

## Dataset stored in this milestone

[Final_Quarterly_Data(1).xlsx](Final_Quarterly_Data%281%29.xlsx)

- SHA-256: 87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970
- Worksheets: Final_Quarterly_Data, Calculation Audit, Data Quality Checks.
- This exact file is also stored in the M2 audit folder as the versioned derived quarterly workbook.

## Active target and legacy evidence

The active project target is next-quarter EBITDA margin. Older D4-v1 experiment artifacts report a PAT-margin experiment. Preserve them as historical/legacy evidence; they are not an approved EBITDA-margin model. M4 must run and document a fresh EBITDA-target training workflow based on the M3 output and create a separate experiment version.

## Candidate predictors

Use only fields supported by the approved M2/M3 package: USD/INR, CPI, WPI and supplied daily/monthly oil-benchmark proxies. Document date/frequency aggregation and feature availability. Do not claim load factor, yield, capacity, ATF spend or passenger-demand features are present.

## Modelling controls

- Use chronological or rolling/expanding splits; do not shuffle time-series observations.
- Document target/predictor periods, leakage controls, row exclusions and split boundaries.
- Record input hashes, code version, parameters, seed and environment for every run.
- Never overwrite D4-v1 historical inputs/results; create a new named experiment version.
