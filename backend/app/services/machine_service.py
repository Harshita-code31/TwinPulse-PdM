from sqlalchemy.orm import Session

from app.database.models.machine import Machine
from app.database.repositories.machine_repository import (
    create_machine,
    get_all_machines,
    get_machine_by_id,
)
from app.database.repositories.machine_repository import (
    update_machine,
    delete_machine,
)

def edit_machine(db: Session, machine_id: int, machine: Machine):
    return update_machine(db, machine_id, machine)


def remove_machine(db: Session, machine_id: int):
    return delete_machine(db, machine_id)


def get_machines(db: Session) -> list[Machine]:
    """
    Return all machines.
    """
    return get_all_machines(db)


def get_machine(db: Session, machine_id: int) -> Machine | None:
    """
    Return a machine by ID.
    """
    return get_machine_by_id(db, machine_id)


def add_machine(db: Session, machine: Machine) -> Machine:
    """
    Create a new machine.
    """
    return create_machine(db, machine)