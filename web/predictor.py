import pickle
import numpy as np

model_path = "/Users/apple/Desktop/Agric_smart/notebooks/ml/yield_prediction_model.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

def predict_yield(features):
    """
    features: dict of user inputs
    """

    X = np.array([[
        features["Region"],
        features["Soil_Type"],
        features["Crop"],
        features["Rainfall_mm"],
        features["Temperature_Celsius"],
        features["Fertilizer_Used"],
        features["Irrigation_Used"]
        features["Weather_Condition"],
        features["Days_to_Harvest"]			
    ]])

    prediction = model.predict(X)
    return float(prediction[0])