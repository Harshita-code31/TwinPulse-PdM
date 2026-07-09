import 'dart:convert';

import 'package:http/http.dart' as http;

class ApiService {
  // Android Emulator
  static const String baseUrl = "http://10.0.2.2:8000";

  // Physical Phone
  // static const String baseUrl = "http://YOUR_PC_IP:8000";

  Future<List<dynamic>> getAlerts() async {
    final response = await http.get(Uri.parse("$baseUrl/alerts"));

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }

    throw Exception("Failed to load alerts");
  }

  Future<List<dynamic>> getHistory(int machineId) async {
    final response = await http.get(Uri.parse("$baseUrl/history/$machineId"));

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }

    throw Exception("Failed to load history");
  }
}
