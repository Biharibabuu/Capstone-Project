# M6 / D6 — Deployment Inputs

**Status:** Todo — deployment has not started.

## Required upstream contracts

| Input | Owner | Required content |
|---|---|---|
| Approved model | M5 / D5 | Model version, approval decision, evaluation report and limitations |
| Feature contract | M4 / D4 and M5 / D5 | Field names, units, transformations, lag logic, cadence and missing-value behaviour |
| Source catalogue | M2 / D2 | Source IDs, rights/access notes, frequency and publication timing |
| Forecast target | M1 / D1 | Next-quarter EBITDA Margin definition and forecast horizon |

## Data responsibility

D6 does not own or duplicate the historical training dataset. It owns runtime request schemas, refreshed source observations, timestamps, freshness checks, prediction logs and monitoring events.

## Planned runtime records

- source_refresh_log.csv — provider, timestamp, response status and retrieved period.
- feature_snapshot.json — inference features and availability timestamps.
- forecast_log.csv — forecast origin, target quarter, model version and predicted EBITDA Margin.
- data_health_log.csv — missingness, stale-source and schema-validation outcomes.

These are planned outputs, not currently committed data records. Keep credentials and provider secrets outside GitHub.