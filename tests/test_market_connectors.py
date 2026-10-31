from __future__ import annotations

from unittest.mock import patch

import pytest

from src.connectors.common import ConnectorError
from src.connectors.fx_client import fetch_usd_inr
from src.connectors.brent_client import fetch_brent


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def test_fx_connector_normalizes_alpha_vantage_response():
    payload = {"Realtime Currency Exchange Rate": {
        "5. Exchange Rate": "83.25",
        "6. Last Refreshed": "2026-10-30 16:00:00",
        "7. Time Zone": "UTC",
    }}
    with patch("src.connectors.common.requests.get", return_value=FakeResponse(payload)):
        row = fetch_usd_inr("test-key")
    assert row["value"] == 83.25
    assert row["unit"] == "INR per USD"
    assert row["source"] == "alpha_vantage_usd_inr"


def test_brent_connector_normalizes_oilpriceapi_response():
    payload = {"status": "success", "data": {
        "price": 80.5, "currency": "USD", "unit": "barrel",
        "code": "BRENT_CRUDE_USD", "timestamp": "2026-10-30T10:00:00Z",
    }}
    with patch("src.connectors.common.requests.get", return_value=FakeResponse(payload)):
        row = fetch_brent("test-key")
    assert row["value"] == 80.5
    assert row["currency"] == "USD"
    assert row["source"] == "oilpriceapi_brent"


def test_connector_requires_api_key(monkeypatch):
    monkeypatch.delenv("ALPHAVANTAGE_API_KEY", raising=False)
    with pytest.raises(ConnectorError, match="not configured"):
        fetch_usd_inr()
