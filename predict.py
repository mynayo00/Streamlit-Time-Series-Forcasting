import streamlit as st
import pandas as pd
import joblib

def prediction():
    # Load model ARIMA hasil fit
    model = joblib.load("model_terbaik.pkl")

    st.header("Prediksi Penjualan per Bulan")

    # Dropdown bulan
    bulan = st.selectbox("Pilih bulan prediksi:", ["2026-01","2026-02","2026-03"])
    future_date = pd.to_datetime(bulan)

    try:
        # ARIMAResultsWrapper punya .predict()
        pred = model.predict(start=future_date, end=future_date)

        st.subheader(f"Hasil Prediksi untuk {bulan}")
        st.write(pred)

        # Tambahkan grafik forecast agar lebih informatif
        st.line_chart(pred)

    except Exception as e:
        st.error(f"Gagal prediksi: {e}")