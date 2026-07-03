from sqlalchemy.orm import Session

from app.database.models.sensor import SensorData


def save_sensor_data(db: Session, data: dict) -> SensorData:

    sensor = SensorData(

        machine_id=data["machine_id"],

        machine_type=data["machine_type"],

        operating_hours=data["operating_hours"],

        machine_age=data["machine_age"],

        ambient_temperature=data["ambient_temperature"],

        operating_load=data["operating_load"],

        maintenance_count=data["maintenance_count"],

        fault_type=data["fault_type"],

        temperature=data["temperature"],

        rpm=data["rpm"],

        torque=data["torque"],

        vibration=data["vibration"],

        current=data["current"],

        oil_level=data["oil_level"]

    )

    db.add(sensor)

    db.commit()

    db.refresh(sensor)

    return sensor


def get_all_sensor_data(db: Session):

    return (
        db.query(SensorData)
        .order_by(SensorData.timestamp.desc())
        .all()
    )


def get_sensor_data_by_machine(
    db: Session,
    machine_id: int
):

    return (
        db.query(SensorData)
        .filter(SensorData.machine_id == machine_id)
        .order_by(SensorData.timestamp.desc())
        .all()
    )