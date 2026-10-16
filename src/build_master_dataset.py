"""Build a point-in-time master dataset for next-quarter IndiGo PAT-margin forecasting.

Inputs are normalized source extracts in data/raw/. The script does not scrape websites
and does not fabricate publication dates. See docs/Phase1_Data_Collection_Plan.md.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


class DataQualityError(ValueError):
    """Raised when source data violate the dataset's minimum quality contract."""


SOURCE_FILES = {
    "financials": "financial_quarterly.csv",
    "operations": "operational_monthly.csv",
    "atf": "atf_monthly.csv",
    "fx": "usd_inr_daily.csv",
    "cpi": "cpi_monthly.csv",
}

OUTPUT_FEATURE_COLUMNS = [
    "latest_reported_revenue_inr_mn",
    "latest_reported_pat_inr_mn",
    "latest_reported_pat_margin_pct",
    "latest_reported_ebitdar_inr_mn",
    "latest_passengers_carried",
    "latest_passenger_load_factor_pct",
    "latest_atf_price_inr_per_kl",
    "latest_usd_inr",
    "latest_cpi_index",
    "latest_cpi_inflation_yoy_pct",
]

TARGET_ONLY_COLUMNS = [
    "target_revenue_inr_mn",
    "target_pat_inr_mn",
    "target_pat_margin_pct",
    "target_financial_published_on",
    "target_financial_source_url",
]


def fiscal_quarter_start(quarter_end: pd.Timestamp) -> pd.Timestamp:
    """Derive quarter start for Indian fiscal quarters ending Mar/Jun/Sep/Dec."""
    q_end = pd.Timestamp(quarter_end).normalize()
    if q_end.month not in (3, 6, 9, 12) or q_end != q_end + pd.offsets.MonthEnd(0):
        raise DataQualityError(
            f"quarter_end must be a calendar quarter-end date; received {q_end.date()}."
        )
    return q_end - pd.offsets.MonthEnd(3) + pd.Timedelta(days=1)


def fiscal_quarter_label(quarter_start: pd.Timestamp) -> str:
    """Return labels such as FY2024-25_Q1."""
    start = pd.Timestamp(quarter_start).normalize()
    q_by_month = {4: 1, 7: 2, 10: 3, 1: 4}
    if start.month not in q_by_month or start.day != 1:
        raise DataQualityError(
            f"quarter_start must be the first day of Apr/Jul/Oct/Jan; received {start.date()}."
        )
    fy_start = start.year if start.month >= 4 else start.year - 1
    fy_end_short = (fy_start + 1) % 100
    return f"FY{fy_start}-{fy_end_short:02d}_Q{q_by_month[start.month]}"


def _parse_date_column(frame: pd.DataFrame, column: str, path: Path) -> None:
    if column not in frame.columns:
        raise DataQualityError(f"{path}: missing required date column '{column}'.")
    parsed = pd.to_datetime(frame[column], errors="coerce")
    bad = parsed.isna()
    if bad.any():
        rows = (frame.index[bad] + 2).tolist()
        raise DataQualityError(
            f"{path}: invalid/missing dates in '{column}' at CSV line(s) {rows[:12]}."
        )
    frame[column] = parsed.dt.normalize()


def _numeric_column(
    frame: pd.DataFrame,
    column: str,
    path: Path,
    *,
    required: bool,
    positive: bool = False,
    nonnegative: bool = False,
) -> None:
    if column not in frame.columns:
        if required:
            raise DataQualityError(f"{path}: missing required numeric column '{column}'.")
        frame[column] = np.nan
        return

    raw = frame[column].replace(r"^\s*$", np.nan, regex=True)
    parsed = pd.to_numeric(raw, errors="coerce")
    malformed = raw.notna() & parsed.isna()
    if malformed.any():
        rows = (frame.index[malformed] + 2).tolist()
        raise DataQualityError(
            f"{path}: non-numeric values in '{column}' at CSV line(s) {rows[:12]}."
        )
    if required and parsed.isna().any():
        rows = (frame.index[parsed.isna()] + 2).tolist()
        raise DataQualityError(
            f"{path}: missing required values in '{column}' at CSV line(s) {rows[:12]}."
        )
    values = parsed.dropna().to_numpy(dtype=float)
    if not np.isfinite(values).all():
        raise DataQualityError(f"{path}: '{column}' contains infinite values.")
    if positive and (parsed.dropna() <= 0).any():
        raise DataQualityError(f"{path}: '{column}' must be greater than zero.")
    if nonnegative and (parsed.dropna() < 0).any():
        raise DataQualityError(f"{path}: '{column}' must be zero or greater.")
    frame[column] = parsed


def _load_source(path: Path, required_columns: set[str]) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Required source file not found: {path}. Copy the matching CSV template "
            "from data/templates/ into data/raw/ and populate it with documented data."
        )
    frame = pd.read_csv(path, dtype=str)
    if frame.empty:
        raise DataQualityError(
            f"{path} has a header but no records. Populate the file before building the dataset."
        )
    missing = sorted(required_columns - set(frame.columns))
    if missing:
        raise DataQualityError(f"{path}: missing required columns: {', '.join(missing)}.")
    if "source_url" in frame.columns:
        urls = frame["source_url"].fillna("").astype(str).str.strip()
        if urls.eq("").any():
            rows = (frame.index[urls.eq("")] + 2).tolist()
            raise DataQualityError(
                f"{path}: source_url is missing at CSV line(s) {rows[:12]}."
            )
    return frame


def _assert_unique(frame: pd.DataFrame, column: str, path: Path) -> None:
    duplicates = frame[column].duplicated(keep=False)
    if duplicates.any():
        samples = frame.loc[duplicates, column].astype(str).tolist()[:10]
        raise DataQualityError(
            f"{path}: duplicate '{column}' values {samples}. Aggregate/resolve duplicates first."
        )


def load_financials(input_dir: Path) -> pd.DataFrame:
    path = input_dir / SOURCE_FILES["financials"]
    frame = _load_source(
        path,
        {"quarter_end", "revenue_inr_mn", "pat_inr_mn", "financial_published_on", "source_url"},
    )
    _parse_date_column(frame, "quarter_end", path)
    _parse_date_column(frame, "financial_published_on", path)
    _assert_unique(frame, "quarter_end", path)

    valid_quarter_end = (
        frame["quarter_end"].dt.month.isin([3, 6, 9, 12])
        & frame["quarter_end"].eq(frame["quarter_end"] + pd.offsets.MonthEnd(0))
    )
    if not valid_quarter_end.all():
        raise DataQualityError(
            f"{path}: quarter_end must be Mar/Jun/Sep/Dec month-end dates."
        )
    if (frame["financial_published_on"] < frame["quarter_end"]).any():
        raise DataQualityError(
            f"{path}: financial_published_on precedes the quarter end. Use the actual publication date."
        )
    _numeric_column(frame, "revenue_inr_mn", path, required=True, positive=True)
    _numeric_column(frame, "pat_inr_mn", path, required=True)
    _numeric_column(frame, "ebitdar_inr_mn", path, required=False)

    frame["quarter_start"] = frame["quarter_end"].map(fiscal_quarter_start)
    frame["fiscal_quarter"] = frame["quarter_start"].map(fiscal_quarter_label)
    frame["pat_margin_pct"] = frame["pat_inr_mn"] / frame["revenue_inr_mn"] * 100.0
    frame["source_url"] = frame["source_url"].astype(str).str.strip()
    return frame.sort_values("quarter_end").reset_index(drop=True)


