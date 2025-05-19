# 🏦 Credit Card Approval Model API

This project provides an API interface to a machine learning model that predicts whether a user is eligible for a credit card based on submitted criteria.

## 📁 Files

- `app.py` – Main application file that exposes the API endpoint.
- `credit_card_ML.ipynb` – Notebook used to train and evaluate the credit card approval model.
- `model - Copy.pkl` – Serialized trained model.
- `requirements.txt` – Python dependencies needed to run the API.

## 🚀 Features

- Machine learning model trained on user data to predict credit card eligibility.
- Simple REST API to get approval prediction.
- Accepts user information via JSON and returns a decision (`Approved` or `Rejected`).

## 🧠 Model Training
The model was trained using credit_card_ML.ipynb. It includes data preprocessing, feature selection, model training, and evaluation. The final trained model was saved as model - Copy.pkl.

## 📌 Notes
Ensure the input JSON contains all features required by the model.

This is a prototype and not production-grade – consider model explainability, security, and data validation for production use.
