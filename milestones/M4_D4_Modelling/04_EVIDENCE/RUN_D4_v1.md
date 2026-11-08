# D4-v1 Run Instructions

1. Use Python 3.10 or newer.
2. Create and activate a virtual environment:
   - Windows: `py -3.10 -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements-d4-v1.txt`
4. Put the approved input workbook beside the notebook and name it `EDA ANALYSIS.xlsx` (or update `DATA_PATH`). It must contain `Sheet1` and all required columns.
5. Open the notebook in Jupyter or Colab and run all cells in order.
6. The notebook reports metrics, plots holdout forecasts, saves `best_ebitda_model.pkl`, and prints a one-quarter-ahead forecast.

## Reproducibility caveats
- Original run timestamp, input workbook hash, exact package versions and quarter boundaries are not embedded in the supplied notebook.
- `random_state=42` is used for tree estimators; no global random seed is set.
- XGBoost is optional.
- Record exact data hash, `pip freeze`, commit SHA, run timestamp and quarter boundaries in future runs.
