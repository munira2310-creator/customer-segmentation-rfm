import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Customer Segmentation Dashboard")

df = pd.read_csv("Customer_Segmentation_RFM.csv")

st.subheader("Segment Distribution")
st.bar_chart(df['Segment'].value_counts())

st.subheader("RFM Table Preview")
st.dataframe(df.head())
