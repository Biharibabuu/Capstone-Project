import pandas as pd
import pytest

from src.data_pipeline import DataQualityError, validate_and_prepare_financials
from src.features import add_pat_margin_lags


def test_financial_validation_sorts_and_calculates_pat_margin():
    raw = pd.DataFrame(
        {
            "quarter_end": ["2025-06-30", "2025-03-31"],
            "revenue_inr_mn": [200.0, 100.0],
            "pat_inr_mn": [10.0, -5.0],
        }
    )

    result = validate_and_prepare_financials(raw)

    assert result["quarter_end"].is_monotonic_increasing
    assert result.loc[0, "pat_margin_pct"] == pytest.approx(-5.0)
    assert result.loc[1, "pat_margin_pct"] == pytest.approx(5.0)


def test_duplicate_quarters_are_rejected():
    raw = pd.DataFrame(
        {
            "quarter_end": ["2025-03-31", "2025-03-31"],
            "revenue_inr_mn": [100.0, 120.0],
            "pat_inr_mn": [10.0, 12.0],
        }
    )

    with pytest.raises(DataQualityError, match="Duplicate"):
        validate_and_prepare_financials(raw)


def test_nonpositive_revenue_is_rejected():
    raw = pd.DataFrame(
        {
            "quarter_end": ["2025-03-31"],
            "revenue_inr_mn": [0.0],
            "pat_inr_mn": [5.0],
        }
    )

    with pytest.raises(DataQualityError, match="greater than zero"):
        validate_and_prepare_financials(raw)


def test_lag_uses_previous_quarter_in_time_order():
    prepared = pd.DataFrame(
        {
            "quarter_end": ["2025-06-30", "2025-03-31", "2025-09-30"],
            "pat_margin_pct": [3.0, 1.0, 5.0],
        }
    )

    result = add_pat_margin_lags(prepared, max_lag=1)

    assert result["pat_margin_lag_1"].iloc[0] != result["pat_margin_lag_1"].iloc[0]
    assert result["pat_margin_lag_1"].iloc[1] == pytest.approx(1.0)
    assert result["pat_margin_lag_1"].iloc[2] == pytest.approx(3.0)
