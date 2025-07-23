# 🛡️ Guarding Transactions with AI-Powered Credit Card Fraud Detection and Prevention

Detect fraudulent credit card transactions using machine learning and deploy it as a real-time web app using Streamlit.

---

## 📌 Problem Statement

Fraudulent credit card transactions are increasing rapidly. Detecting such transactions in real time is critical to prevent financial losses. This project uses a binary classification model to detect frauds using anonymized financial data. It addresses class imbalance using SMOTE and applies machine learning techniques for accurate predictions.

---

## 🧠 Abstract

This project aims to detect fraudulent credit card transactions by analyzing anonymized features. The key challenges include class imbalance and subtle fraudulent behavior patterns. Using SMOTE and machine learning classifiers like Logistic Regression, Random Forest, and XGBoost, we build a reliable model. The final model is deployed using Streamlit for real-time prediction.

---

## 💻 System Requirements

**Hardware:**
- Minimum 4GB RAM
- i3 or above processor

**Software:**
- Python 3.8+
- Google Colab / Jupyter / VS Code
- Required Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, imblearn, streamlit

---

## 🎯 Objectives

- Preprocess and balance the imbalanced fraud dataset
- Build models to classify transactions as fraud or not
- Evaluate models based on accuracy, recall, precision, and F1-score
- Deploy the final model as an interactive web app

---

## 🔄 Project Workflow

-Data Collection ➝ Preprocessing ➝ EDA ➝ Feature Engineering ➝ Modeling ➝ Evaluation ➝ Deployment



---

## 📁 Dataset Description

- **Source:** [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Type:** Public
- **Rows:** 284,807
- **Columns:** 31 (including target `Class`)
- **Target Variable:** `Class` (0 = Not Fraud, 1 = Fraud)

---

## 🧹 Data Preprocessing

- Handled missing values and removed duplicates
- Applied StandardScaler to normalize `Amount` and `Time`
- Addressed class imbalance using **SMOTE**
- Categorical encoding was not required as all features were numerical

---

## 📊 Exploratory Data Analysis (EDA)

- Visualized distributions using histograms and boxplots
- Heatmap revealed low correlation between features
- Found that most fraudulent transactions had lower amounts
- Fraud cases made up only 0.17% of the data

---

## 🏗️ Feature Engineering

- Applied feature scaling to `Amount` and `Time`
- Created new features: transaction_hour, transaction_day
- Removed features with low variance
- Selected top features based on importance from tree models

---

## 🤖 Model Building

Models used:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

All trained using SMOTE-balanced data.

---

## 📈 Model Evaluation

| Model               | Accuracy | Precision | Recall | F1-Score |
|--------------------|----------|-----------|--------|----------|
| Logistic Regression| 97.3%    | 73%       | 65%    | 69%      |
| Random Forest      | 99.8%    | 92%       | 86%    | 89%      |
| XGBoost            | 99.9%    | 93%       | 87%    | 90%      |

✅ **Best Model:** XGBoost (Balanced accuracy + recall)

**Evaluation Metrics Used:**
- Confusion Matrix
- ROC-AUC Curve
- Classification Report
- Cross-validation score

---

## 🚀 Deployment

- **Platform:** Streamlit Cloud
- **App Link:** [https://naan-mudhalvan-funcstzeen3bguwnbsdtdp.streamlit.app/]
- **Deployment Method:** Uploaded via GitHub → connected to Streamlit Cloud
- **UI Includes:**
  - Transaction input fields
  - Fraud/Not Fraud prediction
  - Model performance metrics
  - Download result option

---

## 📂 Folder Structure
credit-card-fraud-detection/
├── app/
│ └── streamlit_app.py
├── data/
│ └── creditcard.csv
├── notebooks/
│ └── fraud_modeling.ipynb
├── images/
│ └── eda_visuals.png
├── requirements.txt
├── README.md

---

## 💡 Future Scope

- Add real-time streaming data integration using Kafka or Apache Spark
- Train with deep learning models like Autoencoders
- Create fraud detection APIs for fintech usage
- Add alert notification system via email/SMS for detected frauds

---

## 👨‍💻 How to Run This Project

### 🧬 Clone the Repository

```bash
git clone https://github.com/yourusername/credit-card-fraud-detection.git
cd credit-card-fraud-detection

