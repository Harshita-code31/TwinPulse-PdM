# Project Overview

# PredictivePulse

### Industrial AI Predictive Maintenance Platform

---

## Introduction

PredictivePulse is an end-to-end Industrial Internet of Things (IIoT) Predictive Maintenance Platform developed to demonstrate how modern industrial systems can leverage Digital Twins, Artificial Intelligence, MQTT messaging, cloud-ready microservices, and mobile applications to monitor machine health in real time.

The platform continuously simulates multiple industrial machines, streams live telemetry through MQTT, predicts machine health using a TensorFlow LSTM model, stores operational data in MySQL, exposes REST APIs through FastAPI, and visualizes the entire system using a Flutter mobile application.

Rather than focusing on individual components, PredictivePulse demonstrates a complete industrial data pipeline from sensor generation to AI-driven maintenance recommendations.

---

# Objectives

The primary objectives of the project are:

- Simulate an industrial production environment using Digital Twins.
- Stream machine telemetry using MQTT.
- Store historical machine data for analysis.
- Predict machine health using Artificial Intelligence.
- Estimate Remaining Useful Life (RUL).
- Generate maintenance recommendations.
- Provide live industrial monitoring through a mobile application.
- Demonstrate a production-style software architecture using modern technologies.

---

# System Workflow

The PredictivePulse workflow consists of six major stages.

## Stage 1 — Digital Twin Simulation

The platform begins by simulating multiple industrial machines.

Each Digital Twin continuously generates realistic operational parameters including:

- Temperature
- RPM
- Torque
- Vibration
- Current
- Oil Level
- Operating Hours
- Ambient Temperature
- Operating Load

The simulator also introduces fault conditions to emulate real-world industrial scenarios.

---

## Stage 2 — Real-Time Communication

Generated telemetry is transmitted through the MQTT protocol using Eclipse Mosquitto.

MQTT provides lightweight, low-latency communication between different components of the platform while decoupling data producers from consumers.

Topics used include:

```text
machines/sensors
machines/predictions
```

---

## Stage 3 — Data Processing

The MQTT Subscriber receives incoming telemetry and performs the following operations:

- Parses sensor payloads
- Stores telemetry into MySQL
- Triggers AI prediction
- Publishes prediction results back to MQTT

This ensures both historical persistence and live data availability.

---

## Stage 4 — Artificial Intelligence

Historical telemetry is processed by a TensorFlow LSTM model trained to estimate machine health.

The prediction engine generates:

- Health Score
- Failure Probability
- Remaining Useful Life (RUL)
- Maintenance Recommendation

Prediction results are stored in the database and simultaneously published to MQTT.

---

## Stage 5 — Backend Services

FastAPI provides REST APIs that expose platform data to external applications.

Available services include:

- Machine History
- Active Alerts
- Machine Predictions
- Health Check
- Swagger Documentation

These APIs enable reliable retrieval of historical and analytical information.

---

## Stage 6 — Flutter Mobile Dashboard

The Flutter application serves as the primary user interface for the platform.

The dashboard combines two communication mechanisms.

### MQTT

Used for:

- Live telemetry
- Real-time AI predictions

### REST APIs

Used for:

- Machine History
- Active Alerts

This hybrid architecture ensures low-latency updates while maintaining access to historical information.

---

# Key Capabilities

PredictivePulse demonstrates the following industrial capabilities:

- Real-Time Machine Monitoring
- AI-Based Predictive Maintenance
- Historical Data Analysis
- Remaining Useful Life Estimation
- Maintenance Recommendation Generation
- Live MQTT Communication
- REST API Integration
- Mobile-Based Fleet Monitoring
- Dockerized Deployment

---

# Software Architecture

The project follows a modular architecture consisting of independent services.

```text
Digital Twin
      │
      ▼
MQTT Publisher
      │
      ▼
Mosquitto Broker
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Subscriber  Flutter App
 │
 ▼
TensorFlow
 │
 ▼
MySQL
 │
 ▼
FastAPI
```

This separation of responsibilities makes the platform scalable, maintainable, and easy to extend.

---

# Current Project Status

| Module | Status |
|----------|--------|
| Digital Twin Simulator | ✅ Complete |
| MQTT Communication | ✅ Complete |
| FastAPI Backend | ✅ Complete |
| TensorFlow Prediction Engine | ✅ Complete |
| MySQL Integration | ✅ Complete |
| Docker Deployment | ✅ Complete |
| Flutter Mobile Application | ✅ Complete |
| End-to-End Integration | ✅ Complete |

---

# Future Scope

Potential future enhancements include:

- Angular Web Dashboard
- User Authentication
- Role-Based Access Control
- Push Notifications
- Cloud Deployment
- Industrial PLC Integration
- Advanced Predictive Analytics
- Automated Maintenance Scheduling
- CI/CD Pipeline
- Real Industrial Sensor Integration

---

# Conclusion

PredictivePulse demonstrates how Digital Twins, MQTT, Machine Learning, REST APIs, Docker, and Flutter can be combined into a unified Industrial IoT platform capable of monitoring equipment, predicting failures, and supporting data-driven maintenance decisions.

The project reflects a production-oriented software architecture and provides a strong foundation for future industrial automation and predictive maintenance solutions.