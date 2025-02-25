import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Load custom CSS
with open('app.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title of the app
st.title("Medical Insurance Cost Prediction")

# Input fields for user data
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sex = st.selectbox("Sex", options=["Male", "Female"])
bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", options=["Yes", "No"])
region = st.selectbox("Region", options=["Southeast", "Southwest", "Northeast", "Northwest"])

# Convert categorical data to numerical
sex = 0 if sex == "Male" else 1
smoker = 1 if smoker == "Yes" else 0
region_dict = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}
region = region_dict[region]

# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

# Predict the insurance cost
if st.button("Predict"):
    prediction = loaded_model.predict(input_data)
    st.write(f"Predicted Medical Insurance Cost: ${prediction[0]:.2f}")