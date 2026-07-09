import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../core/theme/app_theme.dart';
import '../../providers/dashboard_provider.dart';

class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  Color _statusColor(bool connected) {
    return connected ? AppTheme.success : AppTheme.danger;
  }

  String _statusText(bool connected) {
    return connected ? "ONLINE" : "OFFLINE";
  }

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<DashboardProvider>();

    return Scaffold(
      appBar: AppBar(title: const Text("System Status")),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          _buildStatusSection(
            icon: Icons.router_rounded,
            title: "MQTT Status",
            status: _statusText(provider.isConnected),
            connected: provider.isConnected,
          ),
          const SizedBox(height: 12),
          _buildStatusSection(
            icon: Icons.api_rounded,
            title: "FastAPI Status",
            status: "ONLINE",
            connected: true,
          ),
          const SizedBox(height: 12),
          _buildStatusSection(
            icon: Icons.settings_remote_rounded,
            title: "TensorFlow Status",
            status: "ONLINE",
            connected: true,
          ),
          const SizedBox(height: 12),
          _buildStatusSection(
            icon: Icons.storage_rounded,
            title: "MySQL Status",
            status: "ONLINE",
            connected: true,
          ),
          const SizedBox(height: 12),
          _buildStatusSection(
            icon: Icons.cloud_rounded,
            title: "Docker Status",
            status: "RUNNING",
            connected: true,
          ),
          const SizedBox(height: 28),
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: AppTheme.surface,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.white10),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "Application Version",
                  style: TextStyle(
                    color: AppTheme.textSecondary,
                    fontSize: 12,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 1.2,
                  ),
                ),
                const SizedBox(height: 8),
                const Text(
                  "v2.0.0 - PredictivePulse",
                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 12),
                Text(
                  "Industrial Fleet Command Center\nBuilt with Flutter & FastAPI",
                  style: TextStyle(
                    color: AppTheme.textSecondary,
                    fontSize: 12,
                    height: 1.6,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStatusSection({
    required IconData icon,
    required String title,
    required String status,
    required bool connected,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: _statusColor(connected).withOpacity(0.2)),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: _statusColor(connected).withOpacity(0.1),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Icon(icon, color: _statusColor(connected), size: 24),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  status,
                  style: TextStyle(
                    color: _statusColor(connected),
                    fontSize: 12,
                    fontWeight: FontWeight.w600,
                    letterSpacing: 1,
                  ),
                ),
              ],
            ),
          ),
          Container(
            width: 8,
            height: 8,
            decoration: BoxDecoration(
              color: _statusColor(connected),
              shape: BoxShape.circle,
              boxShadow: [
                BoxShadow(
                  color: _statusColor(connected),
                  blurRadius: 4,
                  spreadRadius: 1,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
