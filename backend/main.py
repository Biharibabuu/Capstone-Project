"""FastAPI application entrypoint for the IndiGo Profitability Intelligence System."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import router

app = FastAPI(
    title="IndiGo Profitability Intelligence API",
    version="0.1.0",
    description=(
        "Academic prototype API for next-quarter IndiGo PAT-margin forecasting. "
        "Forecasts remain disabled until a model is trained and evaluated."
    ),
)

# Local-development origins only. Review origins before any hosted deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "project": "IndiGo Profitability Intelligence System",
        "status": "prototype_scaffold",
        "docs": "/docs",
        "health": "/api/health",
    }
