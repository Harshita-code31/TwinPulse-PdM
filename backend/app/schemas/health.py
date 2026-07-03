from pydantic import BaseModel


class HealthResponse(BaseModel):
    machine_id: int
    health_score: float
    status: str