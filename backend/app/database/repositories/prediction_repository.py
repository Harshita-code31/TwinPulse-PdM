from sqlalchemy.orm import Session

from app.database.models.prediction import Prediction


def save_prediction(db: Session, prediction: dict):

    record = Prediction(

        machine_id=prediction["machine_id"],

        health_score=prediction["health_score"],

        failure_probability=prediction["_legacy_failure_probability"],

        remaining_useful_life=prediction["_legacy_remaining_useful_life"],

        predicted_fault=prediction["simulation_fault"]

    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record


def get_predictions_by_machine(
    db: Session,
    machine_id: int
):

    return (

        db.query(Prediction)

        .filter(
            Prediction.machine_id == machine_id
        )

        .order_by(
            Prediction.timestamp.desc()
        )

        .all()

    )