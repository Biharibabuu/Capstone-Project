# M4 Data Folder — Modelling Inputs and Snapshots

M4 consumes versioned, approved datasets; it does not silently modify the M2 source workbooks.

## D4-v1 locked input

- Canonical path: [data/processed/Final_Quarterly_Data(1).xlsx](../../../data/processed/Final_Quarterly_Data%281%29.xlsx)
- Worksheet: `Final_Quarterly_Data`
- SHA-256: `85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c`
- Snapshot status: immutable D4-v1 benchmark input.

## Related modelling data and evidence

- D4 input manifest: [experiments/D4_data_manifest.json](../experiments/D4_data_manifest.json)
- D4 metrics: [experiments/D4_metrics.json](../experiments/D4_metrics.json)
- D4 predictions: [experiments/D4_test_predictions.csv](../experiments/D4_test_predictions.csv)
- Training code: [src/d4_train.py](../src/d4_train.py)
- Experiment notebook: [notebooks/D4_modeling_experiment.ipynb](../notebooks/D4_modeling_experiment.ipynb)

## Rules

1. Never overwrite the D4-v1 input snapshot.
2. Every new data version gets a new filename, source manifest and SHA-256.
3. Do not use unreconciled or rights-pending workbooks as training data.
4. Keep raw source files in M2's canonical data location; record their exact paths here rather than duplicating binaries.
5. New modelling datasets must record target definition, fiscal-quarter key, feature availability cut-off, row exclusions and train/validation/test period boundaries.
