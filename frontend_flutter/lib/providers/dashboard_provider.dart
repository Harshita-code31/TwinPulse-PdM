import 'package:flutter/material.dart';

import '../models/prediction_model.dart';
import '../models/telemetry_model.dart';
import '../services/mqtt_service.dart';

class DashboardProvider extends ChangeNotifier {
  final MQTTService _mqttService = MQTTService();

  /// Latest telemetry for every machine
  final Map<int, TelemetryModel> _telemetryMap = {};

  /// Latest prediction for every machine
  final Map<int, PredictionModel> _predictionMap = {};

  bool _connected = false;

  bool get isConnected => _connected;

  Map<int, TelemetryModel> get telemetryMap => _telemetryMap;

  Map<int, PredictionModel> get predictionMap => _predictionMap;

  List<TelemetryModel> get machines =>
      _telemetryMap.values.toList()
        ..sort((a, b) => a.machineId.compareTo(b.machineId));

  Future<void> initialize() async {
    await _mqttService.connect();

    _connected = true;
    notifyListeners();

    // Live telemetry updates
    _mqttService.telemetryStream.listen((telemetry) {
      _telemetryMap[telemetry.machineId] = telemetry;
      notifyListeners();
    });

    // Live prediction updates
    _mqttService.predictionStream.listen((prediction) {
      print("Prediction Received");
      print(prediction.failureProbability);

      _predictionMap[prediction.machineId] = prediction;
      notifyListeners();
    });
  }

  TelemetryModel? getTelemetry(int machineId) {
    return _telemetryMap[machineId];
  }

  PredictionModel? getPrediction(int machineId) {
    return _predictionMap[machineId];
  }

  void disconnect() {
    _mqttService.disconnect();

    _connected = false;

    notifyListeners();
  }

  @override
  void dispose() {
    disconnect();
    super.dispose();
  }
}
