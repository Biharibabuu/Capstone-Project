"""Small SQLite cache for normalized market observations."""
from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def database_path() -> Path:
    configured = os.getenv("MARKET_DATA_DB")
    path = Path(configured).expanduser() if configured else ROOT / "data" / "processed" / "market_data.sqlite3"
    if not path.is_absolute():
        path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _connect() -> sqlite3.Connection:
    connection = sqlite3.connect(database_path())
    connection.row_factory = sqlite3.Row
    connection.execute("""
        CREATE TABLE IF NOT EXISTS market_observations (
            source TEXT NOT NULL,
            observed_at TEXT NOT NULL,
            value REAL NOT NULL,
            unit TEXT NOT NULL,
            currency TEXT,
            fetched_at TEXT NOT NULL,
            provider TEXT NOT NULL,
            metadata_json TEXT NOT NULL DEFAULT '{}',
            PRIMARY KEY (source, observed_at)
        )
    """)
    connection.commit()
    return connection


def save_observation(observation: dict[str, Any]) -> None:
    metadata = {
        key: value for key, value in observation.items()
        if key not in {"source", "observed_at", "value", "unit", "currency", "fetched_at", "provider"}
    }
    with _connect() as connection:
        connection.execute("""
            INSERT OR REPLACE INTO market_observations
            (source, observed_at, value, unit, currency, fetched_at, provider, metadata_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            observation["source"], observation["observed_at"], observation["value"],
            observation["unit"], observation.get("currency"), observation["fetched_at"],
            observation["provider"], json.dumps(metadata, ensure_ascii=False),
        ))
        connection.commit()


def latest_observations() -> list[dict[str, Any]]:
    with _connect() as connection:
        rows = connection.execute("""
            SELECT m.* FROM market_observations m
            JOIN (
                SELECT source, MAX(observed_at) AS latest_time
                FROM market_observations GROUP BY source
            ) x ON x.source = m.source AND x.latest_time = m.observed_at
            ORDER BY m.source
        """).fetchall()
    result = []
    for row in rows:
        item = dict(row)
        metadata = json.loads(item.pop("metadata_json") or "{}")
        result.append({**item, **metadata})
    return result
