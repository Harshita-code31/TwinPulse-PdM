import random


FAULT_PROFILES = {
    "Healthy": {
        "temp_rate": 0.000,
        "vibration_rate": 0.000,
        "current_rate": 0.000,
        "oil_rate": -0.002,
        "rpm_rate": 0,
        "torque_rate": 0,
        "health_rate": 0.002,
    },

    "Bearing Wear": {
        "temp_rate": 0.020,
        "vibration_rate": 0.015,
        "current_rate": 0.006,
        "oil_rate": -0.003,
        "rpm_rate": 0,
        "torque_rate": 0.10,
        "health_rate": 0.020,
    },

    "Lubrication Failure": {
        "temp_rate": 0.035,
        "vibration_rate": 0.010,
        "current_rate": 0.008,
        "oil_rate": -0.050,
        "rpm_rate": 0,
        "torque_rate": 0.20,
        "health_rate": 0.030,
    },

    "Motor Overload": {
        "temp_rate": 0.040,
        "vibration_rate": 0.008,
        "current_rate": 0.020,
        "oil_rate": -0.005,
        "rpm_rate": -2,
        "torque_rate": 0.80,
        "health_rate": 0.040,
    },

    "Gear Wear": {
        "temp_rate": 0.025,
        "vibration_rate": 0.020,
        "current_rate": 0.007,
        "oil_rate": -0.004,
        "rpm_rate": 0,
        "torque_rate": 0.30,
        "health_rate": 0.025,
    },

    "Shaft Misalignment": {
        "temp_rate": 0.018,
        "vibration_rate": 0.018,
        "current_rate": 0.010,
        "oil_rate": -0.003,
        "rpm_rate": 0,
        "torque_rate": 0.50,
        "health_rate": 0.025,
    },

    "Critical": {
        "temp_rate": 0.060,
        "vibration_rate": 0.030,
        "current_rate": 0.030,
        "oil_rate": -0.020,
        "rpm_rate": -5,
        "torque_rate": 1.00,
        "health_rate": 0.080,
    },

    "Failure": {
        "temp_rate": 0.100,
        "vibration_rate": 0.050,
        "current_rate": 0.050,
        "oil_rate": -0.050,
        "rpm_rate": -10,
        "torque_rate": 2.00,
        "health_rate": 0.150,
    },
}


class FaultEngine:
    """
    Applies fault effects to the machine.
    """

    def apply_fault(self, machine):

        profile = FAULT_PROFILES[machine.current_fault]

        # Temperature
        machine.temperature += profile["temp_rate"]

        # Vibration
        machine.vibration += profile["vibration_rate"]

        # Motor Current
        machine.current += profile["current_rate"]

        # Oil Level
        machine.oil_level += profile["oil_rate"]

        # RPM
        machine.rpm += profile["rpm_rate"]

        # Torque
        machine.torque += profile["torque_rate"]

        # Health degradation
        machine.health_score -= profile["health_rate"]

        # Clamp values
        machine.health_score = max(0.0, machine.health_score)

        machine.oil_level = max(0.0, machine.oil_level)

        machine.temperature = min(machine.temperature, 150)

        machine.vibration = min(machine.vibration, 10)

        machine.current = min(machine.current, 20)