from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base


class Alert(Base):
    """
    Stores machine alerts.
    """

    __tablename__ = "alerts"

    alert_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    machine_id: Mapped[int] = mapped_column(
        ForeignKey("machines.machine_id"),
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(30)
    )

    message: Mapped[str] = mapped_column(
        String(255)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    is_acknowledged: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    machine = relationship(
        "Machine",
        back_populates="alerts",
    )