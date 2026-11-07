# M5 / D5 — Model Evaluation

Status: Todo — not started. This folder is an evaluation checklist, not a claim that D5 is complete.

Required work:
1. Preserve the D4-v1 data snapshot and model-selection decision.
2. Add release-date/vintage controls and point-in-time feature eligibility.
3. Run expanding-window or rolling-origin backtests where history permits.
4. Compare persistence and candidate models using MAE and RMSE.
5. Analyse errors by period/regime, especially exceptional loss quarters.
6. Quantify uncertainty and document when forecasting should be withheld.
7. Produce an evaluation memo and updated experiment log.

D4 handoff: persistence was selected because Ridge and Random Forest did not improve validation MAE. Locked test MAE was 11.53 pp; the eight-quarter holdout is small and historical release timestamps are unavailable.

Expected evidence: D5 evaluation report PDF; rolling-origin code/notebook; updated log; error-analysis CSV; metrics JSON; model card; data/environment manifests.

## Folder structure

- `notebooks/` — rolling-origin evaluation notebook.
- `experiments/` — run log, metrics and error analysis.
- `reports/` — evaluation memo/report.
- `references/` — validation protocol and methodological sources.
- `MILESTONE_CONTROL.md`, `DELIVERABLES_CHECKLIST.md` and `MILESTONE_MANIFEST.csv` — governance and evidence tracking.
