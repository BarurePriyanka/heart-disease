import streamlit as st
import pandas as pd
import joblib
# Load the trained model
model = joblib.load(r"C:\Users\Komal Madde\OneDrive\Desktop\priya\streamlit trail\model.pkl")
st.title("Heart Disease Prediction App ❤️")
st.write("Enter the patient details below to predict heart disease risk.")

# Sidebar input
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
bp = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=400, value=200)
max_hr = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
# Add more features as per your trained model

# Convert categorical inputs to numeric if needed
sex_val = 1 if sex == "Male" else 0

# Prepare input for the model
input_data = pd.DataFrame([[age, sex_val, bp, chol, max_hr]],
                          columns=['age', 'sex', 'bp', 'chol', 'max_hr'])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "High Risk ❤️" if prediction[0] == 1 else "Low Risk 💚"
    st.success(f"Prediction: {result}")
