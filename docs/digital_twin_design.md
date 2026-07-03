# Predictive Maintenance Digital Twin Design

## Objective

Simulate realistic industrial machine behavior by generating sensor data that follows actual degradation patterns instead of random values.

---

# Machine Life Cycle

NEW
↓

HEALTHY
↓

EARLY WARNING
↓

WARNING
↓

CRITICAL
↓

FAILURE

↓

MAINTENANCE

↓

HEALTHY (Recovered)

---

# Machine Properties

Machine ID

Machine Name

Machine Type

Machine Age

Operating Hours

Current Health Score

Operating Load

Ambient Temperature

Maintenance History

Current Fault

---

# Sensors

Temperature (°C)

RPM

Torque (Nm)

Current (A)

Oil Level (%)

Vibration (mm/s)

---

# Health Score

100 → Brand New

80 → Healthy

60 → Warning

40 → Critical

20 → Near Failure

0 → Failure

---

# Operating Load

Idle

25%

50%

75%

100%

120% (Overload)

---

# Environment

Summer

Winter

High Humidity

Dusty Environment

---

# Fault Types

Healthy

Bearing Wear

Lubrication Failure

Motor Overload

Shaft Misalignment

Gear Wear

Sensor Failure

Catastrophic Failure

---

# Recommendation Engine

Each fault must produce

Priority

Recommendation

Estimated Downtime

Maintenance Type

Expected Recovery

---

# Prediction Targets

Health Score

Failure Probability

Remaining Useful Life

Fault Type

Recommendation