# Deployment Guide

## Overview

This document explains how to set up and run the Predictive Maintenance Backend for local development.

The backend consists of:

- FastAPI Backend
- MySQL Database
- Eclipse Mosquitto MQTT Broker
- MQTT Publisher
- MQTT Subscriber
- TensorFlow Prediction Engine

---

# Prerequisites

Install the following software before running the project.

## Python

Version

```
Python 3.11+
```

---

## Docker

Install Docker Desktop.

Verify installation

```bash
docker --version
docker compose version
```

---

## Git

```bash
git --version
```

---

# Clone Repository

```bash
git clone <repository-url>

cd PredictiveMaintenance_V2
```

---

# Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Files

The backend uses two environment configurations.

## Local Development

```
backend/.env.local
```

Used by

- MQTT Publisher
- MQTT Subscriber

Uses

```
localhost
```

---

## Docker

```
backend/.env.docker
```

Used by

- FastAPI

Uses

```
mysql
mosquitto
```

This separation avoids networking conflicts between Docker containers and local development.

---

# Start Backend

Start Docker services.

```bash
docker compose up --build
```

This starts

- MySQL
- Mosquitto MQTT Broker
- FastAPI Backend

---

# Start Subscriber

Open another terminal.

```bash
cd backend

python -m app.mqtt.subscriber
```

---

# Start Publisher

Open another terminal.

```bash
cd backend

python -m app.mqtt.publisher
```

The publisher continuously generates sensor data for multiple industrial machines.

---

# Swagger Documentation

Open

```
http://localhost:8000/docs
```

Available APIs

- Prediction
- History
- Alerts

---

# Verify Database

Connect

```bash
docker exec -it pdm_mysql mysql -uroot -proot
```

Use

```sql
USE predictive_maintenance;
```

Example

```sql
SELECT COUNT(*) FROM sensor_data;

SELECT * FROM predictions;

SELECT * FROM alerts;
```

---

# Docker Services

| Service | Port |
|----------|------|
| FastAPI | 8000 |
| MySQL | 3306 |
| MQTT | 1883 |
| MQTT WebSocket | 9001 |

---

# Troubleshooting

## Backend not starting

Check

```bash
docker compose logs backend
```

---

## MQTT not publishing

Verify Mosquitto is running

```bash
docker ps
```

---

## Database Connection Error

Verify

```
MySQL container is running

Port 3306 is available
```

---

# Deployment Workflow

Docker

↓

MySQL

Mosquitto

FastAPI

↓

Publisher

↓

Subscriber

↓

Machine Prediction

↓

REST APIs