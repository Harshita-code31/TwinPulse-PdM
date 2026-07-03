# System Architecture

## Overview

The Predictive Maintenance System is designed to simulate industrial machines, collect telemetry using MQTT, store sensor readings in MySQL, perform machine learning predictions using TensorFlow, and expose the results through FastAPI.

---

# High Level Architecture

```
                   +-----------------------+
                   | Digital Twin Machines |
                   +-----------+-----------+
                               |
                               |
                     MQTT Publisher
                               |
                               |
                     Eclipse Mosquitto
                               |
                               |
                     MQTT Subscriber
                               |
                               |
                          MySQL Database
                               |
                               |
                    TensorFlow Prediction
                               |
                               |
                          FastAPI Backend
                               |
               +---------------+---------------+
               |                               |
        Angular Dashboard              Flutter App
```

---

# Components

## Digital Twin

Simulates multiple industrial machines by continuously generating realistic sensor readings.

---

## MQTT Publisher

Publishes sensor readings from all simulated machines to the MQTT broker.

Topic

```
machines/sensors
```

---

## Mosquitto Broker

Acts as the communication layer between publishers and subscribers.

Responsibilities

- Receive MQTT messages
- Forward messages
- Decouple data producers and consumers

---

## MQTT Subscriber

Receives sensor data and stores it into MySQL.

Responsibilities

- Subscribe to MQTT topic
- Parse JSON payload
- Save data into database

---

## MySQL

Stores

- Machines
- Sensor History
- Predictions
- Alerts

---

## TensorFlow Prediction Engine

Uses the latest twenty sensor readings to estimate

- Health Score
- Failure Probability
- Remaining Useful Life
- Maintenance Recommendation

---

## FastAPI

Provides REST APIs for frontend applications.

Responsibilities

- Prediction API
- History API
- Alerts API
- Swagger Documentation

---

# Data Flow

Digital Twin

↓

Publisher

↓

Mosquitto

↓

Subscriber

↓

Sensor Repository

↓

MySQL

↓

Prediction Service

↓

TensorFlow Model

↓

Prediction Repository

↓

REST APIs

↓

Angular / Flutter

---

# Technology Stack

Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

Database

- MySQL

Machine Learning

- TensorFlow
- NumPy
- Pandas
- Scikit-Learn

Messaging

- MQTT
- Mosquitto

Deployment

- Docker
- Docker Compose