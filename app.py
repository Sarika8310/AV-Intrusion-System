import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Setup
st.set_page_config(page_title="🚗 Intrusion Detector", layout="centered")
st.title("🚗 Smart Car Intrusion Detection")
st.markdown("Upload CAN bus data (DoS or RPM) to detect possible intrusions in real time.")

# Load model and scaler
model = joblib.load("random_forest_car_model.pkl")
scaler = joblib.load("scaler.pkl")  # Load previously fitted scaler

# File Upload
uploaded_file = st.file_uploader("📤 Upload CAN Bus CSV File", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, header=None)

        # Try using expected 12-column header
        columns = ['Time', 'ID', 'Len', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'Class']
        if df.shape[1] == 12:
            df.columns = columns
        else:
            st.error("❌ Unexpected CSV format. It must have exactly 12 columns.")
            st.stop()

        # Drop Time and Class
        df = df.drop(['Time', 'Class'], axis=1)

        # Convert all hex to integers, else set as 0
        def safe_hex(x):
            try:
                return int(str(x), 16)
            except:
                return 0

        for col in df.columns:
            df[col] = df[col].apply(safe_hex)

        # Scale
        df_scaled = scaler.transform(df)

        # Predict
        predictions = model.predict(df_scaled)
        probs = model.predict_proba(df_scaled)

        df['Status'] = ['ATTACK' if p == 1 else 'NORMAL' for p in predictions]
        df['Confidence (%)'] = [round(max(p) * 100, 2) for p in probs]

        # Output
        st.success("✅ Detection Complete")
        st.dataframe(df)

        csv_output = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Results", csv_output, "detection_results.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("Please upload a CSV file to begin.")
