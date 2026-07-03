# API Documentation

## Overview

The Predictive Maintenance Backend exposes REST APIs through FastAPI for accessing machine predictions, historical sensor data, alerts, and system status.

Base URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# Endpoints

---

## Health Check

### GET /

Returns the current backend status.

### Response

```json
{
    "message": "Predictive Maintenance Backend Running"
}
```

---

## Machine Prediction

### GET /prediction/{machine_id}

Predicts the current health of a machine using the latest 20 sensor readings.

### Path Parameter

| Parameter | Type | Description |
|-----------|------|-------------|
| machine_id | Integer | Machine ID |

### Example

```
GET /prediction/1
```

### Response

```json
{
  "success": true,
  "machine_id": 1,
  "prediction": {
    "health_score": 65.68,
    "failure_probability": 34.32,
    "remaining_useful_life": 131.37,
    "recommendation": "Schedule Inspection",
    "machine_id": 1,
    "predicted_fault": "Healthy"
  }
}
```

---

## Machine History

### GET /history/{machine_id}

Returns historical sensor readings for the selected machine.

### Example

```
GET /history/1
```

### Response

```json
[
    {
        "timestamp": "2026-07-03T10:25:18",
        "temperature": 74.8,
        "rpm": 1486,
        "torque": 101.2,
        "vibration": 1.84,
        "current": 11.6,
        "oil_level": 86.3
    }
]
```

---

## Active Alerts

### GET /alerts

Returns all active maintenance alerts.

### Response

```json
[
    {
        "alert_id": 1,
        "machine_id": 1,
        "severity": "Medium",
        "message": "Schedule machine inspection.",
        "created_at": "2026-07-03T10:45:20",
        "is_acknowledged": false
    }
]
```

---

# API Workflow

Digital Twin

↓

MQTT Publisher

↓

Mosquitto Broker

↓

MQTT Subscriber

↓

MySQL Database

↓

TensorFlow Prediction Engine

↓

FastAPI APIs

↓

Angular / Flutter