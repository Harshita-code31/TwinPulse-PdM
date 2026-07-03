from pathlib import Path

from tensorflow.keras.models import load_model

# -------------------------------------------------
# Paths
# -------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[3]

MODEL_PATH = (
    ROOT_DIR
    / "artifacts"
    / "trained_models"
    / "model.keras"
)

# -------------------------------------------------
# Singleton Model
# -------------------------------------------------

_model = None


def get_model():
    """
    Loads the TensorFlow model only once.
    Returns the already loaded model afterwards.
    """

    global _model

    if _model is None:

        print("Loading TensorFlow Model...")

        _model = load_model(MODEL_PATH)

        print("Model Loaded Successfully!")

    return _model