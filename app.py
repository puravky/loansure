import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_approval_model2.pkl")

st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦")
st.title("🏦 LoanSure")
st.markdown("Predict whether your loan application will be approved based on your details.")


with st.form("loan_form"):
    col1, col2 = st.columns(2)

    with col1:
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        applicant_income = st.number_input(
            "Applicant Income (monthly, ₹)", step=10000, placeholder="e.g. 50000"
        )
        loan_amount = st.number_input(
            "Loan Amount (₹)", step=10000, placeholder="e.g. 1500000"
        )
        loan_term = st.selectbox(
            "Loan Amount Term (in days)", [360, 720, 120, 180, 240, 300, 60, 84]
        )
        
    with col2:
        married = st.selectbox("Married", ["Yes", "No"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
        coapplicant_income = st.number_input(
            "Coapplicant Income (monthly, ₹)", step=10000, placeholder="e.g. 20000"
        )
        credit_history = st.selectbox(
            "Credit History",
            [1.0, 0.0],
            format_func=lambda x: "1.0 - Good (all dues met)" if x == 1.0 else "0.0 - Poor (dues not met)",
        )

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame({
        'Gender': ["Male"],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount / 1000],
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
st.markdown("Made with ❤️ by Puravky & RitijRaj")