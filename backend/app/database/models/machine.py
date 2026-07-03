from datetime import date

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base


class Machine(Base):
    """
    Machine master table.
    Stores static information about industrial machines.
    """

    __tablename__ = "machines"

    machine_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    machine_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    machine_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    installation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Healthy"
    )

    sensor_data = relationship(
        "SensorData",
        back_populates="machine",
        cascade="all, delete-orphan"
    )

    predictions = relationship(
        "Prediction",
        back_populates="machine",
        cascade="all, delete-orphan"
    )

    maintenance_logs = relationship(
        "MaintenanceLog",
        back_populates="machine",
        cascade="all, delete-orphan"
    )

    alerts = relationship(
        "Alert",
        back_populates="machine",
        cascade="all, delete-orphan"
    )