"""FastAPI routes for forecasting readiness and external data refresh."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request, status

from backend.schemas import HealthResponse, PredictionRequest
from src.connectors.registry import get_source_catalogue
from src.market_refresh import get_market_snapshot, refresh_market_data

router = APIRouter(prefix="/api", tags=["forecasting and data"])


@router.get("/health", response_model=HealthResponse)
def health(request: Request) -> HealthResponse:
    model_service = getattr(request.app.state, "model_service", None)
    model_loaded = model_service is not None
    return HealthResponse(
        status="ready" if model_loaded else "model_not_trained",
        model_loaded=model_loaded,
        message=(
            "A prediction service is registered. Confirm its model version and evaluation metadata."
            if model_loaded
            else "Market-data refresh is available independently. Forecasts remain disabled until a model is trained and evaluated."
        ),
    )


@router.get("/sources")
def sources() -> dict:
    """Return source cadence and ingestion method without exposing secret values."""
    return {"sources": get_source_catalogue()}


@router.get("/market/latest")
def market_latest() -> dict:
    """Return the latest successfully stored market observations and source status."""
    return get_market_snapshot()


@router.post("/market/refresh")
def market_refresh() -> dict:
    """Refresh USD/INR and Brent; report each connector result separately."""
    return refresh_market_data()


@router.post("/predict")
def predict(payload: PredictionRequest, request: Request):
    """Fail safely rather than returning a made-up prediction."""
    model_service = getattr(request.app.state, "model_service", None)
    if model_service is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "No validated forecasting model is loaded. Complete chronological model comparison, "
                "evaluation and model packaging before enabling prediction."
            ),
        )
    return model_service.predict(payload)
