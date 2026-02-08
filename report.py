import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("data_clean.csv")

class trend_rating:
    @staticmethod
    def trend_data(df_clean, col):
        # pastikan kolom tanggal jadi datetime
        df_clean["Order Date"] = pd.to_datetime(df_clean["Order Date"])
        
        if col == 'Order ID':
            temp = (
                df_clean.set_index('Order Date')[col]
                .resample('MS')   # Monthly Start
                .count()
                .to_frame()
            )
        else:
            temp = (
                df_clean.set_index('Order Date')[col]
                .resample('MS')
                .mean()
                .to_frame()
            )
        return temp

    @staticmethod
    def plot_trend(df_clean, col):
        temp = trend_rating.trend_data(df_clean, col)
        fig, ax = plt.subplots(figsize=(16,4))
        sns.lineplot(data=temp, x=temp.index, y=col, marker="o", ax=ax)
        ax.set_title(f'Trend of {col} (Monthly)')
        ax.set_xlabel('Month')
        ax.set_ylabel(col)
        ax.grid(True)
        st.pyplot(fig)   # tampilkan di Streamlit

# Contoh pemanggilan di Streamlit
def analysis(df_clean):
    st.header("Sales Trend Analysis")
    for col in ['Quantity Ordered','Revenue','Order ID']:
        if col not in ['Price Each','GMV']:
            st.subheader(f"{col} Trend")
            trend_rating.plot_trend(df_clean, col)

# Jalankan analisis
analysis(data)