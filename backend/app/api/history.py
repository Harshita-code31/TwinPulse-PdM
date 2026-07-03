from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_database_session
from app.schemas.history import HistoryResponse
from app.services.history_service import get_history

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get("/{machine_id}", response_model=list[HistoryResponse])
def read_history(
    machine_id: int,
    db: Session = Depends(get_database_session),
):
    return get_history(
        db,
        machine_id,
    )