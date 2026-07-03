from fastapi import FastAPI

from app.api.machine import router as machine_router
from app.config.settings import get_settings
from app.database.db import initialize_database
from app.api.sensor import router as sensor_router
from app.api.prediction import router as prediction_router
from app.api.health import router as health_router
from app.api.history import router as history_router
from app.api.alerts import router as alerts_router

settings = get_settings()


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
    )

    # Initialize database
    initialize_database()

    # Register API routers
    app.include_router(machine_router)
    app.include_router(sensor_router)
    app.include_router(prediction_router)
    app.include_router(health_router)
    app.include_router(history_router)
    app.include_router(alerts_router)

    return app


app = create_application()


@app.get("/")
def home():
    return {
        "message": "Predictive Maintenance Backend Running"
    }