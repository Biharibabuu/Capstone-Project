# Analytics source code

Planned modules:
- data_pipeline.py: validate and prepare source-derived quarterly observations.
- features.py: target engineering, lags and validated features.
- train.py: baseline and candidate experiments.
- predict.py: controlled inference using the same preprocessing used during training.
- scenarios.py: low-cost/favourable, base and high-cost/adverse sensitivity inputs.

Do not freeze predictor names until D2 data audit and D3 EDA establish coverage, definitions and forecast-date availability. Record experiment settings and metrics. All evaluation must preserve time order.
