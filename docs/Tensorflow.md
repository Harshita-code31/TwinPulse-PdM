# TensorFlow Prediction Engine

## Overview

The Predictive Maintenance System uses a TensorFlow LSTM model to predict machine health using historical sensor readings.

The model estimates

- Machine Health Score
- Failure Probability
- Remaining Useful Life (RUL)
- Maintenance Recommendation

---

# Input Features

The prediction model uses the latest twenty sensor readings.

Features

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

# Preprocessing Pipeline

Raw Sensor Data

↓

Label Encoding

↓

Feature Scaling

↓

Tensor Conversion

↓

TensorFlow LSTM

↓

Prediction

---

# Encoders

Categorical Features

- Machine Type
- Fault Type

These are converted into numerical values using trained Label Encoders.

---

# Feature Scaling

Numerical features are normalized using a trained Standard Scaler.

This ensures consistent input to the neural network.

---

# TensorFlow Model

Framework

```
TensorFlow
```

Model Type

```
LSTM Neural Network
```

Input

```
20 consecutive sensor readings
```

Output

```
Health Score
```

---

# Health Score

Range

```
0 - 100
```

Higher value

```
Better machine condition
```

Lower value

```
Poor machine health
```

---

# Failure Probability

Calculated as

```
100 - Health Score
```

Example

Health Score

```
82
```

Failure Probability

```
18%
```

---

# Remaining Useful Life

Estimated using the predicted health score.

Current Formula

```
Health Score × 2
```

Future versions may replace this heuristic with a dedicated RUL prediction model.

---

# Recommendation Engine

Health Score ≥ 90

```
Machine Healthy
```

Health Score ≥ 70

```
Monitor Machine
```

Health Score ≥ 50

```
Schedule Inspection
```

Health Score ≥ 30

```
Maintenance Required
```

Health Score < 30

```
Immediate Shutdown Recommended
```

---

# Prediction Workflow

Latest Sensor Readings

↓

Repository

↓

Prediction Service

↓

Preprocessing

↓

TensorFlow Model

↓

Prediction

↓

Prediction Repository

↓

Alert Generation

↓

REST API

---

# Future Improvements

- Real Remaining Useful Life Model
- Online Model Retraining
- Fault Classification
- Explainable AI (XAI)
- Confidence Scores
- Edge AI Deployment

---

# Summary

The TensorFlow Prediction Engine forms the core intelligence of the Predictive Maintenance System by continuously evaluating machine health and providing actionable maintenance insights from real-time industrial sensor data.