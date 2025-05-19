import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("fraud_model.pkl")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #ffe5b4, #ffb347);
        padding: 2rem;
        border-radius: 12px;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🔍 Credit Card Fraud Detection")

st.write("Enter the transaction details below:")

# Create input fields for V1 to V28
features = []
for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    features.append(val)

# Input for 'Amount' and 'Time'
amount = st.number_input("Amount", value=0.0)
time = st.number_input("Time", value=0.0)

features.extend([amount, time])

# Predict button
if st.button("Predict Fraud"):
    input_array = np.array([features])
    prediction = model.predict(input_array)[0]
    probability = model.predict_proba(input_array)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Fraud Detected! (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Transaction is Normal. (Probability of Fraud: {probability:.2f})")
