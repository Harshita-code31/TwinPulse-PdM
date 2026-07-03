from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_database_session
from app.database.models.machine import Machine
from app.schemas.machine import MachineCreate, MachineResponse
from app.services.machine_service import (
    add_machine,
    edit_machine,
    get_machine,
    get_machines,
    remove_machine,
)

router = APIRouter(
    prefix="/machines",
    tags=["Machines"],
)


@router.get("/", response_model=list[MachineResponse])
def read_machines(
    db: Session = Depends(get_database_session),
):
    return get_machines(db)


@router.get("/{machine_id}", response_model=MachineResponse)
def read_machine(
    machine_id: int,
    db: Session = Depends(get_database_session),
):
    machine = get_machine(db, machine_id)

    if machine is None:
        raise HTTPException(
            status_code=404,
            detail="Machine not found",
        )

    return machine


@router.post("/", response_model=MachineResponse)
def create_machine(
    machine: MachineCreate,
    db: Session = Depends(get_database_session),
):
    new_machine = Machine(
        machine_name=machine.machine_name,
        machine_type=machine.machine_type,
        location=machine.location,
        installation_date=machine.installation_date,
        status=machine.status,
    )

    return add_machine(db, new_machine)


@router.put("/{machine_id}", response_model=MachineResponse)
def update_machine(
    machine_id: int,
    machine: MachineCreate,
    db: Session = Depends(get_database_session),
):
    updated_machine = Machine(
        machine_name=machine.machine_name,
        machine_type=machine.machine_type,
        location=machine.location,
        installation_date=machine.installation_date,
        status=machine.status,
    )

    result = edit_machine(
        db,
        machine_id,
        updated_machine,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Machine not found",
        )

    return result


@router.delete("/{machine_id}")
def delete_machine(
    machine_id: int,
    db: Session = Depends(get_database_session),
):
    deleted = remove_machine(
        db,
        machine_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Machine not found",
        )

    return {
        "message": "Machine deleted successfully"
    }