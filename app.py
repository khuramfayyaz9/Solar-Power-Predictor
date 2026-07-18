import streamlit as st
import joblib

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("solar_power_model.pkl")

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Solar Power Predictor",
    page_icon="☀️",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.title("☀️ Solar Power Predictor")
st.write("Predict solar power generation using a Machine Learning model.")

st.markdown("---")

# -------------------------------
# Input Section
# -------------------------------
st.subheader("Enter Input Values")

col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=3.4,
        max_value=32.4,
        value=20.0
    )

    prectotland = st.number_input(
        "Prectotland",
        min_value=0.0,
        max_value=3.35,
        value=0.0
    )

    rhoa = st.number_input(
        "Rhoa",
        min_value=1.13,
        max_value=1.24,
        value=1.18
    )

with col2:
    irradiance_g = st.number_input(
        "Irradiance (G)",
        min_value=0.0,
        max_value=720.0,
        value=300.0
    )

    irradiance_a = st.number_input(
        "Irradiance (A)",
        min_value=0.0,
        max_value=1015.0,
        value=500.0
    )

    cloud = st.number_input(
        "Cloud",
        min_value=0.0,
        max_value=1.0,
        value=0.2
    )

st.markdown("---")

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Predict Solar Power"):

    prediction = model.predict([[
        temperature,
        prectotland,
        rhoa,
        irradiance_g,
        irradiance_a,
        cloud
    ]])

    st.success(f"⚡ Predicted Solar Power: {prediction[0]:.2f} W")

st.markdown("---")

st.caption("Developed using Python, Streamlit, Scikit-learn and Linear Regression.")
