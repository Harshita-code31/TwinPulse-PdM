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
RANDOM_STATE = 42

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

print(f"Rows     : {len(df):,}")
print(f"Machines : {df['machine_id'].nunique()}")


# =====================================================
# FEATURES
# fault_type intentionally excluded.
# It is simulator ground truth, not an observable sensor.
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
]

TARGET_COLUMN = "health_score"


# =====================================================
# MACHINE-LEVEL SPLIT
#
# Split machines BEFORE sequence generation so that
# overlapping windows from one machine cannot leak
# between train, validation and test sets.
# =====================================================

machine_table = (
    df[["machine_id", "machine_type"]]
    .drop_duplicates()
    .sort_values("machine_id")
    .reset_index(drop=True)
)

train_machines, temp_machines = train_test_split(
    machine_table,
    test_size=0.30,
    random_state=RANDOM_STATE,
    stratify=machine_table["machine_type"],
)

val_machines, test_machines = train_test_split(
    temp_machines,
    test_size=0.50,
    random_state=RANDOM_STATE,
    stratify=temp_machines["machine_type"],
)

train_ids = set(train_machines["machine_id"])
val_ids = set(val_machines["machine_id"])
test_ids = set(test_machines["machine_id"])

train_df = df[df["machine_id"].isin(train_ids)].copy()
val_df = df[df["machine_id"].isin(val_ids)].copy()
test_df = df[df["machine_id"].isin(test_ids)].copy()

print()
print("Machine split")
print(f"Train      : {len(train_ids)}")
print(f"Validation : {len(val_ids)}")
print(f"Test       : {len(test_ids)}")

assert train_ids.isdisjoint(val_ids)
assert train_ids.isdisjoint(test_ids)
assert val_ids.isdisjoint(test_ids)


# =====================================================
# MACHINE TYPE ENCODER
# Fit ONLY on training data.
# =====================================================

machine_encoder = LabelEncoder()

machine_encoder.fit(train_df["machine_type"])

train_df["machine_type"] = machine_encoder.transform(
    train_df["machine_type"]
)

val_df["machine_type"] = machine_encoder.transform(
    val_df["machine_type"]
)

test_df["machine_type"] = machine_encoder.transform(
    test_df["machine_type"]
)

joblib.dump(
    machine_encoder,
    SCALER_DIR / "machine_encoder.pkl",
)


# =====================================================
# FEATURE SCALER
# Fit ONLY on training data.
# =====================================================

scaler = MinMaxScaler()

scaler.fit(train_df[FEATURE_COLUMNS])

joblib.dump(
    scaler,
    SCALER_DIR / "feature_scaler.pkl",
)


# =====================================================
# CREATE SEQUENCES
# =====================================================

def create_sequences(split_df):
    X = []
    y = []

    for machine_id in sorted(split_df["machine_id"].unique()):

        machine_df = (
            split_df[split_df["machine_id"] == machine_id]
            .sort_values("operating_hours")
            .reset_index(drop=True)
        )

        machine_scaled = scaler.transform(
            machine_df[FEATURE_COLUMNS]
        )

        target = machine_df[TARGET_COLUMN].values

        for i in range(len(machine_df) - SEQUENCE_LENGTH):

            X.append(
                machine_scaled[i:i + SEQUENCE_LENGTH]
            )

            y.append(
                target[i + SEQUENCE_LENGTH]
            )

    return (
        np.asarray(X, dtype=np.float32),
        np.asarray(y, dtype=np.float32),
    )


print()
print("Creating leakage-safe sequences...")

X_train, y_train = create_sequences(train_df)
X_val, y_val = create_sequences(val_df)
X_test, y_test = create_sequences(test_df)

print(f"Training sequences   : {len(X_train):,}")
print(f"Validation sequences : {len(X_val):,}")
print(f"Testing sequences    : {len(X_test):,}")
print(f"Input shape          : {X_train.shape}")


# =====================================================
# SAVE
# =====================================================

np.save(DATA_DIR / "X_train.npy", X_train)
np.save(DATA_DIR / "y_train.npy", y_train)

np.save(DATA_DIR / "X_val.npy", X_val)
np.save(DATA_DIR / "y_val.npy", y_val)

np.save(DATA_DIR / "X_test.npy", X_test)
np.save(DATA_DIR / "y_test.npy", y_test)

np.save(
    DATA_DIR / "train_machine_ids.npy",
    np.array(sorted(train_ids)),
)

np.save(
    DATA_DIR / "val_machine_ids.npy",
    np.array(sorted(val_ids)),
)

np.save(
    DATA_DIR / "test_machine_ids.npy",
    np.array(sorted(test_ids)),
)

print()
print("=" * 60)
print("PREPROCESSING COMPLETE")
print("=" * 60)
print("fault_type excluded from model inputs")
print("scaler fitted on training machines only")
print("machine-level train/validation/test separation")
print("=" * 60)
