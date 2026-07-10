# TensorFlow Prediction Engine

# PredictivePulse

---

# Overview

PredictivePulse uses a TensorFlow LSTM model to estimate the health of industrial machines using historical telemetry collected from the Digital Twin Simulator.

The model analyzes recent machine behavior and predicts future machine health rather than simply detecting current faults.

---

# Inputs

The model processes:

- Machine Type
- Operating Hours
- Machine Age
- Ambient Temperature
- Operating Load
- Temperature
- RPM
- Torque
- Vibration
- Current
- Oil Level
- Maintenance Count
- Fault Type

---

# Outputs

The model predicts:

- Health Score
- Failure Probability
- Remaining Useful Life (RUL)
- Maintenance Recommendation

---

# Prediction Workflow

```text
Sensor Data

↓

Feature Engineering

↓

Feature Scaling

↓

TensorFlow LSTM

↓

Prediction

↓

Health Score

↓

Recommendation
```

---

# Integration

After prediction:

1. Results are stored inside MySQL.
2. Prediction packets are published through MQTT.
3. Flutter receives prediction updates in real time.
4. FastAPI exposes prediction history through REST APIs.

---

# Prediction Pipeline

```text
Telemetry

↓

TensorFlow Model

↓

Prediction

├────────► MQTT

│              │

│              ▼

│        Flutter Dashboard

│

▼

MySQL

↓

FastAPI

↓

History APIs
```

---

# Summary

TensorFlow serves as the intelligence layer of PredictivePulse by transforming live telemetry into actionable maintenance insights that are simultaneously stored, published, and visualized.