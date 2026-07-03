from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_database_session
from app.database.repositories.alert_repository import get_active_alerts

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)


@router.get("/")
def alerts(db: Session = Depends(get_database_session)):
    return get_active_alerts(db)