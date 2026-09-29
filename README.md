# 🚀 TwinPulse-PdM

### Industrial Digital Twin & Predictive Maintenance

TwinPulse-PdM is an end-to-end Industrial IoT Predictive Maintenance Platform that combines Digital Twin simulation, MQTT messaging, TensorFlow-based machine learning, FastAPI services, MySQL data storage, Dockerized deployment, and a Flutter mobile application for real-time industrial monitoring.

The platform continuously simulates industrial machines, streams live telemetry through MQTT, predicts machine health using an LSTM model, estimates failure probability and Remaining Useful Life (RUL), stores historical sensor data, generates maintenance alerts, and visualizes the entire system through a live mobile dashboard.

## Origin and development status

TwinPulse-PdM builds on [PredictivePulse-IIoT](https://github.com/Saisanjanaa06/PredictivePulse-IIoT) by **Sai Sanjanaa P R**. The original Git history, author attribution, and [MIT license](LICENSE) are preserved.

This version includes ongoing Docker, simulation, prediction-response, and preprocessing changes. The preprocessing pipeline now produces 12 input features, while inference still expects 13; training and inference alignment and model retraining remain unfinished. Existing completion claims below describe the inherited project and are not verification of this version.

Local environment files must be supplied separately and must not be committed.

---

# 📖 Project Overview

TwinPulse-PdM was developed as an industry-oriented Predictive Maintenance solution capable of simulating real industrial equipment and demonstrating a complete IIoT pipeline from sensor generation to AI-driven maintenance recommendations.

The project integrates multiple technologies into a single production-style architecture including:

- Digital Twin Simulation
- MQTT Communication
- TensorFlow Machine Learning
- FastAPI REST Services
- MySQL Database
- Docker Containers
- Flutter Mobile Dashboard

---

# ✨ Features

## Industrial Simulation

- Digital Twin Machine Simulator
- Multi-Machine Real-Time Simulation
- Live Sensor Data Generation
- Fault Injection Engine

## Artificial Intelligence

- TensorFlow LSTM Health Prediction
- Failure Probability Estimation
- Remaining Useful Life (RUL)
- Maintenance Recommendation Engine

## Backend

- FastAPI REST APIs
- MQTT Publisher & Subscriber
- MySQL Database Integration
- Historical Sensor Storage
- Alert Generation
- Swagger API Documentation

## Mobile Application

- Flutter Dashboard
- Live Fleet Monitoring
- Machine Details
- AI Predictions
- History Viewer
- Alerts
- System Status
- MQTT Live Updates

## Infrastructure

- Dockerized Deployment
- Mosquitto MQTT Broker
- MySQL Database
- Containerized Backend

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

## Mobile Application

- Flutter
- Provider
- MQTT Client
- HTTP REST API

## DevOps

- Docker
- Docker Compose

---

# 🏗 System Architecture

```text
                     Digital Twin Simulator
                              │
                              ▼
                      MQTT Publisher
                              │
                              ▼
                   Mosquitto MQTT Broker
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
          ▼                                       ▼
  MQTT Subscriber                         Flutter App
          │                           (Live MQTT Updates)
          │                                       ▲
          ▼                                       │
 TensorFlow Prediction Engine                     │
          │                                       │
          ▼                                       │
      MySQL Database ───────────────► FastAPI REST APIs
                                             │
                                             ▼
                               History • Alerts • Predictions
```

---

# 📂 Project Structure

```text
TwinPulse-PdM/

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
├── frontend_flutter/
│   ├── android/
│   ├── ios/
│   ├── lib/
│   ├── web/
│   ├── pubspec.yaml
│   └── analysis_options.yaml
│
├── artifacts/
├── data/
├── docs/
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Environment Configuration

The project uses separate configurations for local development and Docker deployment.

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

---

# 🚀 Running the Project

## 1. Clone Repository

```bash
git clone https://github.com/Harshita-code31/TwinPulse-PdM.git

cd TwinPulse-PdM
```

---

## 2. Start Docker

```bash
docker compose up -d
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

---

## 5. Launch Flutter Application

```bash
cd frontend_flutter

flutter pub get

flutter run
```

---

# 📱 Flutter Application

The mobile application provides real-time monitoring of the industrial fleet.

### Screens

- Splash Screen
- Fleet Dashboard
- Machine Details
- AI Predictions
- Sensor History
- Alerts
- System Status

---

# 🌐 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

---

# 📡 REST API Endpoints

## Health Check

```
GET /
```

---

## Machine Prediction

```
GET /prediction/{machine_id}
```

Returns

- Health Score
- Failure Probability
- Remaining Useful Life
- Recommendation

---

## Sensor History

```
GET /history/{machine_id}
```

---

## Active Alerts

```
GET /alerts
```

---

# 🤖 Machine Learning Pipeline

```text
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
      ├────────► Failure Probability
      ├────────► Remaining Useful Life
      └────────► Maintenance Recommendation
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

# 🗄 Database Tables

- machines
- sensor_data
- predictions
- alerts

---

# 🔄 Data Flow

```text
Digital Twin Simulator
        │
        ▼
MQTT Publisher
        │
        ▼
Mosquitto Broker
        │
        ▼
MQTT Subscriber
        │
        ▼
TensorFlow Prediction Engine
        │
        ▼
MySQL Database
        │
        ▼
FastAPI REST API
        │
        ├────────► Flutter Dashboard (REST)
        │
        └────────► History & Alerts APIs

MQTT Broker
        │
        ▼
Flutter Live Dashboard (MQTT)
```

---

# 📊 Current Project Status

| Module | Status |
|---------|--------|
| Backend | ✅ Complete |
| Digital Twin Simulator | ✅ Complete |
| Machine Learning | ✅ Complete |
| MQTT Communication | ✅ Complete |
| FastAPI APIs | ✅ Complete |
| MySQL Database | ✅ Complete |
| Docker Deployment | ✅ Complete |
| Flutter Mobile App | ✅ Complete |
| End-to-End Integration | ✅ Complete |

---

# 🚀 Future Enhancements

- Angular Web Dashboard
- User Authentication
- Role-Based Access Control
- Push Notifications
- Predictive Maintenance Scheduling
- Cloud Deployment (AWS / Azure)
- Real Industrial PLC Integration
- CI/CD Pipeline
- Monitoring & Logging
- Conveyor Model Retraining

---

# Repository Owner

**Harshita Gupta** ([Harshita-code31](https://github.com/Harshita-code31))

Repository owner and maintainer of TwinPulse-PdM — Industrial Digital Twin & Predictive Maintenance.
