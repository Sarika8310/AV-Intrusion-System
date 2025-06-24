Here’s a **concise version** of your `README.md` — clean, informative, and perfect for GitHub:

---

```markdown
# 🚗 Smart Car Intrusion Detection System

Detects cyber-attacks in autonomous vehicles using Machine Learning on CAN bus data. Built with a trained Random Forest model and deployed via Streamlit.

---

## 📁 Project Structure

```

AV-Intrusion-System/
├── app.py              # Streamlit app
├── .gitignore          # Ignores large model files
├── scaler.pkl          # Preprocessing scaler (download below)
├── datasets/           # Training & test CSV files
└── README.md

````

---

## 🔍 How It Works

- Input: CAN bus `.csv` files
- Preprocessing: Hex to int + StandardScaler
- Output: `NORMAL` or `ATTACK` + confidence %
- Model: Trained on RPM data, tested on DoS attacks

---

## ⚙️ Setup & Run

```bash
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
````

> 🔽 Download model & scaler:
> [Model (.pkl)](https://drive.google.com/file/d/1cBlwF8Jku_PRHzbaG-TaIoPEB5b0UIsL/view?usp=drive_link)
> Scaler (.pkl)

---

## 📊 Datasets

* `datasets/RPM_dataset.csv` — Training data(https://drive.google.com/file/d/103aYRiNQINiV7vyzDtEaXvHLZIrlDmsl/view?usp=drive_link)
* `datasets/DoS_dataset.csv` — Attack test data(https://drive.google.com/file/d/1_Z8adK7KpcJk6eEm6wkf6YhsRmNGS8aQ/view?usp=drive_link)


---

