"""India CPI connector using the official MoSPI eSankhyiki API."""
from __future__ import annotations

from datetime import datetime
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

API_PATH_2012 = "/api/cpi/getCPIIndex"
API_PATH_2024 = "/api/cpi/getCPIData"


def normalize_cpi_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Select the latest All-India General CPI inflation observation.

    Prefer the published year-on-year inflation field. If the API supplies only
    index values, calculate the year-on-year change from the same base-year series.
    """
    rows = extract_records(payload)
    if not rows:
        raise ConnectorError("MoSPI CPI response contained no data rows.")

    selected: list[tuple[Any, str, dict[str, Any]]] = []
    for row in rows:
        text = all_rows_text(row)
        state = row_value(row, ("state", "state_name", "state_ut", "state_name_label"))
        if state is not None and str(state).strip().lower() not in {"all india", "india", "99"}:
            continue

        group = row_value(row, ("group", "group_name", "group_description", "groupname"))
        subgroup = row_value(row, ("subgroup", "sub_group", "subgroup_name"))
        sector = row_value(row, ("sector", "sector_name"))
        if group is not None and "general" not in str(group).lower():
            continue
        if subgroup is not None and not any(term in str(subgroup).lower() for term in ("general", "overall")):
            continue
        if sector is not None and "combined" not in str(sector).lower():
            continue
        if group is None and subgroup is None and "general" not in text:
            continue

        period = month_end_from_row(row)
        if period is not None:
            selected.append((period[0], period[1], row))

    if not selected:
        raise ConnectorError(
            "No All-India General Combined CPI rows were found. Check MoSPI base-year/filter definitions."
        )

    selected.sort(key=lambda item: item[0])
    latest_date, latest_period, latest_row = selected[-1]
    inflation = numeric_field(
        latest_row,
        ("inflation", "inflation_rate", "yoy_inflation", "annual_inflation", "year_on_year_inflation"),
    )

    if inflation is None:
        index_value = numeric_field(latest_row, ("index", "cpi_index", "index_value", "price_index"))
        if index_value is None:
            raise ConnectorError("MoSPI CPI row has neither an inflation field nor a usable index field.")
        prior = next(
            (
                row for observation_date, _, row in reversed(selected[:-1])
                if observation_date.year == latest_date.year - 1
                and observation_date.month == latest_date.month
            ),
            None,
        )
        prior_index = numeric_field(prior, ("index", "cpi_index", "index_value", "price_index")) if prior else None
        if prior_index is None or prior_index == 0:
            raise ConnectorError("CPI index is available, but the matching prior-year month is missing.")
        inflation = (index_value / prior_index - 1.0) * 100.0

    return {
        "source": "mospi_cpi",
        "display_name": "India CPI inflation",
        "value": finite_number(inflation, "CPI inflation"),
        "unit": "% year-on-year",
        "currency": None,
        "observed_at": latest_date.isoformat(),
        "fetched_at": utc_now_iso(),
        "provider": "MoSPI eSankhyiki",
        "reference_period": latest_period,
        "publication_date": find_publication_date(latest_row),
        "base_year": row_value(latest_row, ("baseyear", "base_year")) or "2024",
        "series": "All-India General, Combined",
        "metric": "year-on-year inflation",
    }


def fetch_cpi() -> dict[str, Any]:
    """Fetch recent CPI rows from the official monthly API."""
    years = get_year_window()
    base_year = "2024"
    params = {
        "base_year": base_year,
        "series": "Current",
        "year": years,
        "Format": "JSON",
        "limit": "2000",
        "page": "1",
    }
    payload = fetch_mospi_json(API_PATH_2024, params)
    return normalize_cpi_payload(payload)
