import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'core/theme/app_theme.dart';
import 'pages/splash/splash_screen.dart';
import 'providers/dashboard_provider.dart';

void main() {
  runApp(const PredictivePulseApp());
}

class PredictivePulseApp extends StatelessWidget {
  const PredictivePulseApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (_) {
            final provider = DashboardProvider();
            provider.initialize();
            return provider;
          },
        ),
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'PredictivePulse',
        theme: AppTheme.darkTheme,
        home: const SplashScreen(),
      ),
    );
  }
}
