import 'package:flutter/material.dart';

class AppTheme {
  AppTheme._();

  // ---------- Colors ----------
  static const Color background = Color(0xFF0F1115);
  static const Color surface = Color(0xFF1A1D24);

  static const Color primary = Color(0xFF3B82F6);

  static const Color success = Color(0xFF22C55E);
  static const Color warning = Color(0xFFF59E0B);
  static const Color danger = Color(0xFFEF4444);

  static const Color textPrimary = Colors.white;
  static const Color textSecondary = Color(0xFFA3AAB7);

  static ThemeData darkTheme = ThemeData(
    useMaterial3: true,
    brightness: Brightness.dark,

    scaffoldBackgroundColor: background,

    colorScheme: ColorScheme.dark(
      primary: primary,
      secondary: primary,
      surface: surface,
    ),

    appBarTheme: const AppBarTheme(
      backgroundColor: background,
      elevation: 0,
      centerTitle: false,
    ),

    cardTheme: CardThemeData(
      color: surface,
      elevation: 0,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    ),
  );
}
