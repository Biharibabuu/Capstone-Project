# M6 / D6 — Deployment and Monitoring: Milestone Control

**Status:** PROTOTYPE SCAFFOLD EXISTS; MODEL INTEGRATION AND END-TO-END ACCEPTANCE PENDING.

## Purpose
Expose the approved evaluated forecast through an API and web interface, refresh market inputs, show data freshness and monitor data/model health.

## Inputs
A D5-approved model and exact feature contract are required. The current repository has a FastAPI scaffold, frontend and four market connectors (USD/INR, Brent, CPI, WPI); do not represent these as a validated prediction service.

## Working record
backend/, frontend/, src/connectors/, src/market_refresh.py, src/market_store.py and docs/LIVE_DATA_INTEGRATION.md.

## Deliverables
Deployment architecture note, API release instructions, monitoring plan and demo runbook; pending.

## Evidence
Unit/integration/API tests, feature parity, source freshness, failure handling, secret/security checks, monitoring metrics and demonstration record; pending.

## Exit gate
Integrate only the D5-approved model; prove training/live feature parity; reject stale or missing inputs; record data/model versions; keep secrets server-side; test provider failures and monitoring triggers before calling the application deployable.
