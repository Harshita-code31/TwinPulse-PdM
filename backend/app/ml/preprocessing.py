from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


# =====================================================
# CONFIG
# =====================================================

SEQUENCE_LENGTH = 20

ROOT_DIR = Path(__file__).resolve().parents[3]

DATASET = ROOT_DIR / "data" / "training" / "predictive_maintenance_dataset.csv"

ARTIFACTS = ROOT_DIR / "artifacts"

SCALER_DIR = ARTIFACTS / "scalers"

DATA_DIR = ARTIFACTS / "processed"

SCALER_DIR.mkdir(parents=True, exist_ok=True)

DATA_DIR.mkdir(parents=True, exist_ok=True)


# =====================================================
# LOAD DATA
# =====================================================

print("Loading dataset...")

df = pd.read_csv(DATASET)

print(f"Rows : {len(df)}")


# =====================================================
# REMOVE UNUSED COLUMNS
# =====================================================

df = df.drop(
    columns=[
        "timestamp",
        "machine_name",
    ]
)


# =====================================================
# ENCODE CATEGORICAL DATA
# =====================================================

machine_encoder = LabelEncoder()

fault_encoder = LabelEncoder()

df["machine_type"] = machine_encoder.fit_transform(
    df["machine_type"]
)

df["fault_type"] = fault_encoder.fit_transform(
    df["fault_type"]
)

joblib.dump(
    machine_encoder,
    SCALER_DIR / "machine_encoder.pkl",
)

joblib.dump(
    fault_encoder,
    SCALER_DIR / "fault_encoder.pkl",
)


# =====================================================
# FEATURES
# =====================================================

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

TARGET_COLUMN = "health_score"


# =====================================================
# SCALE FEATURES
# =====================================================

scaler = MinMaxScaler()

scaled_features = scaler.fit_transform(
    df[FEATURE_COLUMNS]
)

joblib.dump(
    scaler,
    SCALER_DIR / "feature_scaler.pkl",
)


# =====================================================
# CREATE SEQUENCES
# =====================================================

print("Creating sequences...")

X = []

y = []

machine_ids = df["machine_id"].unique()

for machine_id in machine_ids:

    machine_df = df[
        df["machine_id"] == machine_id
    ].reset_index(drop=True)

    machine_scaled = scaler.transform(
        machine_df[FEATURE_COLUMNS]
    )

    target = machine_df[TARGET_COLUMN].values

    for i in range(
        len(machine_df) - SEQUENCE_LENGTH
    ):

        X.append(
            machine_scaled[
                i : i + SEQUENCE_LENGTH
            ]
        )

        y.append(
            target[
                i + SEQUENCE_LENGTH
            ]
        )

X = np.array(X)

y = np.array(y)

print("Sequences:", len(X))


# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    shuffle=True,

)


# =====================================================
# SAVE
# =====================================================

np.save(
    DATA_DIR / "X_train.npy",
    X_train,
)

np.save(
    DATA_DIR / "X_test.npy",
    X_test,
)

np.save(
    DATA_DIR / "y_train.npy",
    y_train,
)

np.save(
    DATA_DIR / "y_test.npy",
    y_test,
)

print()

print("=" * 50)

print("Preprocessing Complete")

print(f"Training Samples : {len(X_train)}")

print(f"Testing Samples  : {len(X_test)}")

print()

print("Saved to:")

print(DATA_DIR)

print("=" * 50)