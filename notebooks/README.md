# Notebooks workflow

Suggested order:
1. data_audit.ipynb — coverage, sources, missingness, dates, units and duplicates.
2. eda.ipynb — trends, relationships, anomalies, seasonality and hypotheses.
3. baseline.ipynb — simple baseline and time-ordered evaluation setup.
4. experiments.ipynb — Ridge/Elastic Net and any justified nonlinear candidate.
5. evaluation.ipynb — chronological/rolling-origin errors, leakage checks, stability and limitations.

Keep raw data unchanged. Avoid random quarter shuffling. Record metrics, splits, feature sets and decisions so results are reproducible.
