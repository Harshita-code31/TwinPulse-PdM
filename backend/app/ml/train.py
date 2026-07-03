from pathlib import Path

import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping


# ============================================
# PATHS
# ============================================

ROOT_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = ROOT_DIR / "artifacts" / "processed"

MODEL_DIR = ROOT_DIR / "artifacts" / "trained_models"

MODEL_DIR.mkdir(parents=True, exist_ok=True)


# ============================================
# LOAD DATA
# ============================================

print("Loading training data...")

X_train = np.load(DATA_DIR / "X_train.npy")
X_test = np.load(DATA_DIR / "X_test.npy")

y_train = np.load(DATA_DIR / "y_train.npy")
y_test = np.load(DATA_DIR / "y_test.npy")

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")


# ============================================
# MODEL
# ============================================

model = Sequential([

    LSTM(
        64,
        return_sequences=True,
        input_shape=(
            X_train.shape[1],
            X_train.shape[2]
        )
    ),

    Dropout(0.2),

    LSTM(32),

    Dropout(0.2),

    Dense(16, activation="relu"),

    Dense(1)

])


model.compile(

    optimizer="adam",

    loss="mse",

    metrics=["mae"]

)


model.summary()


# ============================================
# TRAIN
# ============================================

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=5,

    restore_best_weights=True

)


history = model.fit(

    X_train,

    y_train,

    validation_split=0.2,

    epochs=30,

    batch_size=64,

    callbacks=[early_stop],

    verbose=1

)


# ============================================
# EVALUATE
# ============================================

loss, mae = model.evaluate(

    X_test,

    y_test,

    verbose=1

)

print()

print("="*50)

print("Final Test Results")

print(f"Loss : {loss:.4f}")

print(f"MAE  : {mae:.4f}")

print("="*50)


# ============================================
# SAVE
# ============================================

MODEL_PATH = MODEL_DIR / "model.keras"

model.save(MODEL_PATH)

print()

print(f"Model saved to:\n{MODEL_PATH}")