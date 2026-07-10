# Deployment Guide

# PredictivePulse

### Industrial AI Predictive Maintenance Platform

---

# Overview

This document explains how to deploy and run the complete PredictivePulse platform in a local development environment.

The platform consists of:

- Dockerized Backend
- MySQL Database
- Eclipse Mosquitto MQTT Broker
- TensorFlow Prediction Engine
- FastAPI REST APIs
- MQTT Publisher
- MQTT Subscriber
- Flutter Mobile Application

---

# System Requirements

## Software

- Python 3.11+
- Flutter SDK
- Docker Desktop
- Git

---

## Python Packages

Install the project dependencies:

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
PredictiveMaintenance_V2/

├── backend/
├── frontend_flutter/
├── artifacts/
├── docs/
├── data/
├── docker-compose.yml
└── requirements.txt
```

---

# Environment Configuration

Two environment files are used.

## Local Development

```text
backend/.env.local
```

Used by:

- MQTT Publisher
- MQTT Subscriber

---

## Docker Deployment

```text
backend/.env.docker
```

Used by:

- FastAPI Backend

---

# Step 1 — Clone Repository

```bash
git clone <repository-url>

cd PredictiveMaintenance_V2
```

---

# Step 2 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 3 — Start Docker Services

Launch all backend containers.

```bash
docker compose up -d
```

Verify the running containers.

```bash
docker ps
```

Expected containers:

- pdm_backend
- pdm_mysql
- pdm_mosquitto

---

# Step 4 — Verify Backend

Open the Swagger interface.

```text
http://localhost:8000/docs
```

If Swagger loads successfully, the FastAPI backend is operational.

---

# Step 5 — Start MQTT Subscriber

Open a terminal.

```bash
cd backend

python -m app.mqtt.subscriber
```

The subscriber will:

- Listen for MQTT telemetry
- Store sensor data
- Run AI prediction
- Publish prediction results

---

# Step 6 — Start Digital Twin Simulator

Open another terminal.

```bash
cd backend

python -m app.mqtt.publisher
```

The simulator continuously generates telemetry for multiple industrial machines.

---

# Step 7 — Launch Flutter Application

Open a new terminal.

```bash
cd frontend_flutter

flutter pub get

flutter run
```

---

# Physical Android Device

When testing on a physical Android device:

Replace

```dart
10.0.2.2
```

with

```text
YOUR_PC_IP
```

inside

```text
lib/services/mqtt_service.dart
```

and

```text
lib/services/api_service.dart
```

Ensure:

- Laptop and phone are connected to the same Wi-Fi network.
- FastAPI is running using:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Windows Firewall should allow incoming connections on the local network.

---

# Runtime Sequence

The recommended startup order is:

```text
1. Docker Containers

2. FastAPI Backend

3. MQTT Subscriber

4. MQTT Publisher

5. Flutter Application
```

---

# Docker Services

| Service | Port |
|----------|------|
| FastAPI | 8000 |
| MySQL | 3306 |
| Mosquitto MQTT | 1883 |
| Mosquitto WebSocket | 9001 |

---

# Verification Checklist

After deployment, verify the following:

✅ Docker containers are running

✅ FastAPI Swagger is accessible

✅ MQTT Subscriber receives telemetry

✅ Digital Twin publishes sensor data

✅ TensorFlow predictions are generated

✅ Flutter dashboard connects successfully

✅ Live machine telemetry updates

✅ History API returns records

✅ Alerts API returns active alerts

---

# Troubleshooting

## MQTT Connection Failed

Verify:

- Mosquitto container is running.
- MQTT broker address is correct.
- Port 1883 is accessible.

---

## FastAPI Not Reachable

Verify:

- Docker container is running.
- Port 8000 is available.
- Swagger loads successfully.

---

## Flutter Shows No Live Data

Check:

- MQTT Publisher is running.
- MQTT Subscriber is running.
- Flutter is connected to the correct MQTT broker.
- Physical devices use the laptop's local IP address instead of `10.0.2.2`.

---

## Database Connection Error

Verify:

- MySQL container is running.
- Environment variables are correct.
- Database credentials match the Docker configuration.

---

# Deployment Summary

The PredictivePulse deployment consists of:

- Digital Twin Simulator
- MQTT Messaging
- TensorFlow Prediction Engine
- MySQL Database
- FastAPI Backend
- Flutter Mobile Application

Together, these components create a complete end-to-end Industrial AI Predictive Maintenance platform capable of real-time monitoring, predictive analytics, and mobile visualization.