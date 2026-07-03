import csv
import random
from pathlib import Path
from datetime import datetime, timedelta

from app.simulator.machine import Machine


# ==========================================================
# CONFIGURATION
# ==========================================================

TOTAL_MACHINES = 50
CYCLES_PER_MACHINE = 2500

ROOT_DIR = Path(__file__).resolve().parents[3]

OUTPUT_DIR = ROOT_DIR / "data" / "training"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "predictive_maintenance_dataset.csv"


# ==========================================================
# MACHINE TYPES
# ==========================================================

MACHINE_TYPES = [
    "Gearbox",
    "Motor",
    "Pump",
    "Compressor",
    "Cooling Fan"
]


FAULT_MAP = {
    "Gearbox": "Gear Wear",
    "Motor": "Motor Overload",
    "Pump": "Lubrication Failure",
    "Compressor": "Bearing Wear",
    "Cooling Fan": "Shaft Misalignment"
}


# ==========================================================
# MACHINE CREATION
# ==========================================================

def create_machine(machine_id: int):

    machine_type = random.choice(MACHINE_TYPES)

    machine = Machine(
        machine_id=machine_id,
        machine_name=f"{machine_type}-{machine_id}",
        machine_type=machine_type
    )

    machine.current_fault = "Healthy"

    machine.health_score = random.uniform(95, 100)

    machine.operating_load = random.uniform(40, 95)

    machine.ambient_temperature = random.uniform(24, 38)

    return machine


# ==========================================================
# LABEL GENERATION
# ==========================================================

def calculate_failure_probability(machine):

    probability = (
        (100 - machine.health_score) * 0.70
        + machine.vibration * 4
        + (100 - machine.oil_level) * 0.10
    )

    probability = max(0, min(probability, 100))

    return round(probability, 2)


def calculate_rul(machine):

    rul = (
        machine.health_score * 3
        - machine.machine_age * 5
    )

    return max(round(rul, 2), 0)


# ==========================================================
# DATASET GENERATION
# ==========================================================

def generate_dataset():

    fieldnames = [
        "timestamp",
        "machine_id",
        "machine_name",
        "machine_type",
        "operating_hours",
        "machine_age",
        "ambient_temperature",
        "operating_load",
        "temperature",
        "rpm",
        "torque",
        "vibration",
        "current",
        "oil_level",
        "health_score",
        "fault_type",
        "maintenance_count",
        "failure_probability",
        "remaining_useful_life",
    ]

    start_time = datetime(2026, 1, 1, 8, 0, 0)

    with open(OUTPUT_FILE, "w", newline="") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for machine_id in range(1, TOTAL_MACHINES + 1):

            machine = create_machine(machine_id)

            primary_fault = FAULT_MAP[machine.machine_type]

            print(
                f"Generating Machine {machine_id}/{TOTAL_MACHINES} ({machine.machine_type})..."
            )

            for cycle in range(CYCLES_PER_MACHINE):

                # -----------------------------
                # Controlled fault progression
                # -----------------------------

                if cycle < 500:

                    machine.current_fault = "Healthy"

                elif cycle < 1200:

                    machine.current_fault = primary_fault

                elif cycle < 1800:

                    machine.current_fault = "Critical"

                elif cycle < 2200:

                    machine.current_fault = "Failure"

                else:

                    machine.current_fault = "Healthy"

                    if machine.health_score < 90:

                        machine.health_score = 95

                        machine.maintenance_count += 1

                        machine.temperature = 60

                        machine.rpm = 1450

                        machine.torque = 120

                        machine.vibration = 1.2

                        machine.current = 6.5

                        machine.oil_level = 100

                machine.update()

                timestamp = start_time + timedelta(minutes=cycle)

                writer.writerow(
                    {
                        "timestamp": timestamp,

                        "machine_id": machine.machine_id,

                        "machine_name": machine.machine_name,

                        "machine_type": machine.machine_type,

                        "operating_hours": machine.operating_hours,

                        "machine_age": machine.machine_age,

                        "ambient_temperature": round(machine.ambient_temperature, 2),

                        "operating_load": round(machine.operating_load, 2),

                        "temperature": round(machine.temperature, 2),

                        "rpm": machine.rpm,

                        "torque": round(machine.torque, 2),

                        "vibration": round(machine.vibration, 3),

                        "current": round(machine.current, 3),

                        "oil_level": round(machine.oil_level, 2),

                        "health_score": round(machine.health_score, 2),

                        "fault_type": machine.current_fault,

                        "maintenance_count": machine.maintenance_count,

                        "failure_probability": calculate_failure_probability(machine),

                        "remaining_useful_life": calculate_rul(machine),
                    }
                )

# ==========================================================
# MAIN
# ==========================================================

def main():

    print("=" * 60)
    print("Predictive Maintenance Dataset Generator")
    print("=" * 60)
    print(f"Machines           : {TOTAL_MACHINES}")
    print(f"Cycles / Machine   : {CYCLES_PER_MACHINE}")
    print(f"Expected Rows      : {TOTAL_MACHINES * CYCLES_PER_MACHINE:,}")
    print()

    generate_dataset()

    print()
    print("=" * 60)
    print("Dataset Generation Complete!")
    print(f"Saved to : {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
    