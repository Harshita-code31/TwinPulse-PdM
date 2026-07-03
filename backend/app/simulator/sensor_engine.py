import random


class SensorEngine:
    """
    Adds realistic industrial sensor behaviour.
    """

    def apply_noise(self, machine):

        # -------------------------
        # Gaussian Noise
        # -------------------------

        machine.temperature += random.gauss(0, 0.25)

        machine.vibration += random.gauss(0, 0.05)

        machine.current += random.gauss(0, 0.08)

        machine.torque += random.gauss(0, 0.40)

        machine.rpm += int(random.gauss(0, 2))

        # -------------------------
        # Temperature Drift
        # -------------------------

        machine.temperature += (
            machine.operating_hours * 0.0003
        )

        # -------------------------
        # Rare Sensor Spikes
        # -------------------------

        if random.random() < 0.001:

            machine.temperature += random.uniform(3, 8)

        if random.random() < 0.001:

            machine.vibration += random.uniform(0.4, 1.5)

        if random.random() < 0.001:

            machine.current += random.uniform(0.5, 1.5)

        # -------------------------
        # Clamp Values
        # -------------------------

        machine.temperature = max(
            20,
            min(machine.temperature, 150)
        )

        machine.vibration = max(
            0,
            min(machine.vibration, 10)
        )

        machine.current = max(
            0,
            min(machine.current, 20)
        )

        machine.oil_level = max(
            0,
            min(machine.oil_level, 100)
        )

        machine.rpm = max(
            500,
            min(machine.rpm, 3000)
        )

        machine.torque = max(
            0,
            min(machine.torque, 600)
        )