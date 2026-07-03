from datetime import datetime

from pydantic import BaseModel


class SensorResponse(BaseModel):
    sensor_id: int
    machine_id: int
    timestamp: datetime
    temperature: float
    rpm: int
    torque: float
    vibration: float
    current: float
    oil_level: float

    class Config:
        from_attributes = True