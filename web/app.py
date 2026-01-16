import streamlit as st
from predictor import predict_yield
from main import main

st.set_page_config(page_title="Agri Yield Assistant", layout="wide")

st.title("🌾 AgriSmart – Crop Yield Intelligence Platform")

tab1, tab2 = st.tabs(["Prediction", "Ask the Agent"])


# Prediction
with st.sidebar:
    st.header("Input Parameters")

    region = st.selectbox("Region", ["North", "South", "East", "West"])
    soil_type = st.selectbox("Soil Type", ["Clay", "Sandy", "Loam", "Silt", "Peaty", "Chalky"])
    crop = st.selectbox("Crop", ["Wheat", "Rice", "Maize", "Barley", "Soybean", "Cotton"])
    rainfall = st.slider("Rainfall (mm)", 100, 1500, 800)
    temperature = st.slider("Temperature (°C)", 10, 40, 25)
    fertilizer = st.checkbox("Fertilizer Used")
    irrigation = st.checkbox("Irrigation Used")
    weather = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])
    days = st.slider("Days to Harvest", 60, 200, 120)
    
    if st.button("Predict Yield"):
        yield_prediction = predict_yield({
            "Region": region
            "Soil_Type": soil_type,
            "Crop": crop,
            "Rainfall_mm": rainfall,
            "Temperature_Celsius": temperature,
            "Fertilizer_Used": fertilizer,
            "Irrigation_Used": irrigation,
            "Weather_Condition": weather,
            "Days_to_Harvest": days,
            
        })
        result = predict_yield(features)
        st.write(f"Predicted Yield:  **{result:.2f} tons/hectare**")    



# Ask the Agent
st.subheader("Ask the Agri Assistant")

question = st.text_input("Ask a farming question")

if st.button("Ask"):
    answer = ask_agent(question)
    st.write(answer)

