from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base


class SensorData(Base):

    __tablename__ = "sensor_data"

    sensor_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    machine_id: Mapped[int] = mapped_column(
        ForeignKey("machines.machine_id"),
        nullable=False,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    # ---------- Machine Metadata ----------

    machine_type: Mapped[str] = mapped_column(String(100))

    operating_hours: Mapped[int] = mapped_column(Integer)

    machine_age: Mapped[int] = mapped_column(Integer)

    ambient_temperature: Mapped[float] = mapped_column(Float)

    operating_load: Mapped[float] = mapped_column(Float)

    maintenance_count: Mapped[int] = mapped_column(Integer)

    fault_type: Mapped[str] = mapped_column(String(100))

    # ---------- Sensors ----------

    temperature: Mapped[float] = mapped_column(Float)

    rpm: Mapped[int] = mapped_column(Integer)

    torque: Mapped[float] = mapped_column(Float)

    vibration: Mapped[float] = mapped_column(Float)

    current: Mapped[float] = mapped_column(Float)

    oil_level: Mapped[float] = mapped_column(Float)

    machine = relationship(
        "Machine",
        back_populates="sensor_data",
    )