# Frontend

The single user interface is planned in HTML, CSS and JavaScript.

Current state:
- Shows the project purpose and forecast/data-health status.
- Checks the API health endpoint when the page is opened.
- Clearly states that no prediction is available until the model is trained and validated.
- Does not invent forecasts or imply current unpublished company profit is known.

Serve locally, for example with the VS Code Live Server extension on port 5500, then run the API from the repository root:

    uvicorn backend.main:app --reload

The predictor input controls should be added after D2/D3 confirm which candidate variables are sufficiently covered and available at forecast time.
