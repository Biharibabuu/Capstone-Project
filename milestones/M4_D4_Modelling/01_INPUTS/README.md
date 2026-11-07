# M4 — Inputs and Data Contracts

## Current modelling input snapshot
- [Final_Quarterly_Data(1).xlsx](../data/Final_Quarterly_Data%281%29.xlsx) — copied into the M4 milestone data folder; SHA-256: 87e56b4a08a81740c93386f62845bb48de53d0cbea754427b0da3d5b8fd5d970.
- [M3 EBITDA-only EDA panel](../../M3_D3_Exploratory_Data_Analysis/data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv) — 38-quarter analysis handoff.

## Important distinction
The locked historic D4-v1 input used a PAT-margin target and is retained as a legacy experiment. The new active modelling task is EBITDA margin. Do not treat the old PAT results as current M4 EBITDA model performance.

## Source lineage
Raw statement and macro/market source workbooks and source definitions are maintained under [M2 data](../../M2_D2_Data_Audit/data/README.md). Every new M4 dataset must be versioned, checksummed and tied to source hashes and transformation steps.

## Required validation before training
Confirm target denominator, actual/estimate status, dates/quarter alignment, feature availability and missingness. Use chronological splits and do not bridge missing quarterly target observations.
