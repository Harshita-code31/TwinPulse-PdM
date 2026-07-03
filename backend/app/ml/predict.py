from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from app.ml.model_loader import get_model


# -------------------------------------------------
# Paths
# -------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[3]

ARTIFACTS = ROOT_DIR / "artifacts"

SCALER_PATH = (
    ARTIFACTS
    / "scalers"
    / "feature_scaler.pkl"
)

MACHINE_ENCODER = (
    ARTIFACTS
    / "scalers"
    / "machine_encoder.pkl"
)

FAULT_ENCODER = (
    ARTIFACTS
    / "scalers"
    / "fault_encoder.pkl"
)


# -------------------------------------------------
# Load once
# -------------------------------------------------

model = get_model()

scaler = joblib.load(SCALER_PATH)

machine_encoder = joblib.load(MACHINE_ENCODER)

fault_encoder = joblib.load(FAULT_ENCODER)


# -------------------------------------------------
# Recommendation Engine
# -------------------------------------------------

def recommendation(health):

    if health >= 90:
        return "Machine Healthy"

    elif health >= 70:
        return "Monitor machine"

    elif health >= 50:
        return "Schedule Inspection"

    elif health >= 30:
        return "Maintenance Required"

    return "Immediate Shutdown Recommended"


# -------------------------------------------------
# Failure Probability
# -------------------------------------------------

def failure_probability(health):

    probability = 100 - health

    probability = max(
        0,
        min(probability, 100)
    )

    return round(probability, 2)


# -------------------------------------------------
# Remaining Useful Life
# -------------------------------------------------

def calculate_rul(health):

    rul = health * 2

    return round(max(rul, 0), 2)


# -------------------------------------------------
# Prediction
# -------------------------------------------------

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

    "fault_type"

]


def predict_machine_health(df: pd.DataFrame):

    """
    Predict machine health using the
    last 20 sensor readings.
    """

    if len(df) < 20:

        raise ValueError(
            "At least 20 sensor readings are required."
        )

    latest = df.tail(20).copy()

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

    prediction = float(prediction)

    prediction = max(
        0,
        min(prediction, 100)
    )

    return {

        "health_score":
            round(prediction, 2),

        "failure_probability":
            failure_probability(prediction),

        "remaining_useful_life":
            calculate_rul(prediction),

        "recommendation":
            recommendation(prediction)

    }