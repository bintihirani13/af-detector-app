import streamlit as st
import tensorflow as tf
model = tf.keras.models.load_model("af_model.keras")

st.title("AF Prediction")

# Input fields for 6 features
est_diameter_min = st.number_input('Estimated Diameter Min', format="%.6f")
est_diameter_max = st.number_input('Estimated Diameter Max', format="%.6f")
relative_velocity = st.number_input('Relative Velocity (km/h)')
est_diameter_diff = est_diameter_max - est_diameter_min  # Calculate difference
miss_distance = st.number_input('Miss Distance (km)')
absolute_magnitude = st.number_input('Absolute Magnitude')

if st.button("Predict Hazard"):
    # Prepare input as list of lists
    input_features = [[
        est_diameter_min,
        est_diameter_max,
        relative_velocity,
        est_diameter_diff,
        miss_distance,
        absolute_magnitude
    ]]
    
    prediction = model.predict(input_features)
    
    if prediction[0] == 1:
        st.error("Warning: This asteroid is potentially hazardous!")
    else:
        st.success("This asteroid is not hazardous.")

