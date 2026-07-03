from datetime import date

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base


class MaintenanceLog(Base):
    """
    Stores maintenance history.
    """

    __tablename__ = "maintenance_logs"

    maintenance_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    machine_id: Mapped[int] = mapped_column(
        ForeignKey("machines.machine_id"),
        nullable=False,
    )

    maintenance_type: Mapped[str] = mapped_column(
        String(100)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    technician: Mapped[str] = mapped_column(
        String(100)
    )

    maintenance_date: Mapped[date] = mapped_column(
        Date
    )

    remarks: Mapped[str] = mapped_column(
        Text
    )

    machine = relationship(
        "Machine",
        back_populates="maintenance_logs",
    )