def load_operations(input_dir: Path) -> pd.DataFrame:
    path = input_dir / SOURCE_FILES["operations"]
    frame = _load_source(
        path,
        {"month_start", "passengers_carried", "operational_published_on", "source_url"},
    )
    _parse_date_column(frame, "month_start", path)
    _parse_date_column(frame, "operational_published_on", path)
    _assert_unique(frame, "month_start", path)
    if not frame["month_start"].dt.day.eq(1).all():
        raise DataQualityError(f"{path}: month_start must be the first day of each month.")

    _numeric_column(frame, "passengers_carried", path, required=True, nonnegative=True)
    _numeric_column(frame, "passenger_km_thousand", path, required=False, nonnegative=True)
    _numeric_column(frame, "available_seat_km_thousand", path, required=False, positive=True)
    _numeric_column(
        frame, "passenger_load_factor_pct", path, required=False, nonnegative=True
    )

    has_rpk = frame["passenger_km_thousand"].notna()
    has_ask = frame["available_seat_km_thousand"].notna()
    if (has_rpk ^ has_ask).any():
        raise DataQualityError(
            f"{path}: passenger_km_thousand and available_seat_km_thousand must be supplied together."
        )
    can_recompute = has_rpk & has_ask
    if can_recompute.any():
        frame.loc[can_recompute, "passenger_load_factor_pct"] = (
            frame.loc[can_recompute, "passenger_km_thousand"]
            / frame.loc[can_recompute, "available_seat_km_thousand"]
            * 100.0
        )
    if frame["passenger_load_factor_pct"].isna().any():
        raise DataQualityError(
            f"{path}: provide passenger_load_factor_pct or passenger-km and available seat-km for every row."
        )
    if (frame["passenger_load_factor_pct"] > 100).any():
        raise DataQualityError(f"{path}: passenger load factor cannot exceed 100 percent.")
    frame["source_url"] = frame["source_url"].astype(str).str.strip()
    return frame.sort_values("month_start").reset_index(drop=True)


def load_atf(input_dir: Path) -> pd.DataFrame:
    path = input_dir / SOURCE_FILES["atf"]
    frame = _load_source(
        path, {"month_start", "atf_price_inr_per_kl", "atf_published_on", "source_url"}
    )
    _parse_date_column(frame, "month_start", path)
    _parse_date_column(frame, "atf_published_on", path)
    _assert_unique(frame, "month_start", path)
    if not frame["month_start"].dt.day.eq(1).all():
        raise DataQualityError(f"{path}: month_start must be the first day of each month.")
    _numeric_column(frame, "atf_price_inr_per_kl", path, required=True, positive=True)
    frame["source_url"] = frame["source_url"].astype(str).str.strip()
    return frame.sort_values("month_start").reset_index(drop=True)


def load_fx(input_dir: Path) -> pd.DataFrame:
    path = input_dir / SOURCE_FILES["fx"]
    frame = _load_source(
        path, {"observation_date", "usd_inr", "fx_published_on", "source_url"}
    )
    _parse_date_column(frame, "observation_date", path)
    _parse_date_column(frame, "fx_published_on", path)
    _assert_unique(frame, "observation_date", path)
    _numeric_column(frame, "usd_inr", path, required=True, positive=True)
    frame["source_url"] = frame["source_url"].astype(str).str.strip()
    return frame.sort_values("observation_date").reset_index(drop=True)


def load_cpi(input_dir: Path) -> pd.DataFrame:
    path = input_dir / SOURCE_FILES["cpi"]
    frame = _load_source(
        path, {"month_start", "cpi_index", "cpi_published_on", "source_url"}
    )
    _parse_date_column(frame, "month_start", path)
    _parse_date_column(frame, "cpi_published_on", path)
    _assert_unique(frame, "month_start", path)
    if not frame["month_start"].dt.day.eq(1).all():
        raise DataQualityError(f"{path}: month_start must be the first day of each month.")
    _numeric_column(frame, "cpi_index", path, required=True, positive=True)
    _numeric_column(
        frame, "cpi_inflation_yoy_pct", path, required=False
    )
    frame["source_url"] = frame["source_url"].astype(str).str.strip()
    return frame.sort_values("month_start").reset_index(drop=True)


def latest_available(
    frame: pd.DataFrame,
    *,
    period_column: str,
    release_column: str,
    cutoff: pd.Timestamp,
    target_quarter_start: pd.Timestamp,
) -> pd.Series | None:
    """Return most recent period strictly before target and published by cutoff."""
    eligible = frame.loc[
        (frame[period_column] < target_quarter_start)
        & (frame[release_column] <= cutoff)
    ]
    if eligible.empty:
        return None
    return eligible.sort_values([period_column, release_column]).iloc[-1]


def _value(record: pd.Series | None, column: str) -> Any:
    if record is None or column not in record.index:
        return np.nan
    value = record[column]
    return np.nan if pd.isna(value) else value


