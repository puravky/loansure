import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("loan_approval_model2.pkl")

st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦")
st.title("🏦 LoanSure")
st.markdown("Predict whether your loan application will be approved based on your details.")

with st.form("loan_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.selectbox("Loan Amount Term (in days)", [360, 120, 180, 240, 300, 60, 84])
    credit_history = st.selectbox("Credit History", [1.0, 0.0])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
        st.info(f"Approval Probability: {round(prediction_proba[1] * 100, 2)}%")
    else:
        st.error("❌ Loan Not Approved")
        st.info(f"Approval Probability: {round(prediction_proba[1] * 100, 2)}%")

st.markdown("---")
st.markdown("Made with ❤️ by Ritij & Purav")