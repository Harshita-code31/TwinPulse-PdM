class TelemetryModel {
  final int machineId;
  final String machineName;
  final String machineType;

  final int operatingHours;
  final int machineAge;

  final double operatingLoad;
  final double ambientTemperature;

  final double temperature;
  final int rpm;
  final double torque;
  final double vibration;
  final double current;
  final double oilLevel;

  final double healthScore;

  final String faultType;

  final int maintenanceCount;
  final int lastMaintenanceHour;

  const TelemetryModel({
    required this.machineId,
    required this.machineName,
    required this.machineType,
    required this.operatingHours,
    required this.machineAge,
    required this.operatingLoad,
    required this.ambientTemperature,
    required this.temperature,
    required this.rpm,
    required this.torque,
    required this.vibration,
    required this.current,
    required this.oilLevel,
    required this.healthScore,
    required this.faultType,
    required this.maintenanceCount,
    required this.lastMaintenanceHour,
  });

  factory TelemetryModel.fromJson(Map<String, dynamic> json) {
    return TelemetryModel(
      machineId: json["machine_id"],
      machineName: json["machine_name"],
      machineType: json["machine_type"],

      operatingHours: json["operating_hours"],
      machineAge: json["machine_age"],

      operatingLoad: (json["operating_load"] as num).toDouble(),
      ambientTemperature: (json["ambient_temperature"] as num).toDouble(),

      temperature: (json["temperature"] as num).toDouble(),
      rpm: json["rpm"],
      torque: (json["torque"] as num).toDouble(),
      vibration: (json["vibration"] as num).toDouble(),
      current: (json["current"] as num).toDouble(),
      oilLevel: (json["oil_level"] as num).toDouble(),

      healthScore: (json["health_score"] as num).toDouble(),

      faultType: json["fault_type"],

      maintenanceCount: json["maintenance_count"],
      lastMaintenanceHour: json["last_maintenance_hour"],
    );
  }
}
