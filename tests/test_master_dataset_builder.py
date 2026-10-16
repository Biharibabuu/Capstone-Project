from pathlib import Path

import pandas as pd
import pytest

from src.build_master_dataset import (
    DataQualityError,
    build_master_dataset,
    fiscal_quarter_label,
    fiscal_quarter_start,
)


def _write_csv(path: Path, rows: list[dict]) -> None:
    pd.DataFrame(rows).to_csv(path, index=False)


def _source_files(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)

    _write_csv(
        root / "financial_quarterly.csv",
        [
            {
                "quarter_end": "2023-12-31",
                "revenue_inr_mn": 2000,
                "pat_inr_mn": 100,
                "ebitdar_inr_mn": 200,
                "financial_published_on": "2024-02-15",
                "source_url": "https://example.test/financial-q3",
            },
            {
                "quarter_end": "2024-03-31",
                "revenue_inr_mn": 2200,
                "pat_inr_mn": 110,
                "ebitdar_inr_mn": 210,
                "financial_published_on": "2024-05-15",
                "source_url": "https://example.test/financial-q4",
            },
            {
                "quarter_end": "2024-06-30",
                "revenue_inr_mn": 2400,
                "pat_inr_mn": -20,
                "ebitdar_inr_mn": 220,
                "financial_published_on": "2024-08-15",
                "source_url": "https://example.test/financial-q1",
            },
            {
                "quarter_end": "2024-09-30",
                "revenue_inr_mn": 2600,
                "pat_inr_mn": 130,
                "ebitdar_inr_mn": 230,
                "financial_published_on": "2024-11-15",
                "source_url": "https://example.test/financial-q2",
            },
        ],
    )

    _write_csv(
        root / "operational_monthly.csv",
        [
            {
                "month_start": "2024-02-01",
                "passengers_carried": 5000000,
                "passenger_km_thousand": 1000000,
                "available_seat_km_thousand": 1200000,
                "passenger_load_factor_pct": "",
                "operational_published_on": "2024-03-12",
                "source_url": "https://example.test/ops-feb",
                "data_scope": "test",
            },
            {
                "month_start": "2024-03-01",
                "passengers_carried": 5100000,
                "passenger_km_thousand": 1050000,
                "available_seat_km_thousand": 1200000,
                "passenger_load_factor_pct": "",
                "operational_published_on": "2024-04-12",
                "source_url": "https://example.test/ops-mar",
                "data_scope": "test",
            },
            {
                "month_start": "2024-04-01",
                "passengers_carried": 5200000,
                "passenger_km_thousand": 1060000,
                "available_seat_km_thousand": 1200000,
                "passenger_load_factor_pct": "",
                "operational_published_on": "2024-05-12",
                "source_url": "https://example.test/ops-apr",
                "data_scope": "test",
            },
            {
                "month_start": "2024-05-01",
                "passengers_carried": 5300000,
                "passenger_km_thousand": 1080000,
                "available_seat_km_thousand": 1200000,
                "passenger_load_factor_pct": "",
                "operational_published_on": "2024-06-12",
                "source_url": "https://example.test/ops-may",
                "data_scope": "test",
            },
            {
                "month_start": "2024-06-01",
                "passengers_carried": 5400000,
                "passenger_km_thousand": 1100000,
                "available_seat_km_thousand": 1200000,
                "passenger_load_factor_pct": "",
                "operational_published_on": "2024-07-12",
                "source_url": "https://example.test/ops-jun",
                "data_scope": "test",
            },
        ],
    )

    _write_csv(
        root / "atf_monthly.csv",
        [
            {
                "month_start": month,
                "atf_price_inr_per_kl": price,
                "atf_published_on": month,
                "source_url": "https://example.test/atf",
                "proxy_definition": "Test price proxy",
            }
            for month, price in [
                ("2024-02-01", 90000),
                ("2024-03-01", 91000),
                ("2024-04-01", 92000),
                ("2024-05-01", 93000),
                ("2024-06-01", 94000),
                ("2024-07-01", 95000),
            ]
        ],
    )

    _write_csv(
        root / "usd_inr_daily.csv",
        [
            {"observation_date": day, "usd_inr": rate, "fx_published_on": day,
             "source_url": "https://example.test/fx"}
            for day, rate in [
                ("2024-03-28", 83.0),
                ("2024-06-28", 83.5),
                ("2024-07-02", 84.0),
            ]
        ],
    )

    _write_csv(
        root / "cpi_monthly.csv",
        [
            {"month_start": month, "cpi_index": index, "cpi_inflation_yoy_pct": inflation,
             "cpi_published_on": published, "source_url": "https://example.test/cpi",
             "series_base_year": "2024=100"}
            for month, index, inflation, published in [
                ("2024-01-01", 100.1, 5.0, "2024-02-12"),
                ("2024-02-01", 100.5, 4.9, "2024-03-12"),
                ("2024-03-01", 101.0, 4.8, "2024-04-12"),
                ("2024-04-01", 101.2, 4.7, "2024-05-12"),
                ("2024-05-01", 101.4, 4.6, "2024-06-12"),
                ("2024-06-01", 101.6, 4.5, "2024-07-12"),
            ]
        ],
    )
    return root


def test_fiscal_quarter_start_and_label():
    assert fiscal_quarter_start(pd.Timestamp("2024-06-30")) == pd.Timestamp("2024-04-01")
    assert fiscal_quarter_start(pd.Timestamp("2025-03-31")) == pd.Timestamp("2025-01-01")
    assert fiscal_quarter_label(pd.Timestamp("2024-07-01")) == "FY2024-25_Q2"


def test_builder_uses_only_data_published_by_cutoff(tmp_path):
    raw_dir = _source_files(tmp_path / "raw")
    master, report = build_master_dataset(raw_dir)

    target_q2 = master.loc[master["target_quarter_start"] == pd.Timestamp("2024-07-01")].iloc[0]

    assert target_q2["forecast_as_of_date"] == pd.Timestamp("2024-06-30")
    assert target_q2["target_quarter"] == "FY2024-25_Q2"
    # Q1 result was not yet published on June 30; use Q4 financials published in May.
    assert target_q2["latest_reported_financial_quarter_end"] == pd.Timestamp("2024-03-31")
    # June operational statistics were published after the cutoff, so May is selected.
    assert target_q2["latest_operational_month"] == pd.Timestamp("2024-05-01")
    # June CPI was published after the cutoff, so May is selected.
    assert target_q2["latest_cpi_month"] == pd.Timestamp("2024-05-01")
    # ATF and FX observations in the target quarter must not be used.
    assert target_q2["latest_atf_month"] == pd.Timestamp("2024-06-01")
    assert target_q2["latest_fx_observation_date"] == pd.Timestamp("2024-06-28")
    # Target is next-quarter PAT margin, not the origin or latest released PAT margin.
    assert target_q2["target_pat_margin_pct"] == pytest.approx(130 / 2600 * 100)
    assert target_q2["target_financial_published_on"] > target_q2["forecast_as_of_date"]
    assert report.loc[report["metric"] == "leakage_violations", "value"].iloc[0] == 0


def test_invalid_quarter_end_is_rejected():
    with pytest.raises(DataQualityError):
        fiscal_quarter_start(pd.Timestamp("2024-06-29"))
