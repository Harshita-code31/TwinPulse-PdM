import json
import os
import time

import paho.mqtt.client as mqtt

from app.simulator.machine import Machine

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = "machines/sensors"

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

    Machine(5, "Conveyor-1", "Conveyor")

]

# --------------------------------------------------
# Publish Loop
# --------------------------------------------------

def main():

    print(f"\nPublishing Digital Twin Data to {BROKER}:{PORT}...\n")

    while True:

        for machine in machines:

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