# M6 / D6 — Deployment and Monitoring

Status: In progress/planned. The repository contains a FastAPI scaffold, HTML/CSS/JS frontend and four external data connectors. The evaluated model is not yet integrated into the prediction route.

Existing components: backend/main.py, backend/routes.py, backend/schemas.py; frontend/index.html, app.js and styles.css; src/connectors for USD/INR, Brent, CPI and WPI; src/market_refresh.py and src/market_store.py; docs/LIVE_DATA_INTEGRATION.md.

Remaining work: register only the D5-approved model; align training/live feature definitions; add scheduled refresh with appropriate cadences; monitor freshness, missingness, source failures, model version, prediction errors and drift; use a secret manager for hosted deployment; add security/failure-mode tests.

Expected evidence: deployment architecture note; API test report; monitoring plan and thresholds; environment/release instructions; demonstration screenshots or walkthrough.