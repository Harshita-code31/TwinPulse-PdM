from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_database_session
from app.services.prediction_service import predict_machine

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.get("/{machine_id}")
def predict(machine_id: int, db: Session = Depends(get_database_session)):

    try:

        result = predict_machine(db, machine_id)

        return {

            "success": True,

            "machine_id": machine_id,

            "prediction": result

        }

    except Exception as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )