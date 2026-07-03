from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_database_session
from app.schemas.sensor import SensorResponse
from app.services.sensor_service import (
    get_machine_sensor_history,
    get_sensor_history,
)

router = APIRouter(
    prefix="/sensor-data",
    tags=["Sensor Data"],
)


@router.get("/", response_model=list[SensorResponse])
def read_all_sensor_data(
    db: Session = Depends(get_database_session),
):
    return get_sensor_history(db)


@router.get("/{machine_id}", response_model=list[SensorResponse])
def read_machine_sensor_data(
    machine_id: int,
    db: Session = Depends(get_database_session),
):
    return get_machine_sensor_history(db, machine_id)