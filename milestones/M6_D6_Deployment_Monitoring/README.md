# M6 / D6 — Deployment and Monitoring

Status: Todo — not started. Existing API, frontend and connector scaffolding are reusable components, not completion of D6. The repository contains a FastAPI scaffold, HTML/CSS/JS frontend and four external data connectors. The evaluated model is not yet integrated into the prediction route.

Existing components: backend/main.py, backend/routes.py, backend/schemas.py; frontend/index.html, app.js and styles.css; src/connectors for USD/INR, Brent, CPI and WPI; src/market_refresh.py and src/market_store.py; docs/LIVE_DATA_INTEGRATION.md.

Remaining work: register only the D5-approved model; align training/live feature definitions; add scheduled refresh with appropriate cadences; monitor freshness, missingness, source failures, model version, prediction errors and drift; use a secret manager for hosted deployment; add security/failure-mode tests.

Expected evidence: deployment architecture note; API test report; monitoring plan and thresholds; environment/release instructions; demonstration screenshots or walkthrough.

## Folder structure

- `backend/` — API integration and validation tests (canonical source currently under repository `backend/`).
- `frontend/` — web application source (canonical source currently under repository `frontend/`).
- `reports/` — architecture, API test and monitoring evidence.
- `references/` — deployment/security references.
- `MILESTONE_CONTROL.md`, `DELIVERABLES_CHECKLIST.md` and `MILESTONE_MANIFEST.csv` — governance and evidence tracking.
