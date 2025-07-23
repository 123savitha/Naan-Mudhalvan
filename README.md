# 🛡️ Guarding Transactions with AI-Powered Credit Card Fraud Detection and Prevention

> A machine learning project to detect fraudulent credit card transactions in real-time and safeguard digital payments.

---

## 📌 Overview

With the surge in online transactions, credit card fraud has become a critical challenge. This project focuses on building an AI-powered solution to detect fraudulent transactions using classification models and deploy it with an intuitive web interface using Streamlit.

---

## 🚀 Features

- Detects fraudulent credit card transactions
- Handles class imbalance using SMOTE
- Real-time predictions via a deployed web app
- Clean UI with Streamlit
- Visual insights via EDA and model evaluation metrics

---

## 📊 Problem Statement

Classifying whether a credit card transaction is **fraudulent (1)** or **legitimate (0)** using anonymized features. This is a **binary classification** problem, with high class imbalance requiring thoughtful model evaluation strategies.

---

## 📁 Dataset

- **Source:** [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Rows:** 284,807
- **Columns:** 31 (anonymized features V1–V28, `Amount`, `Time`, `Class`)
- **Target:** `Class` (1 = Fraud, 0 = Not Fraud)

---

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **Libraries:** pandas, numpy, seaborn, matplotlib, scikit-learn, imblearn, xgboost, streamlit
- **IDE:** Google Colab / Jupyter Notebook
- **Deployment:** Streamlit Cloud

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/123savitha/Naan-Mudhalvan.git
   cd credit-card-fraud-detection
2.**pip install -r requirements.txt**
3.**streamlit run app/streamlit_app.py**
graph LR
A[Data Collection] --> B[Preprocessing]
B --> C[EDA]
C --> D[Feature Engineering]
D --> E[Modeling]
E --> F[Evaluation]
F --> G[Deployment]
**📊 Model Comparison**
Model	Accuracy	Precision	Recall	F1-Score
Logistic Regression	97.3%	73%	65%	69%
Random Forest	99.8%	92%	86%	89%
XGBoost	99.9%	93%	87%	90%

✅ Final Model: XGBoost — best trade-off between recall and precision
📈 Evaluation Metrics
Confusion Matrix

ROC-AUC Curve

Classification Report

Cross-Validation Scores



