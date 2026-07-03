from datetime import datetime

from pydantic import BaseModel


class HistoryResponse(BaseModel):
    timestamp: datetime
    temperature: float
    rpm: int
    torque: float
    vibration: float
    current: float
    oil_level: float

    class Config:
        from_attributes = True