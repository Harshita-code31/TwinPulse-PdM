from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from app.ml.model_loader import get_model


# -------------------------------------------------
# Model Artifacts
# -------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[3]
ARTIFACTS = ROOT_DIR / "artifacts"

SCALER_PATH = ARTIFACTS / "scalers" / "feature_scaler.pkl"
MACHINE_ENCODER = ARTIFACTS / "scalers" / "machine_encoder.pkl"
FAULT_ENCODER = ARTIFACTS / "scalers" / "fault_encoder.pkl"

model = get_model()
scaler = joblib.load(SCALER_PATH)
machine_encoder = joblib.load(MACHINE_ENCODER)
fault_encoder = joblib.load(FAULT_ENCODER)


FEATURE_COLUMNS = [
    "machine_type",
    "operating_hours",
    "machine_age",
    "ambient_temperature",
    "operating_load",
    "temperature",
    "rpm",
    "torque",
    "vibration",
    "current",
    "oil_level",
    "maintenance_count",
    "fault_type",
]


# -------------------------------------------------
# Health Classification
# -------------------------------------------------

def condition_from_health(health):
    if health >= 90:
        return "HEALTHY"
    if health >= 70:
        return "WATCH"
    if health >= 50:
        return "WARNING"
    if health >= 30:
        return "CRITICAL"
    return "SEVERE"


# -------------------------------------------------
# Descriptive Sensor Analysis
# -------------------------------------------------

def calculate_sensor_changes(df):
    """
    Compare average sensor values from the first and second halves
    of the latest 20-reading window.

    These values are descriptive telemetry observations.
    They are not additional ML predictions.
    """

    window = df.tail(20)

    first = window.iloc[:10]
    second = window.iloc[10:]

    changes = {}

    for column in [
        "temperature",
        "vibration",
        "current",
        "oil_level",
        "rpm",
        "torque",
    ]:
        old_average = float(first[column].mean())
        new_average = float(second[column].mean())

        changes[column] = {
            "previous_average": round(old_average, 3),
            "recent_average": round(new_average, 3),
            "change": round(new_average - old_average, 3),
        }

    return changes


# -------------------------------------------------
# ML Prediction
# -------------------------------------------------

def predict_machine_health(df: pd.DataFrame):
    """
    Predict machine health using the trained TensorFlow model.

    The model consumes the latest 20 telemetry readings.
    Sensor changes are returned separately as descriptive analytics.
    """

    if len(df) < 20:
        raise ValueError(
            "At least 20 sensor readings are required."
        )

    latest = df.tail(20).copy()

    # Calculate telemetry observations before encoding/scaling.
    sensor_changes = calculate_sensor_changes(latest)

    latest["machine_type"] = machine_encoder.transform(
        latest["machine_type"]
    )

    latest["fault_type"] = fault_encoder.transform(
        latest["fault_type"]
    )

    scaled = scaler.transform(
        latest[FEATURE_COLUMNS]
    )

    X = np.expand_dims(
        scaled,
        axis=0
    )

    prediction = model.predict(
        X,
        verbose=0
    )[0][0]

    health = max(
        0.0,
        min(float(prediction), 100.0)
    )

    return {
        # Genuine TensorFlow model output
        "health_score": round(health, 2),

        # Classification derived directly from ML health score
        "condition": condition_from_health(health),

        # Descriptive telemetry, not ML prediction
        "sensor_changes": sensor_changes,

        # -------------------------------------------------
        # Legacy persistence fields
        # -------------------------------------------------
        # Existing DB schema requires these non-null values.
        # They are intentionally removed from the public API later
        # because they are derived heuristics, not independent
        # ML predictions.
        "_legacy_failure_probability": round(
            100.0 - health,
            2
        ),

        "_legacy_remaining_useful_life": round(
            max(health * 2.0, 0.0),
            2
        ),
    }
