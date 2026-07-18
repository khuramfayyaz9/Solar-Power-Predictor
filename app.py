import streamlit as st
import joblib

# Load the trained model
model = joblib.load("solar_power_model.pkl")

# App Title
st.title("☀️ Solar Power Predictor")

st.write("Enter the values below to predict solar power generation.")

# User Inputs
temperature = st.number_input("Temperature (°C)", value=30.0)
prectotland = st.number_input("Prectotland", value=0.0)
rhoa = st.number_input("Rhoa", value=1.2)
irradiance_g = st.number_input("Irradiance (G)", value=700.0)
irradiance_a = st.number_input("Irradiance (A)", value=680.0)
cloud = st.number_input("Cloud", value=7.0)

# Predict Button
if st.button("Predict"):

    # Feature order MUST match the training data
    prediction = model.predict([[
        temperature,
        prectotland,
        rhoa,
        irradiance_g,
        irradiance_a,
        cloud
    ]])

    st.success(f"Predicted Solar Power: {prediction[0]:.2f}")