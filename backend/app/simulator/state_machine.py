import random


class StateMachine:
    """
    Controls machine state transitions.
    """

    AVAILABLE_FAULTS = [
        "Bearing Wear",
        "Lubrication Failure",
        "Motor Overload",
        "Gear Wear",
        "Shaft Misalignment",
    ]

    def update_state(self, machine):
        """
        Updates the machine state based on health.
        """

        # Healthy machine
        if machine.health_score >= 90:

            machine.current_fault = "Healthy"
            return

        # Assign ONE fault when degradation starts
        if (
            machine.current_fault == "Healthy"
            and machine.health_score < 90
        ):

            machine.current_fault = random.choice(
                self.AVAILABLE_FAULTS
            )

            return

        # Critical stage
        if (
            machine.health_score <= 40
            and machine.current_fault != "Failure"
        ):

            machine.current_fault = "Critical"

            return

        # Failure stage
        if machine.health_score <= 10:

            machine.current_fault = "Failure"

            return

        # Simulate maintenance automatically
        if machine.health_score <= 2:

            machine.health_score = random.uniform(85, 95)

            machine.current_fault = "Healthy"

            machine.temperature = 60

            machine.rpm = 1450

            machine.torque = 120

            machine.vibration = 1.2

            machine.current = 6.5

            machine.oil_level = 100

            machine.maintenance_count += 1

            machine.last_maintenance_hour = machine.operating_hours