import json
import os

import paho.mqtt.client as mqtt

from app.database.db import create_session_factory
from app.database.repositories.sensor_repository import save_sensor_data

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = "machines/sensors"

SessionFactory = create_session_factory()


def on_connect(client, userdata, flags, rc):
    print(f"Connected to Mosquitto (Code: {rc})")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):

    db = SessionFactory()

    try:

        payload = json.loads(msg.payload.decode())

        save_sensor_data(db, payload)

        print(f"Saved -> Machine {payload['machine_id']}")

    except Exception as e:

        db.rollback()

        print(f"Error: {e}")

    finally:

        db.close()


def main():

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT)

    print(f"Waiting for sensor data on {BROKER}:{PORT}...\n")

    client.loop_forever()


if __name__ == "__main__":
    main()