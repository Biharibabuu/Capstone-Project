# M6 / D6 — Deployment and Monitoring: Evaluation Record

**Status:** Scaffold exists; end-to-end model integration and monitoring evidence remain pending.

## Components already in GitHub
- FastAPI: backend/main.py, backend/routes.py, backend/schemas.py.
- Interface: frontend/index.html, frontend/app.js, frontend/styles.css.
- Connectors: src/connectors/fx_client.py, brent_client.py, cpi_client.py, wpi_client.py.
- Refresh/store: src/market_refresh.py and src/market_store.py.
- Guide: docs/LIVE_DATA_INTEGRATION.md.

## Current state
Four independent market connectors handle USD/INR, Brent, CPI and WPI; refresh/store code records source/fetch metadata and retains last successful observations on provider failures. Secrets must remain in environment variables or a hosting secret manager. The D4 persistence rule is not yet integrated as an approved prediction service; do not claim production ML deployment.

## Remaining work
1. Complete D5 and register the approved model/version.
2. Align training/live features and test prediction routes on fixed cases.
3. Verify provider schemas, units, quotas, freshness and data-use/display rights.
4. Add scheduled refresh and stale/missing-data fallback.
5. Add auth, secret management, validation, rate limits and failure/security tests.
6. Monitor freshness, missingness, source failures, drift, prediction error, model version and retraining triggers.
7. Produce deployment architecture, release instructions and demo runbook.

Expected evidence: architecture note, API/failure test report, monitoring thresholds, environment/release guide and demo walkthrough.
