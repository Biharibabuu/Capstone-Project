import pandas as pd
import pytest
import sys
from pathlib import Path

for parent in Path(__file__).resolve().parents:
    if (parent / "src" / "d4_train.py").exists():
        sys.path.insert(0, str(parent))
        break

from src.d4_train import FEATURES, SPLIT_WINDOWS, prepare_supervised_data, split_data


def sample_rows():
    rows = []
    quarters = [(y, f"Q{q}") for y in range(2017, 2027) for q in range(1, 5)]
    for year, quarter in quarters:
        status = "Not available in source" if (year, quarter) in {(2017, "Q1"), (2017, "Q2")} else "Reported (original value)"
        x = len(rows) + 1
        rows.append({
            "Year": year, "Quarter (Calendar)": quarter,
            "PAT Margin": float(x), "EBITDA Margin": float(x + 1),
            "USD INR (Quarterly Mean)": 80.0 + x,
            "CPI inflation (Quarterly Mean)": 3.0 + x / 100,
            "WPI inflation (Quarterly Mean)": 2.0 + x / 100,
            "Oil benchmark(MONTHLY) (Quarterly Mean)": 70.0 + x,
            "Oil benchmark(DAILY) (Quarterly Mean)": 71.0 + x,
            "Financial Data Status": status,
        })
    return pd.DataFrame(rows)


def test_features_are_shifted_from_previous_reported_quarter():
    supervised = prepare_supervised_data(sample_rows())
    first = supervised.iloc[0]
    assert first["target_quarter"] == "2017Q4"
    assert first["forecast_origin_quarter"] == "2017Q3"
    assert first["lag1_pat_margin_pct"] == pytest.approx(3.0)
    assert len(FEATURES) == 6


def test_fixed_chronological_split_windows_are_complete():
    data = prepare_supervised_data(sample_rows())
    splits = split_data(data)
    assert {k: len(v) for k, v in splits.items()} == {"train": 21, "validation": 6, "test": 8}
    assert SPLIT_WINDOWS["train"][1] < SPLIT_WINDOWS["validation"][0]
    assert SPLIT_WINDOWS["validation"][1] < SPLIT_WINDOWS["test"][0]
