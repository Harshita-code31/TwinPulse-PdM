import 'dart:async';

import 'package:flutter/material.dart';

import '../../core/theme/app_theme.dart';

import '../landing/landing_page.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();

    Timer(const Duration(seconds: 3), () {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => const LandingPage()),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                Icons.precision_manufacturing_rounded,
                size: 90,
                color: AppTheme.primary,
              ),

              SizedBox(height: 30),

              Text(
                "PredictivePulse",
                style: TextStyle(
                  fontSize: 34,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.textPrimary,
                ),
              ),

              SizedBox(height: 10),

              Text(
                "Industrial Predictive Maintenance",
                style: TextStyle(color: AppTheme.textSecondary, fontSize: 16),
              ),

              SizedBox(height: 70),

              CircularProgressIndicator(color: AppTheme.primary),
            ],
          ),
        ),
      ),
    );
  }
}
