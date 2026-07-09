import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../providers/dashboard_provider.dart';

class PredictionPage extends StatelessWidget {
  const PredictionPage({super.key});

  Color _statusColor(double health) {
    if (health >= 80) return Colors.green;
    if (health >= 50) return Colors.orange;
    return Colors.red;
  }

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<DashboardProvider>();

    return Scaffold(
      appBar: AppBar(title: const Text("AI Predictions")),

      body: provider.predictionMap.isEmpty
          ? const Center(child: CircularProgressIndicator())
          : ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: provider.predictionMap.length,

              itemBuilder: (context, index) {
                final prediction = provider.predictionMap.values.elementAt(
                  index,
                );

                final telemetry = provider.getTelemetry(prediction.machineId);

                return Container(
                  margin: const EdgeInsets.only(bottom: 16),

                  padding: const EdgeInsets.all(18),

                  decoration: BoxDecoration(
                    color: const Color(0xff171B24),

                    borderRadius: BorderRadius.circular(18),

                    border: Border.all(
                      color: _statusColor(prediction.healthScore),
                    ),
                  ),

                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,

                    children: [
                      Row(
                        children: [
                          Icon(
                            Icons.analytics,
                            color: _statusColor(prediction.healthScore),
                          ),

                          const SizedBox(width: 10),

                          Text(
                            telemetry?.machineName ??
                                "Machine ${prediction.machineId}",

                            style: const TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),

                      const SizedBox(height: 18),

                      Text(
                        "Health Score",
                        style: TextStyle(color: Colors.white.withOpacity(.6)),
                      ),

                      Text(
                        "${prediction.healthScore.toStringAsFixed(0)}%",
                        style: const TextStyle(
                          fontSize: 36,
                          fontWeight: FontWeight.bold,
                        ),
                      ),

                      const SizedBox(height: 20),

                      Row(
                        children: [
                          Expanded(
                            child: _metric(
                              "Failure Probability",
                              "${prediction.failureProbability.toStringAsFixed(1)}%",
                            ),
                          ),

                          const SizedBox(width: 12),

                          Expanded(
                            child: _metric(
                              "RUL",
                              "${prediction.remainingUsefulLife.toStringAsFixed(0)} hrs",
                            ),
                          ),
                        ],
                      ),

                      const SizedBox(height: 18),

                      Container(
                        width: double.infinity,

                        padding: const EdgeInsets.all(14),

                        decoration: BoxDecoration(
                          color: Colors.black26,

                          borderRadius: BorderRadius.circular(12),
                        ),

                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,

                          children: [
                            const Text(
                              "Recommendation",
                              style: TextStyle(color: Colors.white70),
                            ),

                            const SizedBox(height: 8),

                            Text(
                              prediction.recommendation,

                              style: const TextStyle(
                                fontSize: 16,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                );
              },
            ),
    );
  }

  Widget _metric(String title, String value) {
    return Container(
      padding: const EdgeInsets.all(14),

      decoration: BoxDecoration(
        color: Colors.black26,

        borderRadius: BorderRadius.circular(12),
      ),

      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,

        children: [
          Text(
            value,
            style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),

          const SizedBox(height: 6),

          Text(title, style: const TextStyle(color: Colors.white60)),
        ],
      ),
    );
  }
}
