import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../core/theme/app_theme.dart';
import '../../providers/dashboard_provider.dart';
import '../../services/api_service.dart';

class HistoryPage extends StatelessWidget {
  const HistoryPage({super.key});

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<DashboardProvider>();

    return Scaffold(
      appBar: AppBar(title: const Text("Sensor History")),
      body: provider.machines.isEmpty
          ? const Center(child: CircularProgressIndicator())
          : ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: provider.machines.length,
              itemBuilder: (context, index) {
                final machine = provider.machines[index];

                return Card(
                  margin: const EdgeInsets.only(bottom: 12),
                  child: ListTile(
                    leading: const Icon(Icons.precision_manufacturing),
                    title: Text(machine.machineName),
                    subtitle: Text(machine.machineType),
                    trailing: const Icon(Icons.arrow_forward_ios),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (_) =>
                              _HistoryDetailPage(machineId: machine.machineId),
                        ),
                      );
                    },
                  ),
                );
              },
            ),
    );
  }
}

class _HistoryDetailPage extends StatefulWidget {
  final int machineId;

  const _HistoryDetailPage({required this.machineId});

  @override
  State<_HistoryDetailPage> createState() => _HistoryDetailPageState();
}

class _HistoryDetailPageState extends State<_HistoryDetailPage> {
  late Future<List<dynamic>> _historyFuture;
  final ApiService _apiService = ApiService();

  @override
  void initState() {
    super.initState();
    _historyFuture = _apiService.getHistory(widget.machineId);
  }

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<DashboardProvider>();
    final machine = provider.getTelemetry(widget.machineId);

    return Scaffold(
      appBar: AppBar(
        title: Text("${machine?.machineName ?? "Machine"} History"),
      ),
      body: FutureBuilder<List<dynamic>>(
        future: _historyFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }

          if (snapshot.hasError) {
            return Center(
              child: Text(
                "Error: ${snapshot.error}",
                style: const TextStyle(color: Colors.red),
              ),
            );
          }

          if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return const Center(child: Text("No history records found"));
          }

          final history = snapshot.data!;

          return ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: history.length,
            itemBuilder: (context, index) {
              final record = history[index];

              return Container(
                margin: const EdgeInsets.only(bottom: 12),
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  color: AppTheme.surface,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: Colors.white10),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      record["timestamp"] ?? "N/A",
                      style: TextStyle(
                        color: AppTheme.textSecondary,
                        fontSize: 12,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        _historyMetric(
                          "Temperature",
                          "${record["temperature"]?.toStringAsFixed(1) ?? "N/A"}°C",
                        ),
                        _historyMetric(
                          "RPM",
                          record["rpm"]?.toString() ?? "N/A",
                        ),
                        _historyMetric(
                          "Vibration",
                          "${record["vibration"]?.toStringAsFixed(2) ?? "N/A"}",
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        _historyMetric(
                          "Oil Level",
                          "${record["oil_level"]?.toStringAsFixed(0) ?? "N/A"}%",
                        ),
                        _historyMetric(
                          "Current",
                          "${record["current"]?.toStringAsFixed(1) ?? "N/A"}A",
                        ),
                        _historyMetric(
                          "Health",
                          "${record["health_score"]?.toStringAsFixed(0) ?? "N/A"}%",
                        ),
                      ],
                    ),
                  ],
                ),
              );
            },
          );
        },
      ),
    );
  }

  Widget _historyMetric(String title, String value) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          value,
          style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 2),
        Text(
          title,
          style: TextStyle(color: AppTheme.textSecondary, fontSize: 10),
        ),
      ],
    );
  }
}
