import json
import os

import paho.mqtt.client as mqtt

from app.database.db import create_session_factory
from app.database.repositories.sensor_repository import save_sensor_data
from app.services.prediction_service import predict_machine

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))

SENSOR_TOPIC = "machines/sensors"
PREDICTION_TOPIC = "machines/predictions"

SessionFactory = create_session_factory()


def on_connect(client, userdata, flags, rc):
    print(f"Connected to Mosquitto (Code: {rc})")
    client.subscribe(SENSOR_TOPIC)


def on_message(client, userdata, msg):

    db = SessionFactory()

    try:
        payload = json.loads(msg.payload.decode())

        # Save incoming sensor data
        save_sensor_data(db, payload)

        print(f"Sensor Data Saved -> Machine {payload['machine_id']}")

        # Run ML prediction
        prediction = predict_machine(
            db=db,
            machine_id=payload["machine_id"]
        )

        print("Prediction Generated")

        # Publish prediction back to MQTT
        client.publish(
            PREDICTION_TOPIC,
            json.dumps(prediction, default=str)
        )

        print(f"Published Prediction -> {PREDICTION_TOPIC}")

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

    print(f"Listening on {BROKER}:{PORT}")
    print(f"Subscribed : {SENSOR_TOPIC}")
    print(f"Publishing : {PREDICTION_TOPIC}\n")

    client.loop_forever()


if __name__ == "__main__":
    main()