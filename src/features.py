"""Small, auditable feature helpers.

The final feature list must be confirmed after the data audit and EDA. Do not add
external-variable features until their definitions, coverage and publication timing
have been verified.
"""
from __future__ import annotations

import pandas as pd

from src.data_pipeline import DataQualityError


def add_pat_margin_lags(
    prepared: pd.DataFrame, max_lag: int = 1
) -> pd.DataFrame:
    """Create prior-quarter PAT-margin lags in chronological order.

    The output retains early rows with missing lag values; the modelling pipeline
    must decide how to handle them within each training window without leakage.
    """
    if max_lag < 1:
        raise ValueError("max_lag must be at least 1.")
    required = {"quarter_end", "pat_margin_pct"}
    missing = sorted(required - set(prepared.columns))
    if missing:
        raise DataQualityError("Missing required columns: " + ", ".join(missing))

    frame = prepared.copy()
    frame["quarter_end"] = pd.to_datetime(frame["quarter_end"], errors="coerce")
    if frame["quarter_end"].isna().any():
        raise DataQualityError("quarter_end contains invalid or missing dates.")
    if frame["quarter_end"].duplicated().any():
        raise DataQualityError("quarter_end must be unique before feature creation.")

    frame = frame.sort_values("quarter_end").reset_index(drop=True)
    for lag in range(1, max_lag + 1):
        frame[f"pat_margin_lag_{lag}"] = frame["pat_margin_pct"].shift(lag)
    return frame
