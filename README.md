💻 Laptop Price Predictor

An end-to-end Machine Learning application for predicting laptop prices from technical specifications.
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)](https://react.dev/)
---

🚀 Overview


Laptop Price Predictor is a full-stack Machine Learning application that estimates the price of a laptop based on specifications such as RAM, CPU, storage, display and other hardware features.

The prediction model is a Gradient Boosting Regressor, tuned using GridSearchCV and trained on 1,303 real laptop listings.

«🎯 Best Model: Tuned Gradient Boosting Regressor
📈 R² Score: 0.893
💶 RMSE: €296»

---

✨ Features

- 🔮 Predict laptop prices from hardware specifications
- 🤖 Machine Learning powered predictions
- ⚡ FastAPI backend with "/predict" endpoint
- 🖥️ Interactive React frontend
- 📊 Feature engineering from raw laptop specifications
- 🔧 Hyperparameter tuning using GridSearchCV
- 📈 Comparison of multiple regression algorithms
- 💻 Runs locally without a frontend build step

---

🧠 Machine Learning Pipeline

Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Exploratory Analysis
     ↓
Model Comparison
     ↓
Hyperparameter Tuning
     ↓
Gradient Boosting Model
     ↓
FastAPI Backend
     ↓
Interactive Web Interface
     ↓
💰 Predicted Laptop Price

---

📊 Model Comparison

Model| R²| RMSE (€)
🏆 Gradient Boosting — Tuned| 0.893| 296
Gradient Boosting — Default| 0.878| 302
Random Forest| 0.872| 306
Linear Regression| 0.840| 340
Decision Tree| 0.804| 374

The tuned Gradient Boosting Regressor achieved the best performance among the tested models.

---

🔬 Feature Engineering

The project transforms raw laptop specifications into machine-learning-ready features, including:

- RAM extraction
- Weight extraction
- CPU speed and brand
- GPU brand
- Touchscreen indicator
- IPS display indicator
- Screen resolution
- Pixels Per Inch (PPI)
- Separate SSD and HDD storage

For example:

"8GB" → 8
"1.37kg" → 1.37
"256GB SSD + 1TB HDD" → SSD + HDD features

---

## 📊 Dataset

The dataset used for this project was obtained from Kaggle:

🔗 **[Laptop Price Dataset — Kaggle](https://www.kaggle.com/datasets/muhammetvarl/laptop-price)**

It contains **1,303 laptop listings** with specifications such as:

- Brand
- CPU
- GPU
- RAM
- Storage
- Screen
- Weight
- Price

The dataset was cleaned and transformed before being used for model training.

---

🛠️ Tech Stack

Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

Backend

- FastAPI
- Uvicorn

Frontend

- React
- HTML
- CSS
- JavaScript

---

📁 Project Structure

laptop-price-predictor/
│
├── 📄 laptop_price.csv
├── 📄 laptop_cleaned.csv
├── 📄 data_cleaning.py
│
├── 🤖 laptop_price_model.pkl
├── 📄 model_columns.pkl
│
├── ⚡ app.py
├── 🌐 index.html
│
└── 📖 README.md

---

⚙️ Run Locally

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/laptop-price-predictor.git
cd laptop-price-predictor

2. Install dependencies

pip install fastapi uvicorn joblib pandas scikit-learn

3. Start the FastAPI backend

uvicorn app:app --reload

The API will run at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

4. Open the frontend

Open:

index.html

directly in your browser.

---


👩‍💻 Author

Inshra Shaikh

Computer Science Engineering — Data Science
Schoool of Engineering and Technology , MGM University

---

⭐ If you found this project interesting

Give the repository a ⭐ and feel free to explore the project!
