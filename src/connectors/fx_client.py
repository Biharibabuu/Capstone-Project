"""USD/INR spot-rate connector using Alpha Vantage's FX endpoint."""
from __future__ import annotations

import os
from typing import Any

from src.connectors.common import ConnectorError, finite_number, get_json, parse_provider_time, utc_now_iso

API_URL = "https://www.alphavantage.co/query"


def fetch_usd_inr(api_key: str | None = None) -> dict[str, Any]:
    key = api_key or os.getenv("ALPHAVANTAGE_API_KEY")
    if not key:
        raise ConnectorError("ALPHAVANTAGE_API_KEY is not configured.")

    payload = get_json(API_URL, params={
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "USD",
        "to_currency": "INR",
        "apikey": key,
    })
    if "Error Message" in payload:
        raise ConnectorError(str(payload["Error Message"]))
    if "Note" in payload or "Information" in payload:
        raise ConnectorError(str(payload.get("Note") or payload.get("Information")))

    quote = payload.get("Realtime Currency Exchange Rate")
    if not isinstance(quote, dict):
        raise ConnectorError("Alpha Vantage response did not contain the expected FX quote.")

    return {
        "source": "alpha_vantage_usd_inr",
        "display_name": "USD/INR exchange rate",
        "value": finite_number(quote.get("5. Exchange Rate"), "5. Exchange Rate"),
        "unit": "INR per USD",
        "currency": "INR",
        "observed_at": parse_provider_time(quote.get("6. Last Refreshed")),
        "fetched_at": utc_now_iso(),
        "provider": "Alpha Vantage",
        "provider_timezone": quote.get("7. Time Zone"),
    }
