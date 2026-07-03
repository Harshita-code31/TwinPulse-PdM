from datetime import date

from pydantic import BaseModel


class MachineCreate(BaseModel):
    machine_name: str
    machine_type: str
    location: str
    installation_date: date
    status: str


class MachineResponse(MachineCreate):
    machine_id: int

    class Config:
        from_attributes = True