import streamlit as st
import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("af_model.keras")

st.title("Atrial Fibrillation (AF) Detector")

# Inputs
heart_rate = st.number_input("Heart Rate", min_value=30, max_value=200)
ppg_peak_interval = st.number_input("PPG Peak Interval", min_value=200.0, max_value=2000.0)

# Predict
if st.button("Predict"):
    input_data = np.array([[heart_rate, ppg_peak_interval]])
    prediction = model.predict(input_data)

    result = "AF Detected" if prediction[0][0] > 0.5 else "Normal Sinus Rhythm"
    st.success(f"Prediction: {result}")
