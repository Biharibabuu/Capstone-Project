# Tests

Planned test coverage:
- input schema and non-finite values;
- quarter-key uniqueness and date ordering;
- revenue/PAT unit and margin calculations;
- missing/stale inputs and source publication dates;
- feature pipeline consistency between training and prediction;
- chronological split and leakage prevention;
- API health and disabled-prediction behaviour before a model is validated;
- end-to-end HTML → API → ML → prediction path after the model is implemented.
