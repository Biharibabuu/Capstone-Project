"""Shared helpers for external data connectors."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import requests
from dotenv import load_dotenv

# Load local development secrets from .env when present. Hosted environments
# should inject the same variables through their secret manager.
load_dotenv()


class ConnectorError(RuntimeError):
    """Raised when a provider response cannot be safely interpreted."""


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_provider_time(value: Any) -> str:
    """Normalize an ISO-like provider timestamp to an ISO-8601 string."""
    if not value:
        return utc_now_iso()
    text = str(value).strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        # Alpha Vantage FX returns e.g. 2026-10-31 10:45:00.
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                parsed = datetime.strptime(str(value).strip(), fmt)
                break
            except ValueError:
                continue
        else:
            raise ConnectorError(f"Unrecognised provider timestamp: {value!r}")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat()


def get_json(url: str, *, params: dict[str, str] | None = None,
             headers: dict[str, str] | None = None, timeout: int = 15) -> dict[str, Any]:
    """GET JSON with a timeout and provider-friendly error messages."""
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        raise ConnectorError(f"Provider request failed: {exc}") from exc
    except ValueError as exc:
        raise ConnectorError("Provider did not return valid JSON.") from exc
    if not isinstance(payload, dict):
        raise ConnectorError("Provider returned an unexpected JSON structure.")
    return payload


def finite_number(value: Any, label: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ConnectorError(f"Provider field {label!r} is not numeric.") from exc
    if number != number or number in (float("inf"), float("-inf")):
        raise ConnectorError(f"Provider field {label!r} is not finite.")
    return number
