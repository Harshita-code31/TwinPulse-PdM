import 'dart:async';
import 'dart:convert';

import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';

import '../models/prediction_model.dart';
import '../models/telemetry_model.dart';

class MQTTService {
  static final MQTTService _instance = MQTTService._internal();

  factory MQTTService() => _instance;

  MQTTService._internal();

  late MqttServerClient client;

  final StreamController<TelemetryModel> _telemetryController =
      StreamController<TelemetryModel>.broadcast();

  final StreamController<PredictionModel> _predictionController =
      StreamController<PredictionModel>.broadcast();

  Stream<TelemetryModel> get telemetryStream => _telemetryController.stream;

  Stream<PredictionModel> get predictionStream => _predictionController.stream;

  Future<void> connect() async {
    // Android Emulator
    client = MqttServerClient('10.0.2.2', 'flutter_client');

    // If using a physical phone, replace with your PC's IP
    // Example:
    // client = MqttServerClient("192.168.1.100", "flutter_client");

    client.port = 1883;
    client.keepAlivePeriod = 20;
    client.autoReconnect = true;
    client.logging(on: false);

    client.onConnected = _onConnected;
    client.onDisconnected = _onDisconnected;
    client.onSubscribed = _onSubscribed;

    client.connectionMessage = MqttConnectMessage()
        .withClientIdentifier('flutter_client')
        .startClean()
        .withWillQos(MqttQos.atLeastOnce);

    try {
      await client.connect();
    } catch (e) {
      print("MQTT Connection Error: $e");
      disconnect();
      return;
    }

    if (client.connectionStatus?.state != MqttConnectionState.connected) {
      print("MQTT Failed to connect");
      disconnect();
      return;
    }

    client.updates?.listen(_onMessage);
  }

  void _onConnected() {
    print("MQTT Connected");

    client.subscribe("machines/sensors", MqttQos.atLeastOnce);

    client.subscribe("machines/predictions", MqttQos.atLeastOnce);
  }

  void _onDisconnected() {
    print("MQTT Disconnected");
  }

  void _onSubscribed(String topic) {
    print("Subscribed -> $topic");
  }

  void _onMessage(List<MqttReceivedMessage<MqttMessage>> events) {
    final recMess = events.first.payload as MqttPublishMessage;

    final payload = MqttPublishPayload.bytesToStringAsString(
      recMess.payload.message,
    );

    final topic = events.first.topic;

    try {
      final jsonMap = jsonDecode(payload);

      if (topic == "machines/sensors") {
        _telemetryController.add(TelemetryModel.fromJson(jsonMap));
      } else if (topic == "machines/predictions") {
        _predictionController.add(PredictionModel.fromJson(jsonMap));
      }
    } catch (e) {
      print("MQTT Parse Error: $e");
    }
  }

  void disconnect() {
    if (client.connectionStatus?.state == MqttConnectionState.connected) {
      client.disconnect();
    }
  }

  void dispose() {
    _telemetryController.close();
    _predictionController.close();
    disconnect();
  }
}
