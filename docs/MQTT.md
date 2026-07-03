# MQTT Communication

## Overview

The Predictive Maintenance System uses MQTT to transmit sensor readings from simulated industrial machines to the backend.

MQTT provides lightweight, real-time communication between publishers and subscribers.

---

# Architecture

```
Digital Twin

↓

Publisher

↓

Mosquitto Broker

↓

Subscriber

↓

Database
```

---

# MQTT Broker

Broker

```
Eclipse Mosquitto
```

Runs inside Docker.

Default Port

```
1883
```

---

# MQTT Topic

```
machines/sensors
```

All sensor data is published to this topic.

---

# Publisher

Responsibilities

- Simulate industrial machines
- Generate sensor readings
- Publish JSON payloads
- Repeat continuously

---

# Subscriber

Responsibilities

- Subscribe to MQTT topic
- Receive JSON payload
- Parse sensor readings
- Save to MySQL

---

# JSON Payload

Example

```json
{
    "machine_id": 1,
    "machine_type": "Gearbox",
    "temperature": 72.4,
    "rpm": 1492,
    "torque": 98.6,
    "vibration": 1.74,
    "current": 11.2,
    "oil_level": 88.3,
    "operating_hours": 520,
    "machine_age": 4,
    "ambient_temperature": 31,
    "operating_load": 67,
    "maintenance_count": 2,
    "fault_type": "Healthy",
    "timestamp": "2026-07-03T10:20:14"
}
```

---

# Communication Flow

Machine

↓

Publisher

↓

MQTT Topic

↓

Mosquitto

↓

Subscriber

↓

Sensor Repository

↓

MySQL

---

# Advantages of MQTT

- Lightweight
- Low latency
- Publish/Subscribe architecture
- Supports multiple machines
- Easy integration with IoT devices

---

# Future Improvements

- MQTT Authentication
- QoS Levels
- TLS Encryption
- Cloud MQTT Broker
- Device Authentication

---

# Summary

MQTT acts as the communication layer between Digital Twin machines and the backend database, enabling scalable and real-time industrial data streaming.