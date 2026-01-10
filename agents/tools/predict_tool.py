import joblib
import numpy as np

MODEL_PATH = "models/yield_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_yield(features):
    """
    Predict agricultural yield.
    Expected input example:
    {
        "rainfall": 120,
        "temperature": 25,
        "region": 1,
        "crop": 2
    }
    """
    X = np.array([list(features.values())])
    prediction = model.predict(X)

    return {
        "prediction": float(prediction[0]),
        "features": features
    }
