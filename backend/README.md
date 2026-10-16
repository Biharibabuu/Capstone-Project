# Backend

The backend will expose the Python forecasting engine through FastAPI (or Flask if selected after the prototype review).

Current state:
- /health reports whether a trained model artifact is available.
- /predict validates the request contract but intentionally returns HTTP 503 until a reviewed model and preprocessing pipeline exist.
- No fabricated forecast is returned.

Run from the repository root after installing dependencies from requirements.txt:

    uvicorn backend.main:app --reload

Open http://127.0.0.1:8000/docs for the local API documentation.

The final predictor schema must be decided after the data audit and EDA. Do not lock candidate variables into the API before coverage and forecast-date availability have been checked.
