"""Shared helpers for the official MoSPI CPI and WPI APIs."""
from __future__ import annotations

import os
from datetime import date, datetime
from calendar import monthrange
from typing import Any

from src.connectors.common import ConnectorError, get_json


API_BASE = os.getenv("MOSPI_API_BASE_URL", "https://api.mospi.gov.in").rstrip("/")


def fetch_mospi_json(path: str, params: dict[str, str]) -> dict[str, Any]:
    """Fetch an official MoSPI API response, optionally using a Bearer token.

    The eSankhyiki API specifications describe Bearer authentication. Some API
    clients may be able to access open endpoints without a token, so the token is
    optional here. If the portal returns 401/403, configure MOSPI_API_TOKEN.
    """
    headers = {"Accept": "application/json"}
    token = os.getenv("MOSPI_API_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"

    payload = get_json(
        f"{API_BASE}{path}",
        params=params,
        headers=headers,
        timeout=30,
    )
    if payload.get("statusCode") is False or payload.get("status") == "error" or payload.get("error"):
        detail = payload.get("message") or payload.get("error") or "MoSPI returned an unsuccessful response."
        raise ConnectorError(str(detail))
    return payload


def extract_records(payload: Any) -> list[dict[str, Any]]:
    """Extract data rows from the portal's JSON response shapes."""
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        if payload.get("statusCode") is False or payload.get("status") == "error":
            raise ConnectorError(str(payload.get("message") or "MoSPI API reported an error."))
        preferred = ("data", "records", "result", "items", "rows")
        for key in preferred:
            if key in payload:
                found = extract_records(payload[key])
                if found:
                    return found
        for value in payload.values():
            if isinstance(value, (dict, list)):
                found = extract_records(value)
                if found:
                    return found
    return []


def _normalise_key(value: Any) -> str:
    return "".join(ch for ch in str(value).lower() if ch.isalnum())


def row_value(row: dict[str, Any], candidates: tuple[str, ...]) -> Any:
    """Return the first non-empty field matching one of the candidate names."""
    normalised = {_normalise_key(key): value for key, value in row.items()}
    for candidate in candidates:
        key = _normalise_key(candidate)
        if key in normalised and normalised[key] not in (None, ""):
            return normalised[key]
    return None


def numeric_field(row: dict[str, Any], candidates: tuple[str, ...]) -> float | None:
    for key in candidates:
        value = row_value(row, (key,))
        if value is None:
            continue
        try:
            number = float(str(value).replace(",", "").replace("%", "").strip())
        except (TypeError, ValueError):
            continue
        if number == number and number not in (float("inf"), float("-inf")):
            return number
    return None


def month_end_from_row(row: dict[str, Any]) -> tuple[date, str] | None:
    """Read an observation month from common MoSPI field names."""
    period = row_value(row, ("reference_period", "period", "month_year", "date", "monthyear"))
    if period is not None:
        raw = str(period).strip()
        for fmt in (
            "%Y-%m-%d", "%Y-%m", "%b %Y", "%B %Y", "%b-%Y",
            "%B-%Y", "%b-%y", "%m-%Y", "%Y/%m",
        ):
            try:
                parsed = datetime.strptime(raw, fmt).date()
                last = date(parsed.year, parsed.month, monthrange(parsed.year, parsed.month)[1])
                return last, f"{parsed.year:04d}-{parsed.month:02d}"
            except ValueError:
                pass

    year_value = row_value(row, ("year", "year_code", "calendar_year"))
    month_value = row_value(row, ("month_code", "month", "month_name"))
    if year_value is None or month_value is None:
        return None
    try:
        year = int(str(year_value).strip()[:4])
    except ValueError:
        return None

    month_text = str(month_value).strip()
    try:
        month = int(month_text)
    except ValueError:
        month = 0
        for fmt in ("%B", "%b"):
            try:
                month = datetime.strptime(month_text.title(), fmt).month
                break
            except ValueError:
                continue
    if not 1 <= month <= 12:
        return None
    last = date(year, month, monthrange(year, month)[1])
    return last, f"{year:04d}-{month:02d}"


def find_publication_date(row: dict[str, Any]) -> str | None:
    value = row_value(row, ("release_date", "released_on", "publication_date", "published_at", "releaseDate"))
    if value is None:
        return None
    raw = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(raw[:19], fmt).date().isoformat()
        except ValueError:
            continue
    return raw


def all_rows_text(row: dict[str, Any]) -> str:
    return " ".join(str(value).lower() for value in row.values() if value is not None)


def get_year_window() -> str:
    """Return two calendar years to support year-on-year change calculations."""
    current_year = datetime.utcnow().year
    return f"{current_year - 1},{current_year}"
