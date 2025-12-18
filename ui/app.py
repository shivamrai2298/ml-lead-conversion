import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Lead Conversion Predictor")

data = {
    "call_duration": st.slider("Call Duration",0,500,120),
    "campaign_source": st.selectbox("Campaign",["google","facebook","organic"]),
    "calls_last_7_days": st.slider("Calls last 7 days",0,10,2),
    "hour_of_day": st.slider("Hour of day",0,23,12)
}

df = pd.DataFrame([data])
prob = model.predict_proba(df)[0][1]
st.success(f"Conversion Probability: {prob:.2f}")

