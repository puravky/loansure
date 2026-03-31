# 🏦 LoanSure

A minimal loan approval predictor built with Streamlit and scikit-learn.

## What it does

Fill in your financial and personal details and get an instant prediction on whether your loan application is likely to be approved, along with the approval probability.

## Tech Stack

- **Frontend** — Streamlit
- **Model** — Logistic Regression (scikit-learn pipeline)
- **Data** — [Kaggle Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Input Fields

| Field | Description |
|---|---|
| Married | Marital status of the applicant |
| Dependents | Number of financial dependents |
| Education | Graduate / Not Graduate |
| Self Employed | Whether the applicant is self-employed |
| Applicant Income | Monthly gross income (₹) |
| Coapplicant Income | Co-applicant's monthly income (₹) |
| Loan Amount | Total loan amount requested (₹) |
| Loan Term | Repayment duration in days |
| Credit History | Whether past dues have been cleared |
| Property Area | Urban / Semiurban / Rural |