def build_master_dataset(input_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build one target-quarter row, as of the day before that quarter begins."""
    financials = load_financials(input_dir)
    operations = load_operations(input_dir)
    atf = load_atf(input_dir)
    fx = load_fx(input_dir)
    cpi = load_cpi(input_dir)

    rows: list[dict[str, Any]] = []

    for _, target in financials.iterrows():
        target_start = pd.Timestamp(target["quarter_start"]).normalize()
        target_end = pd.Timestamp(target["quarter_end"]).normalize()
        cutoff = target_start - pd.Timedelta(days=1)

        # Outcome must not have been public on or before the simulated forecast cutoff.
        if pd.Timestamp(target["financial_published_on"]) <= cutoff:
            raise DataQualityError(
                f"Target outcome {target['fiscal_quarter']} was marked published by "
                f"forecast cutoff {cutoff.date()}. Check publication dates and target-quarter alignment."
            )

        prior_fin = latest_available(
            financials,
            period_column="quarter_end",
            release_column="financial_published_on",
            cutoff=cutoff,
            target_quarter_start=target_start,
        )
        prior_ops = latest_available(
            operations,
            period_column="month_start",
            release_column="operational_published_on",
            cutoff=cutoff,
            target_quarter_start=target_start,
        )
        prior_atf = latest_available(
            atf,
            period_column="month_start",
            release_column="atf_published_on",
            cutoff=cutoff,
            target_quarter_start=target_start,
        )
        prior_fx = latest_available(
            fx,
            period_column="observation_date",
            release_column="fx_published_on",
            cutoff=cutoff,
            target_quarter_start=target_start,
        )
        prior_cpi = latest_available(
            cpi,
            period_column="month_start",
            release_column="cpi_published_on",
            cutoff=cutoff,
            target_quarter_start=target_start,
        )

        row: dict[str, Any] = {
            "forecast_as_of_date": cutoff,
            "target_quarter": target["fiscal_quarter"],
            "target_quarter_start": target_start,
            "target_quarter_end": target_end,
            "latest_reported_fiscal_quarter": _value(prior_fin, "fiscal_quarter"),
            "latest_reported_financial_quarter_end": _value(prior_fin, "quarter_end"),
            "latest_reported_financial_published_on": _value(prior_fin, "financial_published_on"),
            "latest_reported_revenue_inr_mn": _value(prior_fin, "revenue_inr_mn"),
            "latest_reported_pat_inr_mn": _value(prior_fin, "pat_inr_mn"),
            "latest_reported_pat_margin_pct": _value(prior_fin, "pat_margin_pct"),
            "latest_reported_ebitdar_inr_mn": _value(prior_fin, "ebitdar_inr_mn"),
            "latest_financial_source_url": _value(prior_fin, "source_url"),
            "latest_operational_month": _value(prior_ops, "month_start"),
            "latest_operational_published_on": _value(prior_ops, "operational_published_on"),
            "latest_passengers_carried": _value(prior_ops, "passengers_carried"),
            "latest_passenger_load_factor_pct": _value(prior_ops, "passenger_load_factor_pct"),
            "latest_operational_source_url": _value(prior_ops, "source_url"),
            "latest_atf_month": _value(prior_atf, "month_start"),
            "latest_atf_published_on": _value(prior_atf, "atf_published_on"),
            "latest_atf_price_inr_per_kl": _value(prior_atf, "atf_price_inr_per_kl"),
            "latest_atf_source_url": _value(prior_atf, "source_url"),
            "latest_fx_observation_date": _value(prior_fx, "observation_date"),
            "latest_fx_published_on": _value(prior_fx, "fx_published_on"),
            "latest_usd_inr": _value(prior_fx, "usd_inr"),
            "latest_fx_source_url": _value(prior_fx, "source_url"),
            "latest_cpi_month": _value(prior_cpi, "month_start"),
            "latest_cpi_published_on": _value(prior_cpi, "cpi_published_on"),
            "latest_cpi_index": _value(prior_cpi, "cpi_index"),
            "latest_cpi_inflation_yoy_pct": _value(prior_cpi, "cpi_inflation_yoy_pct"),
            "latest_cpi_source_url": _value(prior_cpi, "source_url"),
            # Outcome values are appended only as labels and never passed to the predictor list.
            "target_revenue_inr_mn": target["revenue_inr_mn"],
            "target_pat_inr_mn": target["pat_inr_mn"],
            "target_pat_margin_pct": target["pat_margin_pct"],
            "target_financial_published_on": target["financial_published_on"],
            "target_financial_source_url": target["source_url"],
        }
        rows.append(row)

    master = pd.DataFrame(rows)
    if master.empty:
        raise DataQualityError("No target-quarter rows were created.")

    master = master.sort_values("target_quarter_start").reset_index(drop=True)
    leakage_report = audit_no_leakage(master)
    if int(leakage_report.loc[leakage_report["metric"] == "leakage_violations", "value"].iloc[0]) != 0:
        raise DataQualityError("Point-in-time leakage checks failed. Review data source timestamps.")

    report_rows: list[dict[str, Any]] = [
        {"metric": "financial_source_rows", "value": len(financials), "notes": SOURCE_FILES["financials"]},
        {"metric": "operational_source_rows", "value": len(operations), "notes": SOURCE_FILES["operations"]},
        {"metric": "atf_source_rows", "value": len(atf), "notes": SOURCE_FILES["atf"]},
        {"metric": "fx_source_rows", "value": len(fx), "notes": SOURCE_FILES["fx"]},
        {"metric": "cpi_source_rows", "value": len(cpi), "notes": SOURCE_FILES["cpi"]},
        {"metric": "master_dataset_rows", "value": len(master), "notes": "One row per target fiscal quarter"},
        {"metric": "target_label_rows", "value": int(master["target_pat_margin_pct"].notna().sum()), "notes": "PAT margin labels available"},
        {"metric": "leakage_violations", "value": 0, "notes": "Publication timestamps and source periods audited"},
    ]
    for col in OUTPUT_FEATURE_COLUMNS:
        report_rows.append(
            {
                "metric": f"missing_{col}",
                "value": int(master[col].isna().sum()),
                "notes": f"{master[col].isna().mean():.1%} missing",
            }
        )
    report_rows.append(
        {
            "metric": "rows_with_all_candidate_features",
            "value": int(master[OUTPUT_FEATURE_COLUMNS].notna().all(axis=1).sum()),
            "notes": "Diagnostic only; do not automatically drop rows or impute outside training folds",
        }
    )
    report = pd.DataFrame(report_rows)
    return master, report


def audit_no_leakage(master: pd.DataFrame) -> pd.DataFrame:
    """Confirm predictors were available by cutoff and source periods predate target."""
    publication_pairs = [
        ("latest_reported_financial_published_on", "latest_reported_financial_quarter_end"),
        ("latest_operational_published_on", "latest_operational_month"),
        ("latest_atf_published_on", "latest_atf_month"),
        ("latest_fx_published_on", "latest_fx_observation_date"),
        ("latest_cpi_published_on", "latest_cpi_month"),
    ]
    violations = 0
    for published_col, period_col in publication_pairs:
        has_value = master[published_col].notna()
        published = pd.to_datetime(master.loc[has_value, published_col])
        cutoff = pd.to_datetime(master.loc[has_value, "forecast_as_of_date"])
        violations += int((published > cutoff).sum())

        has_period = master[period_col].notna()
        period = pd.to_datetime(master.loc[has_period, period_col])
        target_start = pd.to_datetime(master.loc[has_period, "target_quarter_start"])
        violations += int((period >= target_start).sum())

    # Target label release date must be after the as-of cutoff.
    target_published = pd.to_datetime(master["target_financial_published_on"])
    cutoff = pd.to_datetime(master["forecast_as_of_date"])
    violations += int((target_published <= cutoff).sum())
    return pd.DataFrame(
        [
            {
                "metric": "leakage_violations",
                "value": violations,
                "notes": "Must equal zero: source publication <= cutoff, source period before target, target label published after cutoff",
            }
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build the point-in-time next-quarter PAT-margin master dataset."
    )
    parser.add_argument("--input-dir", type=Path, default=Path("data/raw"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/processed"))
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    master, report = build_master_dataset(args.input_dir)
    dataset_path = args.output_dir / "master_dataset.csv"
    report_path = args.output_dir / "data_quality_report.csv"
    master.to_csv(dataset_path, index=False, date_format="%Y-%m-%d")
    report.to_csv(report_path, index=False)
    print(f"Created {dataset_path} ({len(master)} target-quarter rows)")
    print(f"Created {report_path}")
    print("Read the data-quality report before starting EDA or modelling.")


if __name__ == "__main__":
    main()
