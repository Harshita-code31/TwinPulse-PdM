import '../machine_details/machine_details_page.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../core/theme/app_theme.dart';
import '../../providers/dashboard_provider.dart';

import '../../widgets/module_tile.dart';
import '../../widgets/section_title.dart';
import '../../widgets/telemetry_panel.dart';

import '../alerts/alerts_page.dart';
import '../history/history_page.dart';
import '../prediction/prediction_page.dart';
import '../settings/settings_page.dart';

class LandingPage extends StatelessWidget {
  const LandingPage({super.key});

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<DashboardProvider>();
    final machines = provider.machines;

    return Scaffold(
      body: Stack(
        children: [
          // Background Glows
          Positioned(
            top: -120,
            right: -120,
            child: Container(
              width: 260,
              height: 260,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppTheme.primary.withOpacity(.05),
              ),
            ),
          ),
          Positioned(
            bottom: -120,
            left: -120,
            child: Container(
              width: 240,
              height: 240,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppTheme.primary.withOpacity(.03),
              ),
            ),
          ),

          SafeArea(
            child: SingleChildScrollView(
              padding: const EdgeInsets.fromLTRB(24, 24, 24, 32),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Status Bar
                  Row(
                    children: [
                      const _PulseIndicator(),
                      const SizedBox(width: 10),
                      Text(
                        provider.isConnected ? "MQTT LIVE" : "OFFLINE",
                        style: TextStyle(
                          color: provider.isConnected
                              ? AppTheme.success
                              : AppTheme.danger,
                          fontWeight: FontWeight.bold,
                          letterSpacing: 2,
                        ),
                      ),
                      const Spacer(),
                      Text(
                        "${machines.length}/5 UNITS",
                        style: const TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 16,
                          color: AppTheme.textSecondary,
                        ),
                      ),
                    ],
                  ),

                  const SizedBox(height: 24),
                  const Text(
                    "PREDICTIVEPULSE",
                    style: TextStyle(
                      fontSize: 34,
                      fontWeight: FontWeight.bold,
                      letterSpacing: -0.5,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    "Industrial Fleet Command Center",
                    style: TextStyle(
                      color: AppTheme.textSecondary,
                      fontSize: 16,
                    ),
                  ),

                  const SizedBox(height: 28),
                  // Fleet Aggregate Panel
                  TelemetryPanel(
                    isConnected: provider.isConnected,
                    machineName: "FLEET OVERVIEW",
                    healthScore: machines.isEmpty
                        ? 0
                        : machines
                                  .map((e) => e.healthScore)
                                  .reduce((a, b) => a + b) /
                              machines.length,
                    mqttStatus: provider.isConnected ? "CONNECTED" : "OFFLINE",
                    aiStatus: "ONLINE",
                    databaseStatus: "SYNCED",
                    lastSync: DateTime.now().toString().substring(11, 19),
                  ),

                  const SizedBox(height: 36),
                  const SectionTitle(title: "ACTIVE UNITS"),
                  const SizedBox(height: 18),

                  // Scrollable machine list
                  ListView.separated(
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    itemCount: machines.length,
                    separatorBuilder: (_, __) => const SizedBox(height: 16),
                    itemBuilder: (context, index) {
                      final machine = machines[index];
                      return InkWell(
                        borderRadius: BorderRadius.circular(20),
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (_) => MachineDetailsPage(
                                machineId: machine.machineId,
                              ),
                            ),
                          );
                        },
                        child: Container(
                          padding: const EdgeInsets.all(20),
                          decoration: BoxDecoration(
                            color: AppTheme.surface,
                            borderRadius: BorderRadius.circular(20),
                            border: Border.all(
                              color: machine.healthScore > 80
                                  ? AppTheme.success.withOpacity(.2)
                                  : machine.healthScore > 50
                                  ? AppTheme.warning.withOpacity(.2)
                                  : AppTheme.danger.withOpacity(.2),
                            ),
                          ),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Row(
                                children: [
                                  Container(
                                    padding: const EdgeInsets.all(8),
                                    decoration: BoxDecoration(
                                      color:
                                          (machine.healthScore > 80
                                                  ? AppTheme.success
                                                  : machine.healthScore > 50
                                                  ? AppTheme.warning
                                                  : AppTheme.danger)
                                              .withOpacity(0.1),
                                      borderRadius: BorderRadius.circular(10),
                                    ),
                                    child: Icon(
                                      Icons.precision_manufacturing_rounded,
                                      size: 20,
                                      color: machine.healthScore > 80
                                          ? AppTheme.success
                                          : machine.healthScore > 50
                                          ? AppTheme.warning
                                          : AppTheme.danger,
                                    ),
                                  ),
                                  const SizedBox(width: 12),
                                  Expanded(
                                    child: Text(
                                      machine.machineName,
                                      style: const TextStyle(
                                        fontSize: 18,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                  ),
                                  const Icon(
                                    Icons.chevron_right_rounded,
                                    color: Colors.white24,
                                  ),
                                ],
                              ),
                              const SizedBox(height: 20),
                              Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceBetween,
                                children: [
                                  _metric(
                                    "Health",
                                    "${machine.healthScore.toStringAsFixed(0)}%",
                                  ),
                                  _metric(
                                    "Temp",
                                    "${machine.temperature.toStringAsFixed(1)}°C",
                                  ),
                                  _metric("RPM", machine.rpm.toString()),
                                  _metric(
                                    "Oil",
                                    "${machine.oilLevel.toStringAsFixed(0)}%",
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ),
                      );
                    },
                  ),

                  const SizedBox(height: 36),
                  const SectionTitle(title: "QUICK ACCESS"),
                  const SizedBox(height: 18),
                  GridView.count(
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    crossAxisCount: 2,
                    mainAxisSpacing: 16,
                    crossAxisSpacing: 16,
                    childAspectRatio: 1.1,
                    children: [
                      ModuleTile(
                        icon: Icons.analytics_outlined,
                        title: "Analytics",
                        subtitle: "AI Insights",
                        onTap: () => Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (_) => const PredictionPage(),
                          ),
                        ),
                      ),
                      ModuleTile(
                        icon: Icons.notifications_none_rounded,
                        title: "Alerts",
                        subtitle: "Fleet Status",
                        onTap: () => Navigator.push(
                          context,
                          MaterialPageRoute(builder: (_) => const AlertsPage()),
                        ),
                      ),
                      ModuleTile(
                        icon: Icons.history_rounded,
                        title: "History",
                        subtitle: "Past Logs",
                        onTap: () => Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (_) => const HistoryPage(),
                          ),
                        ),
                      ),
                      ModuleTile(
                        icon: Icons.settings_outlined,
                        title: "Settings",
                        subtitle: "Preferences",
                        onTap: () => Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (_) => const SettingsPage(),
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _metric(String title, String value) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          value,
          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 4),
        Text(
          title.toUpperCase(),
          style: TextStyle(
            color: AppTheme.textSecondary.withOpacity(.7),
            fontSize: 10,
            fontWeight: FontWeight.w600,
            letterSpacing: 1.2,
          ),
        ),
      ],
    );
  }
}

class _PulseIndicator extends StatefulWidget {
  const _PulseIndicator({Key? key}) : super(key: key);

  @override
  State<_PulseIndicator> createState() => _PulseIndicatorState();
}

class _PulseIndicatorState extends State<_PulseIndicator>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1200),
    )..repeat(reverse: true);
    _animation = Tween<double>(
      begin: 0.4,
      end: 1.0,
    ).animate(CurvedAnimation(parent: _controller, curve: Curves.easeInOut));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: _animation,
      child: Container(
        width: 10,
        height: 10,
        decoration: const BoxDecoration(
          color: AppTheme.success,
          shape: BoxShape.circle,
          boxShadow: [
            BoxShadow(color: AppTheme.success, blurRadius: 6, spreadRadius: 2),
          ],
        ),
      ),
    );
  }
}
