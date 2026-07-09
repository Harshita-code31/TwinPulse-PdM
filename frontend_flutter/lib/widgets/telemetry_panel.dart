import 'package:flutter/material.dart';

import '../core/theme/app_theme.dart';

class TelemetryPanel extends StatelessWidget {
  final bool isConnected;

  final String machineName;
  final double healthScore;

  final String mqttStatus;
  final String aiStatus;
  final String databaseStatus;

  final String lastSync;

  const TelemetryPanel({
    super.key,
    required this.isConnected,
    required this.machineName,
    required this.healthScore,
    required this.mqttStatus,
    required this.aiStatus,
    required this.databaseStatus,
    required this.lastSync,
  });

  Widget _statusRow(String title, String value, Color color) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        children: [
          Container(
            width: 8,
            height: 8,
            decoration: BoxDecoration(color: color, shape: BoxShape.circle),
          ),

          const SizedBox(width: 12),

          Expanded(
            child: Text(
              title,
              style: TextStyle(
                color: AppTheme.textSecondary,
                letterSpacing: 1.1,
                fontSize: 12,
              ),
            ),
          ),

          Text(
            value,
            style: const TextStyle(
              fontWeight: FontWeight.bold,
              letterSpacing: 1,
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),

      padding: const EdgeInsets.all(22),

      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: AppTheme.primary.withOpacity(.25)),
      ),

      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                isConnected ? Icons.wifi : Icons.wifi_off,
                size: 18,
                color: isConnected ? Colors.green : Colors.red,
              ),

              const SizedBox(width: 10),

              Text(
                machineName.toUpperCase(),
                style: const TextStyle(
                  fontWeight: FontWeight.bold,
                  letterSpacing: 2,
                ),
              ),
            ],
          ),

          const SizedBox(height: 18),

          Text(
            "${healthScore.toStringAsFixed(0)}%",
            style: const TextStyle(
              fontSize: 68,
              fontWeight: FontWeight.bold,
              height: 1,
            ),
          ),

          const SizedBox(height: 6),

          Text(
            "HEALTH SCORE",
            style: TextStyle(
              color: AppTheme.primary,
              fontWeight: FontWeight.bold,
              letterSpacing: 1.3,
            ),
          ),

          const SizedBox(height: 18),

          Divider(color: Colors.white.withOpacity(.08)),

          const SizedBox(height: 12),

          _statusRow("MQTT BROKER", mqttStatus, Colors.green),

          _statusRow("AI ENGINE", aiStatus, Colors.blue),

          _statusRow("DATABASE", databaseStatus, Colors.green),

          _statusRow("LAST SYNC", lastSync, Colors.white),
        ],
      ),
    );
  }
}
