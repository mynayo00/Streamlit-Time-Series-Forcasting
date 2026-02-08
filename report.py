import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk

data = pd.read_csv("data_clean.csv")
data["Order Date"] = pd.to_datetime(data["Order Date"])

class trend_rating:
    @staticmethod
    def trend_data(df_clean, col, freq):
        df_clean["Order Date"] = pd.to_datetime(df_clean["Order Date"])
        

        df_clean = df_clean.set_index("Order Date")

        if col == 'Order ID':
            temp = (
                df_clean[col]
                .resample(freq)   
                .count()
                .to_frame()
            )
        else:
            temp = (
                df_clean[col]
                .resample(freq)
                .mean()
                .to_frame()
            )
        return temp

    @staticmethod
    def plot_trend(df_clean, col, freq):
        temp = trend_rating.trend_data(df_clean, col, freq)
        fig, ax = plt.subplots(figsize=(16,4))
        sns.lineplot(data=temp, x=temp.index, y=col, marker="o", ax=ax)
        ax.set_title(f'Trend of {col} ({freq})')
        ax.set_xlabel('Date')
        ax.set_ylabel(col)
        ax.grid(False)   
        st.pyplot(fig)
        
class best_product:
    @staticmethod
    def product_data(df_clean):
        gb_product_revenue = df_clean.groupby('Product')[['Revenue', 'Quantity Ordered']].sum().reset_index()
        top_10_product = gb_product_revenue.sort_values(by='Revenue', ascending=False).head(10)
        return top_10_product

    @staticmethod
    def plot_product(df_clean):
        top_10_product = best_product.product_data(df_clean)

        fig, ax1 = plt.subplots(figsize=(12,6))

        
        ax1.bar(top_10_product['Product'], top_10_product['Revenue'], color="skyblue", label="Revenue")
        ax1.set_ylabel("Revenue", color="blue")
        ax1.tick_params(axis="y", labelcolor="blue")
        ax1.set_xticklabels(top_10_product['Product'], rotation=45, ha="right")

       
        ax2 = ax1.twinx()
        ax2.plot(top_10_product['Product'], top_10_product['Quantity Ordered'], color="black", marker="o", label="Quantity Ordered")
        ax2.set_ylabel("Quantity Ordered", color="black")
        ax2.tick_params(axis="y", labelcolor="black")

        fig.suptitle("Top 10 Products: Revenue vs Quantity Ordered", fontsize=14)
        ax1.grid(False)

        st.pyplot(fig)


def analysis(df_clean):
    st.header("Sales Trend Analysis")
    
    freq_label = st.selectbox(
        "Pilih frekuensi data:",
        ["Daily", "Weekly", "Monthly"],
        index=1
    )
    
    freq_map = {
        "Daily": "D",
        "Monthly": "MS",
        "Weekly": "W"
    }

    
    freq_option = freq_map[freq_label]

    
    trend_rating.plot_trend(data, "Revenue", freq_option)

    for col in ['Quantity Ordered','Revenue','Order ID']:
        if col not in ['Price Each','GMV']:
            st.subheader(f"{col} Trend")
            trend_rating.plot_trend(df_clean, col, freq_option)
            
    st.header("Top 10 Best Products")
    best_product.plot_product(df_clean)

