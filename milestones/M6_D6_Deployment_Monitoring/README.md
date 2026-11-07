# M6 / D6 — Deployment and Monitoring

**Status:** TODO — NOT STARTED

## Brief
Package the D5-approved forecasting logic into a tested API and user interface, then monitor data and prediction quality. Existing scaffolding is reusable groundwork, not a completed deployment milestone.

## Workflow
1. Receive the D5-approved model, feature schema and preprocessing contract.
2. Integrate that exact model into the API prediction route.
3. Align live feature definitions and update cadence with training.
4. Validate API inputs, output schema, errors and frontend integration.
5. Configure secrets securely and document local/hosted run instructions.
6. Log forecast time, input vintage, model version and prediction.
7. Monitor freshness, missingness, source failures, feature drift and prediction errors when actuals arrive.
8. Run an end-to-end demo and document limitations.

## Inputs and data
D5-approved model artifact; M2 source register; live connectors for USD/INR, Brent, CPI and WPI; M4/M5 approved feature schema, transformations and units. Training data remain governed by M2/M4; the frontend must not recreate them.

## Planned deliverables
Deployment architecture/API contract; model integration and API/frontend tests; refresh/store workflow; monitoring plan and thresholds; deployment runbook, security notes and demo evidence.

## Dependencies and exit gate
Do not integrate an unapproved M4 candidate. D6 starts only after D5 provides an approved model and reproducible input contract.
