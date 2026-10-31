"""India WPI connector using the official MoSPI eSankhyiki API."""
from __future__ import annotations

import os
from typing import Any

from src.connectors.common import ConnectorError, finite_number, utc_now_iso
from src.connectors.mospi_common import (
    all_rows_text,
    extract_records,
    fetch_mospi_json,
    find_publication_date,
    get_year_window,
    month_end_from_row,
    numeric_field,
    row_value,
)

API_PATH = "/api/wpi/getWpiRecords"
INDEX_FIELDS = ("wpi_index", "index", "index_value", "price_index", "wpi", "index_number")
INFLATION_FIELDS = (
    "inflation", "inflation_rate", "yoy_inflation", "annual_inflation",
    "year_on_year_inflation", "annual_change",
)


def normalize_wpi_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Select All Commodities WPI and calculate YoY change if only index values exist."""
    rows = extract_records(payload)
    if not rows:
        raise ConnectorError("MoSPI WPI response contained no data rows.")

    selected: list[tuple[Any, str, dict[str, Any]]] = []
    for row in rows:
        text = all_rows_text(row)
        # WPI's official hierarchy includes an aggregate All Commodities record.
        # Match explicit aggregate labels, never substitute a subgroup silently.
        if not any(label in text for label in ("all commodities", "all commodity")):
            continue
        period = month_end_from_row(row)
        if period is not None:
            selected.append((period[0], period[1], row))

    if not selected:
        raise ConnectorError(
            "No WPI 'All Commodities' aggregate rows were found. Check the selected base year and API filters."
        )

    selected.sort(key=lambda item: item[0])
    latest_date, latest_period, latest_row = selected[-1]
    inflation = numeric_field(latest_row, INFLATION_FIELDS)

    if inflation is None:
        index_value = numeric_field(latest_row, INDEX_FIELDS)
        if index_value is None:
            raise ConnectorError("MoSPI WPI row has neither an inflation field nor a usable index field.")
        prior = next(
            (
                row for observation_date, _, row in reversed(selected[:-1])
                if observation_date.year == latest_date.year - 1
                and observation_date.month == latest_date.month
            ),
            None,
        )
        prior_index = numeric_field(prior, INDEX_FIELDS) if prior else None
        if prior_index is None or prior_index == 0:
            raise ConnectorError("WPI index is available, but the matching prior-year month is missing.")
        inflation = (index_value / prior_index - 1.0) * 100.0

    return {
        "source": "mospi_wpi",
        "display_name": "India WPI inflation",
        "value": finite_number(inflation, "WPI inflation"),
        "unit": "% year-on-year",
        "currency": None,
        "observed_at": latest_date.isoformat(),
        "fetched_at": utc_now_iso(),
        "provider": "MoSPI eSankhyiki / Office of the Economic Adviser",
        "reference_period": latest_period,
        "publication_date": find_publication_date(latest_row),
        "base_year": row_value(latest_row, ("baseyear", "base_year")) or "2022-23",
        "series": "All Commodities",
        "metric": "year-on-year inflation",
    }


def fetch_wpi() -> dict[str, Any]:
    """Fetch two calendar years of monthly WPI rows for a YoY calculation."""
    years = get_year_window()
    base_year = os.getenv("MOSPI_WPI_BASE_YEAR", "2022-23").strip()
    params = {
        "base_year": base_year,
        "year": years,
        "month_code": "1,2,3,4,5,6,7,8,9,10,11,12",
        "Format": "JSON",
        "limit": "5000",
        "page": "1",
    }
    payload = fetch_mospi_json(API_PATH, params)
    return normalize_wpi_payload(payload)
