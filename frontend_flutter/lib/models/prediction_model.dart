class PredictionModel {
  final int machineId;
  final double healthScore;
  final double failureProbability;
  final double remainingUsefulLife;
  final String recommendation;

  const PredictionModel({
    required this.machineId,
    required this.healthScore,
    required this.failureProbability,
    required this.remainingUsefulLife,
    required this.recommendation,
  });

  factory PredictionModel.fromJson(Map<String, dynamic> json) {
    return PredictionModel(
      machineId: json["machine_id"],
      healthScore: (json["health_score"] as num).toDouble(),
      failureProbability: (json["failure_probability"] as num).toDouble(),
      remainingUsefulLife: (json["remaining_useful_life"] as num).toDouble(),
      recommendation: json["recommendation"],
    );
  }
}
