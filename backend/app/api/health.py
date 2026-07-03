from fastapi import APIRouter

from app.schemas.health import HealthResponse
from app.services.health_service import get_machine_health

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/{machine_id}", response_model=HealthResponse)
def read_health(machine_id: int):
    return get_machine_health(machine_id)