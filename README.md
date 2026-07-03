# 🚀 Predictive Maintenance System

An industry-grade IoT Predictive Maintenance platform that monitors industrial machines using Digital Twins, streams sensor data through MQTT, stores telemetry in MySQL, predicts machine health using a TensorFlow LSTM model, and exposes REST APIs through FastAPI for dashboards and mobile applications.

---

# 📖 Overview

This project simulates multiple industrial machines, continuously collects sensor readings, predicts machine health using Machine Learning, estimates failure probability and remaining useful life (RUL), generates maintenance alerts, and stores historical data for analysis.

The backend is containerized using Docker and designed to integrate seamlessly with both an Angular web dashboard and a Flutter mobile application.

---

# ✨ Features

- Digital Twin Machine Simulator
- Multi-Machine Real-Time Simulation
- MQTT Communication (Mosquitto)
- FastAPI REST Backend
- TensorFlow LSTM Prediction Model
- Machine Health Prediction
- Failure Probability Estimation
- Remaining Useful Life (RUL)
- Automatic Alert Generation
- Historical Sensor Data Storage
- MySQL Database Integration
- Dockerized Backend Infrastructure
- Interactive Swagger API Documentation

---

# 🛠 Technology Stack

## Backend

- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic

## Machine Learning

- TensorFlow
- NumPy
- Pandas
- Scikit-Learn
- Joblib

## Database

- MySQL 8
- SQLAlchemy ORM

## Messaging

- MQTT
- Eclipse Mosquitto

## DevOps

- Docker
- Docker Compose

## Planned Frontend

- Angular

## Planned Mobile Application

- Flutter

---

# 🏗 System Architecture

```text
                +----------------------+
                |  Digital Twin        |
                |  Machine Simulator   |
                +----------+-----------+
                           |
                           v
                  MQTT Publisher (Local)
                           |
                           v
                  Eclipse Mosquitto (Docker)
                           |
                           v
                  MQTT Subscriber (Local)
                           |
                           v
                    MySQL Database (Docker)
                           |
                           v
                TensorFlow Prediction Engine
                           |
                           v
                  FastAPI Backend (Docker)
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
  Angular Dashboard (Planned)      Flutter App (Planned)
```

---

# 📁 Project Structure

```text
PredictiveMaintenance_V2/

│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── config/
│   │   ├── database/
│   │   ├── ml/
│   │   ├── mqtt/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── simulator/
│   │
│   ├── .env.local
│   ├── .env.docker
│   └── Dockerfile
│
├── artifacts/
│   ├── scalers/
│   └── trained_models/
│
├── data/
├── docs/
├── frontend-angular/
├── mobile-flutter/
│
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Configuration

The project uses separate environment configurations for local development and Docker deployment.

### Local Development

```
backend/.env.local
```

Used by:

- MQTT Publisher
- MQTT Subscriber

### Docker Deployment

```
backend/.env.docker
```

Used by:

- FastAPI Backend

This separation avoids conflicts between Docker networking (`mysql`, `mosquitto`) and local execution (`localhost`).

---

# 🚀 Running the Project

## 1. Clone Repository

```bash
git clone <repository-url>

cd PredictiveMaintenance_V2
```

---

## 2. Start Docker Services

```bash
docker compose up --build
```

This starts:

- MySQL
- Mosquitto MQTT Broker
- FastAPI Backend

---

## 3. Start MQTT Subscriber

```bash
cd backend

python -m app.mqtt.subscriber
```

---

## 4. Start Digital Twin Publisher

```bash
cd backend

python -m app.mqtt.publisher
```

The publisher continuously streams simulated sensor data for multiple industrial machines.

---

# 🌐 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

---

# 📡 API Endpoints

## Health Check

```
GET /
```

Returns backend status.

---

## Machine Prediction

```
GET /prediction/{machine_id}
```

Returns

- Machine Health Score
- Failure Probability
- Remaining Useful Life
- Maintenance Recommendation

---

## Sensor History

```
GET /history/{machine_id}
```

Returns historical sensor readings for a machine.

---

## Active Alerts

```
GET /alerts
```

Returns all active maintenance alerts.

---

# 🤖 Machine Learning Pipeline

```
Sensor Data

        │

        ▼

Feature Engineering

        │

        ▼

Feature Scaling

        │

        ▼

TensorFlow LSTM Model

        │

        ▼

Health Score Prediction

        │

        ├────────────► Failure Probability

        ├────────────► Remaining Useful Life

        └────────────► Maintenance Recommendation
```

---

# 🐳 Docker Services

| Service | Port |
|----------|------|
| FastAPI | 8000 |
| MySQL | 3306 |
| Mosquitto MQTT | 1883 |
| Mosquitto WebSocket | 9001 |

---

# 📊 Database Tables

- machines
- sensor_data
- predictions
- alerts

---

# 🔄 Data Flow

```
Digital Twin Machine

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

Prediction Repository

↓

FastAPI REST API

↓

Angular Dashboard (Planned)

Flutter Mobile App (Planned)
```

---

# 📌 Current Status

## Backend

- ✅ Complete

## Machine Learning

- ✅ Complete

## Database

- ✅ Complete

## Docker

- ✅ Complete

## MQTT Communication

- ✅ Complete

## REST APIs

- ✅ Complete

## Angular Dashboard

- 🚧 Planned

## Flutter Mobile Application

- 🚧 Planned

---

# 🚀 Future Enhancements

- Angular Monitoring Dashboard
- Flutter Mobile Application
- User Authentication
- Role-Based Access Control
- Predictive Maintenance Scheduling
- Email & SMS Alerts
- Real Industrial Sensor Integration
- Cloud Deployment
- CI/CD Pipeline
- Monitoring & Logging

---

# 👨‍💻 Author

**Sai Sanjanaa P R**

B.E Computer Science and Engineering (Internet of Things)

Sri Sairam Engineering College

Industrial IoT & AI Predictive Maintenance Internship Project