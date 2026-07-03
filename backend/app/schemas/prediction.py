from pydantic import BaseModel


class PredictionResponse(BaseModel):
    machine_id: int
    health_score: float
    failure_probability: float
    remaining_life_days: float
    predicted_fault: str