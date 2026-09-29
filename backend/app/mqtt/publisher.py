import json
import os
import time

import paho.mqtt.client as mqtt

from app.simulator.machine import Machine

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = "machines/sensors"

# Controlled degradation demo.
# Set DEMO_MODE=false for normal simulation.
DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() == "true"
DEMO_FAULT_START = int(os.getenv("DEMO_FAULT_START", "20"))


# --------------------------------------------------
# MQTT Client
# --------------------------------------------------

client = mqtt.Client()
client.connect(BROKER, PORT)


# --------------------------------------------------
# Digital Twin Machines
# --------------------------------------------------

machines = [
    Machine(1, "Gearbox-1", "Gearbox"),
    Machine(2, "Pump-1", "Pump"),
    Machine(3, "Compressor-1", "Compressor"),
    Machine(4, "Motor-1", "Motor"),
    Machine(5, "Conveyor-1", "Conveyor"),
]


# --------------------------------------------------
# Controlled Demo Scenario
# --------------------------------------------------

def apply_demo_scenario(machine):
    """
    Inject a reproducible Bearing Wear scenario into Gearbox-1.

    This is simulated fault injection for demonstration/testing,
    not a real observed equipment failure.
    """

    if not DEMO_MODE:
        return

    if (
        machine.machine_id == 1
        and machine.operating_hours >= DEMO_FAULT_START
    ):
        machine.current_fault = "Bearing Wear"


# --------------------------------------------------
# Publish Loop
# --------------------------------------------------

def main():

    print(f"\nPublishing Digital Twin Data to {BROKER}:{PORT}...\n")

    if DEMO_MODE:
        print(
            "DEMO MODE enabled: "
            f"Gearbox-1 Bearing Wear begins after "
            f"{DEMO_FAULT_START} cycles.\n"
        )

    while True:

        for machine in machines:

            # Set controlled fault before updating sensor state.
            apply_demo_scenario(machine)

            machine.update()

            payload = machine.to_dict()

            client.publish(
                TOPIC,
                json.dumps(payload)
            )

            print(payload)

        time.sleep(2)


if __name__ == "__main__":
    main()
