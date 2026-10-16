"""Request/response schemas for the IndiGo forecasting API."""
from __future__ import annotations

import math
from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class PredictionRequest(BaseModel):
    """Generic inputs until D2/D3 finalise the feature list."""

    as_of_date: date = Field(
        description="Date the forecast is made; all supplied inputs must be available by this date."
    )
    inputs: dict[str, float] = Field(
        description="Named numeric inputs accepted by the final trained feature pipeline."
    )
    scenario: Literal[
        "low_cost_favourable",
        "base",
        "high_cost_adverse",
    ] = "base"

    @field_validator("inputs")
    @classmethod
    def inputs_must_be_finite(cls, value: dict[str, float]) -> dict[str, float]:
        if not value:
            raise ValueError("At least one input value is required.")
        for name, number in value.items():
            if not name.strip():
                raise ValueError("Input names cannot be blank.")
            if not math.isfinite(number):
                raise ValueError(f"Input '{name}' must be finite.")
        return value


class HealthResponse(BaseModel):
    status: Literal["starting", "ready", "model_not_trained"]
    model_loaded: bool
    message: str


class PredictionResponse(BaseModel):
    forecast_horizon: str = "next_quarter"
    target: str = "pat_margin_pct"
    forecast_value: float
    unit: str = "percentage_points"
    model_version: str
    as_of_date: date
    scenario: str
    limitations: list[str]
