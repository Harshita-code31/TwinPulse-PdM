from datetime import date

from sqlalchemy.orm import Session

from app.database.db import create_session_factory
from app.database.models.machine import Machine
from app.database.models.sensor import SensorData
from app.database.models.prediction import Prediction
from app.database.models.alert import Alert


def seed_database(db: Session):
    """
    Reset demo data and create default machines.
    """

    # -------------------------------
    # Clear runtime tables
    # -------------------------------

    db.query(Alert).delete()

    db.query(Prediction).delete()

    db.query(SensorData).delete()

    db.query(Machine).delete()

    db.commit()

    # -------------------------------
    # Demo Machines
    # -------------------------------

    machines = [

        Machine(
            machine_id=1,
            machine_name="Gearbox-1",
            machine_type="Gearbox",
            location="Plant A",
            installation_date=date(2026,1,1),
            status="Running"
        ),

        Machine(
            machine_id=2,
            machine_name="Pump-1",
            machine_type="Pump",
            location="Plant A",
            installation_date=date(2026,1,1),
            status="Running"
        ),

        Machine(
            machine_id=3,
            machine_name="Compressor-1",
            machine_type="Compressor",
            location="Plant A",
            installation_date=date(2026,1,1),
            status="Running"
        ),

        Machine(
            machine_id=4,
            machine_name="Motor-1",
            machine_type="Motor",
            location="Plant A",
            installation_date=date(2026,1,1),
            status="Running"
        ),

        Machine(
            machine_id=5,
            machine_name="Conveyor-1",
            machine_type="Conveyor",
            location="Plant A",
            installation_date=date(2026,1,1),
            status="Running"
        )

    ]

    db.add_all(machines)

    db.commit()

    print("Database seeded successfully.")

    from app.database.db import create_session_factory

if __name__ == "__main__":

    SessionFactory = create_session_factory()

    db = SessionFactory()

    try:
        seed_database(db)
    finally:
        db.close()