import pandas as pd
from sqlalchemy.orm import Session

from app.database.models.sensor import SensorData
from app.database.repositories.alert_repository import create_alert
from app.database.repositories.prediction_repository import save_prediction
from app.ml.predict import predict_machine_health


def predict_machine(db: Session, machine_id: int):

    readings = (
        db.query(SensorData)
        .filter(SensorData.machine_id == machine_id)
        .order_by(SensorData.timestamp.desc())
        .limit(20)
        .all()
    )

    if len(readings) < 20:
        raise ValueError("Not enough sensor readings for prediction.")

    readings.reverse()

    data = []

    for r in readings:

        data.append({

            "machine_type": r.machine_type,

            "operating_hours": r.operating_hours,

            "machine_age": r.machine_age,

            "ambient_temperature": r.ambient_temperature,

            "operating_load": r.operating_load,

            "temperature": r.temperature,

            "rpm": r.rpm,

            "torque": r.torque,

            "vibration": r.vibration,

            "current": r.current,

            "oil_level": r.oil_level,

            "maintenance_count": r.maintenance_count,

            "fault_type": r.fault_type

        })

    df = pd.DataFrame(data)
    print("Running prediction...")

    prediction = predict_machine_health(df)

    print("Prediction:", prediction)

    prediction["machine_id"] = machine_id
    prediction["predicted_fault"] = df.iloc[-1]["fault_type"]

    print("Saving prediction...")

    save_prediction(db, prediction)

    print("Prediction saved!")

    # Create alert based on health score
    health = prediction["health_score"]

    if health < 30:

        create_alert(
            db=db,
            machine_id=machine_id,
            severity="Critical",
            message="Immediate shutdown recommended."
        )

    elif health < 50:

        create_alert(
            db=db,
            machine_id=machine_id,
            severity="High",
            message="Maintenance required immediately."
        )

    elif health < 70:

        create_alert(
            db=db,
            machine_id=machine_id,
            severity="Medium",
            message="Schedule machine inspection."
        )

    elif health < 90:

        create_alert(
            db=db,
            machine_id=machine_id,
            severity="Low",
            message="Monitor machine condition."
        )

    return prediction