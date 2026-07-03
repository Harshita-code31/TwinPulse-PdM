from dataclasses import dataclass

from app.simulator.state_machine import StateMachine
from app.simulator.fault_engine import FaultEngine
from app.simulator.sensor_engine import SensorEngine


@dataclass
class Machine:
    """
    Digital Twin representing one industrial machine.
    """

    # -----------------------------
    # Identity
    # -----------------------------

    machine_id: int
    machine_name: str
    machine_type: str

    # -----------------------------
    # Machine Properties
    # -----------------------------

    health_score: float = 100.0

    operating_hours: int = 0

    machine_age: int = 0

    operating_load: float = 50.0

    ambient_temperature: float = 30.0

    current_fault: str = "Healthy"

    maintenance_count: int = 0

    last_maintenance_hour: int = 0

    # -----------------------------
    # Sensors
    # -----------------------------

    temperature: float = 60.0

    rpm: int = 1450

    torque: float = 120.0

    vibration: float = 1.2

    current: float = 6.5

    oil_level: float = 100.0

    # -----------------------------
    # Engines
    # -----------------------------

    def __post_init__(self):

        self.state_engine = StateMachine()

        self.fault_engine = FaultEngine()

        self.sensor_engine = SensorEngine()

    # -----------------------------
    # One Simulation Cycle
    # -----------------------------

    def update(self):

        self.update_operating_hours()

        self.update_environment()

    # Dataset Generator controls the fault.
    # Do NOT overwrite it here.

        self.fault_engine.apply_fault(self)

        self.sensor_engine.apply_noise(self)

    # -----------------------------
    # Helpers
    # -----------------------------

    def update_operating_hours(self):

        self.operating_hours += 1

        self.machine_age = self.operating_hours // 1000

    def update_environment(self):

        # Ambient temperature effect

        self.temperature += (
            (self.ambient_temperature - 30) * 0.005
        )

        # Load effect

        self.temperature += (
            (self.operating_load - 50) * 0.004
        )

        self.current += (
            (self.operating_load - 50) * 0.002
        )

        self.torque += (
            (self.operating_load - 50) * 0.01
        )

    # -----------------------------
    # Export Machine State
    # -----------------------------

    def to_dict(self):

        return {

            "machine_id": self.machine_id,

            "machine_name": self.machine_name,

            "machine_type": self.machine_type,

            "operating_hours": self.operating_hours,

            "machine_age": self.machine_age,

            "operating_load": round(self.operating_load,2),

            "ambient_temperature": round(self.ambient_temperature,2),

            "temperature": round(self.temperature,2),

            "rpm": self.rpm,

            "torque": round(self.torque,2),

            "vibration": round(self.vibration,2),

            "current": round(self.current,2),

            "oil_level": round(self.oil_level,2),

            "health_score": round(self.health_score,2),

            "fault_type": self.current_fault,

            "maintenance_count": self.maintenance_count,

            "last_maintenance_hour": self.last_maintenance_hour

        }