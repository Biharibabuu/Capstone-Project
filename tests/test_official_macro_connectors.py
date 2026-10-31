"""Tests for official monthly CPI/WPI data normalisation."""
from src.connectors.cpi_client import normalize_cpi_payload
from src.connectors.wpi_client import normalize_wpi_payload


def test_cpi_uses_latest_all_india_general_combined_inflation():
    payload = {
        "data": [
            {
                "year": 2026, "month": "July", "state": "All India",
                "sector": "Combined", "group": "General",
                "subgroup": "General-Overall", "inflation": "5.10",
            },
            {
                "year": 2026, "month": "August", "state": "All India",
                "sector": "Combined", "group": "General",
                "subgroup": "General-Overall", "inflation": "5.30",
            },
            {
                "year": 2026, "month": "August", "state": "All India",
                "sector": "Rural", "group": "General",
                "subgroup": "General-Overall", "inflation": "5.90",
            },
            {
                "year": 2026, "month": "August", "state": "All India",
                "sector": "Combined", "group": "Food", "inflation": "6.80",
            },
        ]
    }
    result = normalize_cpi_payload(payload)
    assert result["value"] == 5.30
    assert result["reference_period"] == "2026-08"
    assert result["series"] == "All-India General, Combined"


def test_wpi_calculates_yoy_from_all_commodities_index():
    payload = {
        "data": [
            {
                "year": 2025, "month": "August",
                "commodity": "All Commodities", "index": "125.0",
            },
            {
                "year": 2026, "month": "August",
                "commodity": "All Commodities", "index": "130.0",
            },
            {
                "year": 2026, "month": "August",
                "commodity": "Food Articles", "index": "140.0",
            },
        ]
    }
    result = normalize_wpi_payload(payload)
    assert result["value"] == 4.0
    assert result["reference_period"] == "2026-08"
    assert result["series"] == "All Commodities"
