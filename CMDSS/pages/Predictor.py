import streamlit as st
import pickle as pkl  # or import pickle
import pandas as pd
import numpy as np

# Load your trained model
# Replace 'models/canteen_model.pkl' with the actual path to your saved model
@st.cache_resource
def load_model():
    try:
        # If using joblib:
        # return joblib.load('models/canteen_model.pkl')
        # For now, we will assume a placeholder or you can point to your file
        return None 
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

st.title("🔮 Demand Predictor")
st.write("Input the parameters below to predict canteen traffic or item demand.")

# UI for user input
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        day = st.selectbox("Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        time_slot = st.selectbox("Time Slot", ["Breakfast", "Lunch", "Snacks"])
    with col2:
        is_holiday = st.radio("Is it a holiday?", ["No", "Yes"])
        special_event = st.radio("Special Event/Festival?", ["No", "Yes"])

    # Convert inputs to numerical format for the model
    # (This depends on how you trained your model)
    input_data = pd.DataFrame([[day, time_slot, is_holiday, special_event]])

    if st.button("Generate Prediction"):
        if model:
            prediction = model.predict(input_data)
            st.metric(label="Predicted Demand", value=f"{prediction[0]} Orders")
        else:
            # Placeholder logic if model file isn't found yet
            st.warning("Model file not found. Here is a simulated prediction:")
            simulated_val = np.random.randint(50, 200)
            st.success(f"Estimated Demand: ~{simulated_val} customers")

st.info("This prediction helps in reducing food wastage by optimizing raw material orders.")