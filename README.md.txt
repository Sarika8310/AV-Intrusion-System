# 🚗 Smart Car Intrusion Detection System

A machine learning-powered Intrusion Detection System (IDS) to identify cyber-attacks on autonomous vehicle CAN bus networks in real time.

---

## 📌 Project Overview

Autonomous vehicles rely on CAN (Controller Area Network) communication between electronic components. This project detects abnormal behavior (DoS attacks) using machine learning and displays results via a Streamlit web app.

---

## 📂 Features

- CAN Bus data pre-processing and hex decoding
- Random Forest model for real-time attack detection
- Streamlit interface to upload and analyze CAN data
- Detection logs with confidence scores
- Downloadable results as CSV

---

## 🧠 Machine Learning

- **Model**: Random Forest Classifier
- **Accuracy**: ~99% on test data
- **Features**: ID, D1–D8 (decoded hex), Len
- **Classes**: 
  - `0`: Normal
  - `1`: DoS Attack

---

### 🔗 Download Model

You can download the trained model here:  
👉 [random_forest_car_model.pkl](https://drive.google.com/file/d/1cBlwF8Jku_PRHzbaG-TaIoPEB5b0UIsL/view?usp=sharing)


