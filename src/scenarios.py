"""Scenario-analysis helpers.

Scenario assumptions must be visible to the user and grounded in the data/model. This
module does not invent numeric shocks or imply causal effects.
"""
from __future__ import annotations

from typing import Literal

ScenarioName = Literal[
    "low_cost_favourable",
    "base",
    "high_cost_adverse",
]


def validate_scenario_name(name: str) -> ScenarioName:
    allowed = {
        "low_cost_favourable",
        "base",
        "high_cost_adverse",
    }
    if name not in allowed:
        raise ValueError(f"scenario must be one of: {', '.join(sorted(allowed))}")
    return name  # type: ignore[return-value]


def apply_scenario(inputs: dict[str, float], overrides: dict[str, float]) -> dict[str, float]:
    """Apply explicit user-supplied overrides; does not choose shock magnitudes."""
    merged = dict(inputs)
    for name, value in overrides.items():
        if not name.strip():
            raise ValueError("Override names cannot be blank.")
        if not isinstance(value, (int, float)):
            raise ValueError(f"Override for '{name}' must be numeric.")
        merged[name] = float(value)
    return merged
