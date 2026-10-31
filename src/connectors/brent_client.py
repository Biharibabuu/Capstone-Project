"""Brent crude connector using OilPriceAPI's latest-price endpoint."""
from __future__ import annotations

import os
from typing import Any

from src.connectors.common import ConnectorError, finite_number, get_json, parse_provider_time, utc_now_iso

API_URL = "https://api.oilpriceapi.com/v1/prices/latest"


def fetch_brent(api_key: str | None = None) -> dict[str, Any]:
    key = api_key or os.getenv("OILPRICEAPI_KEY")
    if not key:
        raise ConnectorError("OILPRICEAPI_KEY is not configured.")

    payload = get_json(
        API_URL,
        params={"by_code": "BRENT_CRUDE_USD"},
        headers={"Authorization": f"Token {key}", "Accept": "application/json"},
    )
    if payload.get("status") == "error":
        raise ConnectorError(str(payload.get("error") or payload.get("message") or "OilPriceAPI returned an error."))
    quote = payload.get("data")
    if not isinstance(quote, dict):
        raise ConnectorError("OilPriceAPI response did not contain a price object.")
    if quote.get("code") not in (None, "BRENT_CRUDE_USD"):
        raise ConnectorError(f"Unexpected commodity code: {quote.get('code')!r}")

    observed = quote.get("timestamp") or quote.get("updated_at") or quote.get("created_at")
    return {
        "source": "oilpriceapi_brent",
        "display_name": "Brent crude benchmark",
        "value": finite_number(quote.get("price"), "price"),
        "unit": quote.get("unit") or "barrel",
        "currency": quote.get("currency") or "USD",
        "observed_at": parse_provider_time(observed),
        "fetched_at": utc_now_iso(),
        "provider": "OilPriceAPI",
        "commodity_code": quote.get("code") or "BRENT_CRUDE_USD",
    }
