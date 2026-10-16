"""Initial API routes. Forecasts stay disabled until a trained model is reviewed."""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException, Request, status

from backend.schemas import HealthResponse, PredictionRequest

router = APIRouter(prefix="/api", tags=["forecasting"])

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = REPOSITORY_ROOT / "models" / "selected_model.joblib"


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    model_loaded = MODEL_PATH.is_file()
    return HealthResponse(
        status="ready" if model_loaded else "model_not_trained",
        model_loaded=model_loaded,
        message=(
            "A model artifact is present; loading and compatibility checks are still required."
            if model_loaded
            else "The forecast endpoint is not enabled: complete the data audit, evaluation and model packaging first."
        ),
    )


@router.post("/predict")
def predict(payload: PredictionRequest, request: Request):
    """Fail safely rather than returning a made-up prediction."""
    model_service = getattr(request.app.state, "model_service", None)
    if model_service is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "No validated forecasting model is loaded. Complete D2/D3, compare candidate models "
                "against the baseline, and register a reproducible model before enabling prediction."
            ),
        )
    # Prediction implementation is intentionally deferred until the feature set is validated.
    return model_service.predict(payload)
