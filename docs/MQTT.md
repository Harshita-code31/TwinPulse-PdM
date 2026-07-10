# MQTT Communication

# PredictivePulse

### MQTT Messaging Architecture

---

# Overview

PredictivePulse uses the **MQTT (Message Queuing Telemetry Transport)** protocol as the primary communication mechanism for real-time data exchange between different components of the platform.

MQTT enables lightweight, low-latency, publish-subscribe communication, making it ideal for Industrial Internet of Things (IIoT) applications where continuous sensor streaming is required.

The platform uses **Eclipse Mosquitto** as the MQTT broker.

---

# Why MQTT?

Industrial monitoring systems require:

- Low network overhead
- Fast message delivery
- Reliable communication
- Loose coupling between components
- Scalability

MQTT satisfies these requirements by allowing producers and consumers to communicate without knowing about each other.

---

# MQTT Architecture

```text
                 Digital Twin Simulator
                          │
                          ▼
                   MQTT Publisher
                          │
                          ▼
             Eclipse Mosquitto Broker
                │                 │
                │                 │
                ▼                 ▼
      MQTT Subscriber      Flutter Mobile App
                │
                ▼
      TensorFlow Prediction Engine
                │
                ▼
        MQTT Prediction Publisher
                │
                ▼
      Eclipse Mosquitto Broker
                │
                ▼
      Flutter Mobile Application
```

---

# MQTT Topics

The platform currently uses two MQTT topics.

## Sensor Telemetry

```text
machines/sensors
```

Published by:

- MQTT Publisher

Subscribed by:

- MQTT Subscriber
- Flutter Mobile Application

---

## AI Predictions

```text
machines/predictions
```

Published by:

- MQTT Subscriber

Subscribed by:

- Flutter Mobile Application

---

# Message Flow

## Step 1

The Digital Twin Simulator generates sensor readings.

Example:

- Temperature
- RPM
- Torque
- Vibration
- Current
- Oil Level

---

## Step 2

The MQTT Publisher serializes the sensor data into JSON and publishes it to:

```text
machines/sensors
```

---

## Step 3

The MQTT Subscriber receives the telemetry.

Responsibilities:

- Parse JSON
- Store telemetry
- Trigger AI prediction
- Publish prediction results

---

## Step 4

The TensorFlow prediction engine calculates:

- Health Score
- Failure Probability
- Remaining Useful Life
- Recommendation

---

## Step 5

Prediction results are published to:

```text
machines/predictions
```

---

## Step 6

The Flutter application subscribes to both topics.

It receives:

### Live Telemetry

```text
machines/sensors
```

Displays:

- Temperature
- RPM
- Torque
- Current
- Oil Level
- Machine Health

---

### Live Predictions

```text
machines/predictions
```

Displays:

- Failure Probability
- Remaining Useful Life
- AI Recommendation

---

# JSON Payload

Example telemetry packet:

```json
{
  "machine_id": 1,
  "machine_name": "Gearbox-1",
  "machine_type": "Gearbox",
  "temperature": 61.4,
  "rpm": 1452,
  "torque": 119.8,
  "vibration": 1.25,
  "current": 6.41,
  "oil_level": 99.8,
  "health_score": 99.8,
  "fault_type": "Healthy"
}
```

---

Example prediction packet:

```json
{
  "machine_id": 1,
  "health_score": 96.45,
  "failure_probability": 3.55,
  "remaining_useful_life": 192.9,
  "recommendation": "Machine Healthy"
}
```

---

# MQTT Components

## MQTT Publisher

Responsibilities:

- Generate telemetry
- Publish sensor packets
- Simulate Digital Twins

---

## Mosquitto Broker

Responsibilities:

- Receive MQTT packets
- Route messages
- Manage subscriptions
- Deliver live updates

---

## MQTT Subscriber

Responsibilities:

- Receive telemetry
- Store sensor data
- Execute AI prediction
- Publish prediction packets

---

## Flutter MQTT Client

Responsibilities:

- Subscribe to sensor topic
- Subscribe to prediction topic
- Update dashboard in real time
- Display live machine information

---

# Communication Model

```text
Telemetry

Publisher
     │
     ▼
machines/sensors
     │
     ├────────► Subscriber
     │
     └────────► Flutter Dashboard


Predictions

Subscriber
     │
     ▼
machines/predictions
     │
     ▼
Flutter Dashboard
```

---

# Advantages of the Architecture

The MQTT-based design provides several advantages.

## Loose Coupling

Publishers and subscribers operate independently.

---

## Scalability

Additional machines and clients can be added without modifying existing components.

---

## Real-Time Monitoring

Sensor updates are immediately delivered to the Flutter application.

---

## Efficient Network Usage

Only small JSON payloads are transmitted.

---

## Extensibility

Additional MQTT clients such as web dashboards or cloud services can subscribe without changing the existing architecture.

---

# Summary

MQTT serves as the real-time communication backbone of PredictivePulse.

It connects the Digital Twin Simulator, AI prediction engine, backend services, and Flutter mobile application into a unified Industrial IoT platform capable of live monitoring and predictive maintenance.