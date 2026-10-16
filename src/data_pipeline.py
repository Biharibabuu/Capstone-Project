"""Validation helpers for public IndiGo quarterly financial data.

Expected working columns follow the project data dictionary. Raw source files should
remain unchanged; these functions return a prepared copy for analysis.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

REQUIRED_COLUMNS = {"quarter_end", "revenue_inr_mn", "pat_inr_mn"}


class DataQualityError(ValueError):
    """Raised when a quarterly financial dataset fails a required quality check."""


def validate_and_prepare_financials(raw: pd.DataFrame) -> pd.DataFrame:
    """Validate required fields, sort quarters and calculate PAT margin.

    This function intentionally fails on missing/invalid required values rather than
    silently dropping records. Source definitions and units must be reconciled in D2.
    """
    missing_columns = sorted(REQUIRED_COLUMNS - set(raw.columns))
    if missing_columns:
        raise DataQualityError(
            "Missing required columns: " + ", ".join(missing_columns)
        )

    frame = raw.copy()
    frame["quarter_end"] = pd.to_datetime(frame["quarter_end"], errors="coerce")
    if frame["quarter_end"].isna().any():
        bad_rows = frame.index[frame["quarter_end"].isna()].tolist()
        raise DataQualityError(f"Invalid or missing quarter_end values in rows: {bad_rows}")

    if frame["quarter_end"].duplicated().any():
        duplicated = (
            frame.loc[frame["quarter_end"].duplicated(keep=False), "quarter_end"]
            .dt.strftime("%Y-%m-%d")
            .tolist()
        )
        raise DataQualityError("Duplicate quarter_end values: " + ", ".join(duplicated))

    for column in ("revenue_inr_mn", "pat_inr_mn"):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
        values = frame[column].to_numpy(dtype=float)
        invalid_mask = ~np.isfinite(values)
        if invalid_mask.any():
            bad_rows = frame.index[invalid_mask].tolist()
            raise DataQualityError(f"Invalid or missing {column} values in rows: {bad_rows}")

    if (frame["revenue_inr_mn"] <= 0).any():
        bad_rows = frame.index[frame["revenue_inr_mn"] <= 0].tolist()
        raise DataQualityError(f"Revenue must be greater than zero in rows: {bad_rows}")

    frame = frame.sort_values("quarter_end").reset_index(drop=True)
    frame["pat_margin_pct"] = (
        frame["pat_inr_mn"] / frame["revenue_inr_mn"]
    ) * 100.0
    return frame
