from sqlalchemy.orm import Session

from app.database.repositories.sensor_repository import (
    get_sensor_data_by_machine,
)


def get_history(
    db: Session,
    machine_id: int,
):
    """
    Return historical sensor data for a machine.
    """

    return get_sensor_data_by_machine(
        db,
        machine_id,
    )