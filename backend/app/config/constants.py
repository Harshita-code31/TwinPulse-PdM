"""
Application constants.
These values rarely change and are shared across the project.
"""

# Machine Status
HEALTHY = "Healthy"
WARNING = "Warning"
CRITICAL = "Critical"

# MQTT Topics
SENSOR_TOPIC = "machines/sensors"
PREDICTION_TOPIC = "machines/predictions"
ALERT_TOPIC = "machines/alerts"

# Machine Health Thresholds
HEALTHY_THRESHOLD = 80
WARNING_THRESHOLD = 50
CRITICAL_THRESHOLD = 20