"""Initial API routes. Forecasts stay disabled until a trained model is reviewed."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request, status

from backend.schemas import HealthResponse, PredictionRequest

router = APIRouter(prefix="/api", tags=["forecasting"])


@router.get("/health", response_model=HealthResponse)
def health(request: Request) -> HealthResponse:
    # A model is "loaded" only when the validated prediction service has been
    # registered at runtime. A file existing on disk does not make it ready.
    model_service = getattr(request.app.state, "model_service", None)
    model_loaded = model_service is not None
    return HealthResponse(
        status="ready" if model_loaded else "model_not_trained",
        model_loaded=model_loaded,
        message=(
            "A prediction service is registered. Confirm its model version and evaluation metadata."
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
    # The final feature set and inference contract will be fixed after D2/D3.
    return model_service.predict(payload)
