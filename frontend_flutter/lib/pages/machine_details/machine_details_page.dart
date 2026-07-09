import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../providers/dashboard_provider.dart';

class MachineDetailsPage extends StatelessWidget {
  final int machineId;

  const MachineDetailsPage({super.key, required this.machineId});

  Widget metric(String title, String value) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xff171B24),
        borderRadius: BorderRadius.circular(14),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            value,
            style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 4),
          Text(title, style: const TextStyle(color: Colors.white54)),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<DashboardProvider>();

    final telemetry = provider.getTelemetry(machineId);

    final prediction = provider.getPrediction(machineId);

    if (telemetry == null) {
      return Scaffold(
        appBar: AppBar(),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      appBar: AppBar(title: Text(telemetry.machineName)),

      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),

        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,

          children: [
            Text(
              telemetry.machineType,
              style: const TextStyle(fontSize: 16, color: Colors.white70),
            ),

            const SizedBox(height: 24),

            Row(
              children: [
                Expanded(
                  child: metric(
                    "Health",
                    "${telemetry.healthScore.toStringAsFixed(0)}%",
                  ),
                ),

                const SizedBox(width: 12),

                Expanded(child: metric("Fault", telemetry.faultType)),
              ],
            ),

            const SizedBox(height: 16),

            Row(
              children: [
                Expanded(
                  child: metric(
                    "Temperature",
                    "${telemetry.temperature.toStringAsFixed(1)} °C",
                  ),
                ),

                const SizedBox(width: 12),

                Expanded(child: metric("RPM", telemetry.rpm.toString())),
              ],
            ),

            const SizedBox(height: 16),

            Row(
              children: [
                Expanded(
                  child: metric("Torque", telemetry.torque.toStringAsFixed(1)),
                ),

                const SizedBox(width: 12),

                Expanded(
                  child: metric(
                    "Current",
                    telemetry.current.toStringAsFixed(2),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 16),

            Row(
              children: [
                Expanded(
                  child: metric(
                    "Oil Level",
                    "${telemetry.oilLevel.toStringAsFixed(0)}%",
                  ),
                ),

                const SizedBox(width: 12),

                Expanded(
                  child: metric(
                    "Vibration",
                    telemetry.vibration.toStringAsFixed(2),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 16),

            Row(
              children: [
                Expanded(
                  child: metric(
                    "Operating Hours",
                    telemetry.operatingHours.toString(),
                  ),
                ),

                const SizedBox(width: 12),

                Expanded(
                  child: metric(
                    "Maintenance",
                    telemetry.maintenanceCount.toString(),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 28),

            const Text(
              "AI PREDICTION",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),

            const SizedBox(height: 16),

            if (prediction != null) ...[
              Row(
                children: [
                  Expanded(
                    child: metric(
                      "Failure Probability",
                      "${prediction.failureProbability.toStringAsFixed(1)}%",
                    ),
                  ),

                  const SizedBox(width: 12),

                  Expanded(
                    child: metric(
                      "RUL",
                      "${prediction.remainingUsefulLife.toStringAsFixed(0)} hrs",
                    ),
                  ),
                ],
              ),

              const SizedBox(height: 16),

              metric("Recommendation", prediction.recommendation),
            ] else ...[
              const Center(
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: CircularProgressIndicator(),
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }
}
