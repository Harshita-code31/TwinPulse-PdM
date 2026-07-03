from sqlalchemy.orm import Session

from app.database.models.alert import Alert


def create_alert(
    db: Session,
    machine_id: int,
    severity: str,
    message: str
):

    alert = Alert(

        machine_id=machine_id,

        severity=severity,

        message=message

    )

    db.add(alert)

    db.commit()

    db.refresh(alert)

    return alert


def get_active_alerts(db: Session):

    return (

        db.query(Alert)

        .filter(
            Alert.is_acknowledged == False
        )

        .order_by(
            Alert.created_at.desc()
        )

        .all()

    )