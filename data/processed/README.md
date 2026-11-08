# Processed and Derived Data
### Shared datasets under M2 governance

This folder contains shared or historical derived datasets. It is not a scratch area for active model runs; current M4 training tables belong under milestones/M4_D4_Modelling/data/.

## Current file

| File | Role | Status |
|---|---|---|
| [Final_Quarterly_Data(1).xlsx](Final_Quarterly_Data%281%29.xlsx) | Pinned D4-v1 quarterly benchmark input with calculation and data-quality sheets | Immutable historical input; known mapping/quarter-label issues remain. Do not treat as the approved active EBITDA model table without reconciliation. |

## Candidate successor

Final_Quarterly_Data(3).xlsx was received locally with a different hash from D4-v1. It has not been committed or approved here. Before promotion:
1. Rebuild financial margins from raw CP IS rows and reported quarters.
2. Verify EBITDA and Revenue from Operations definitions and units.
3. Apply Indian fiscal-quarter labels.
4. Exclude estimated periods from actual labels.
5. Check missingness, duplicate quarters and anomalies.
6. Reconcile the 2020 Q4 discrepancy recorded in M3.
7. Record source hashes, transformation version, coverage, row counts and approval.

## Manifest requirements

Every processed file records filename, milestone owner, parent hashes, transformation, target definition, frequency, quarter convention, coverage, row count, units, actual/estimate treatment, quality status, approval date and SHA-256.

## Data flow

M2 approves or quarantines shared derived data. M3 owns its EBITDA-only EDA panel. M4 owns the active model-ready dataset. M5 freezes the exact M4 data vintage for backtesting. M6 and M7 consume approved artifacts without silently changing the target.