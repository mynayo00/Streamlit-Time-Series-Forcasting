import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Report Sales 2019')

st.sidebar.title('Navigasi')

page = st.sidebar.radio('Pilih halaman', ['Report', 'Prediction','Contact'])
data = pd.read_csv("data_clean.csv")

if page == 'Report':
    import report
    report.analysis(data) 
elif page == 'Prediction' :
    import predict
    predict.prediction()
elif page == 'Contact' :
    import contact
    contact.munculkan_kontak()
