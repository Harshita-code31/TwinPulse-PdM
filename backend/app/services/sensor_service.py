from sqlalchemy.orm import Session

from app.database.repositories.sensor_repository import (
    get_all_sensor_data,
    get_sensor_data_by_machine,
)


def get_sensor_history(db: Session):
    return get_all_sensor_data(db)


def get_machine_sensor_history(db: Session, machine_id: int):
    return get_sensor_data_by_machine(db, machine_id)