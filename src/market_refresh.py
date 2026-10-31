"""Refresh market feeds independently so one provider failure does not block another."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Callable

from src.connectors.common import ConnectorError, utc_now_iso
from src.connectors.fx_client import fetch_usd_inr
from src.connectors.brent_client import fetch_brent
from src.connectors.registry import get_source_catalogue
from src.market_store import latest_observations, save_observation

CONNECTORS: dict[str, Callable[[], dict[str, Any]]] = {
    "alpha_vantage_usd_inr": fetch_usd_inr,
    "oilpriceapi_brent": fetch_brent,
}


def _is_stale(observed_at: str, max_hours: int = 72) -> bool:
    parsed = datetime.fromisoformat(observed_at.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    age_hours = (datetime.now(timezone.utc) - parsed.astimezone(timezone.utc)).total_seconds() / 3600
    return age_hours > max_hours


def get_market_snapshot() -> dict[str, Any]:
    stored = latest_observations()
    records = []
    for item in stored:
        item["freshness"] = "stale" if _is_stale(item["observed_at"]) else "current"
        records.append(item)
    available = {item["source"] for item in records}
    catalogue = []
    for source in get_source_catalogue():
        source_copy = dict(source)
        if source["id"] in available:
            source_copy["connection_status"] = "data_available"
        elif source["mode"] == "api":
            source_copy["connection_status"] = "configured_or_not_yet_refreshed"
        else:
            source_copy["connection_status"] = "official_release_import"
        catalogue.append(source_copy)
    return {"as_of": utc_now_iso(), "market_data": records, "sources": catalogue}


def refresh_market_data() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    successes = 0
    for source_id, connector in CONNECTORS.items():
        try:
            observation = connector()
            save_observation(observation)
            results.append({"source": source_id, "status": "updated", "observed_at": observation["observed_at"]})
            successes += 1
        except ConnectorError as exc:
            message = str(exc)
            result_status = "not_configured" if "not configured" in message else "error"
            results.append({"source": source_id, "status": result_status, "message": message})
        except Exception as exc:  # Defensive boundary for provider/schema changes.
            results.append({"source": source_id, "status": "error", "message": f"Unexpected connector error: {exc}"})

    result_status = "success" if successes == len(CONNECTORS) else "partial_success" if successes else "not_configured"
    return {
        "status": result_status,
        "refreshed_at": utc_now_iso(),
        "results": results,
        "snapshot": get_market_snapshot(),
    }
