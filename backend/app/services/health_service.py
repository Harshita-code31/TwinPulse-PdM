def get_machine_health(machine_id: int):
    """
    Temporary health service.

    Later this will use TensorFlow predictions.
    """

    return {
        "machine_id": machine_id,
        "health_score": 96.5,
        "status": "Healthy",
    }