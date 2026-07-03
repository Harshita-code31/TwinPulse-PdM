from sqlalchemy.orm import Session

from app.database.models.machine import Machine


def get_all_machines(db: Session) -> list[Machine]:
    """
    Return all machines.
    """
    return db.query(Machine).all()


def get_machine_by_id(db: Session, machine_id: int) -> Machine | None:
    """
    Return a machine by its ID.
    """
    return (
        db.query(Machine)
        .filter(Machine.machine_id == machine_id)
        .first()
    )


def create_machine(db: Session, machine: Machine) -> Machine:
    """
    Create a new machine.
    """
    db.add(machine)
    db.commit()
    db.refresh(machine)

    return machine

def update_machine(db: Session, machine_id: int, updated_machine: Machine) -> Machine | None:
    """
    Update an existing machine.
    """

    machine = get_machine_by_id(db, machine_id)

    if machine is None:
        return None

    machine.machine_name = updated_machine.machine_name
    machine.machine_type = updated_machine.machine_type
    machine.location = updated_machine.location
    machine.installation_date = updated_machine.installation_date
    machine.status = updated_machine.status

    db.commit()
    db.refresh(machine)

    return machine


def delete_machine(db: Session, machine_id: int) -> bool:
    """
    Delete a machine.
    """

    machine = get_machine_by_id(db, machine_id)

    if machine is None:
        return False

    db.delete(machine)
    db.commit()

    return True