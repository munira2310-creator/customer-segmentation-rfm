import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page config (VERY IMPORTANT)
# -----------------------------
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("Customer_Segmentation_RFM.csv")

# -----------------------------
# Title & description
# -----------------------------
st.title("📊 Customer Segmentation Dashboard (RFM Analysis)")
st.markdown(
    """
    This dashboard presents customer segments derived using **RFM (Recency, Frequency, Monetary)** analysis.
    It is designed for **business decision-making**, not just visualization.
    """
)

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", df['CustomerID'].nunique())
col2.metric("Loyal Customers", (df['Segment'] == 'Loyal Customers').sum())
col3.metric("At Risk Customers", (df['Segment'] == 'At Risk Customers').sum())
col4.metric("New Customers", (df['Segment'] == 'New Customers').sum())

st.divider()

# -----------------------------
# Filters
# -----------------------------
st.subheader("🔍 Filters")

segment_filter = st.multiselect(
    "Select Customer Segment",
    options=df['Segment'].unique(),
    default=df['Segment'].unique()
)

filtered_df = df[df['Segment'].isin(segment_filter)]

# -----------------------------
# Segment Distribution Chart
# -----------------------------
st.subheader("👥 Customer Segment Distribution")

fig, ax = plt.subplots()
filtered_df['Segment'].value_counts().plot(
    kind='bar',
    ax=ax
)
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")
ax.set_title("Distribution of Customer Segments")

st.pyplot(fig)

st.divider()

# -----------------------------
# RFM Score Distribution
# -----------------------------
st.subheader("📈 RFM Score Overview")

col5, col6, col7 = st.columns(3)

with col5:
    fig_r, ax_r = plt.subplots()
    filtered_df['R_score'].value_counts().sort_index().plot(kind='bar', ax=ax_r)
    ax_r.set_title("Recency Score Distribution")
    st.pyplot(fig_r)

with col6:
    fig_f, ax_f = plt.subplots()
    filtered_df['F_score'].value_counts().sort_index().plot(kind='bar', ax=ax_f)
    ax_f.set_title("Frequency Score Distribution")
    st.pyplot(fig_f)

with col7:
    fig_m, ax_m = plt.subplots()
    filtered_df['M_score'].value_counts().sort_index().plot(kind='bar', ax=ax_m)
    ax_m.set_title("Monetary Score Distribution")
    st.pyplot(fig_m)

st.divider()

# -----------------------------
# Data Table
# -----------------------------
st.subheader("📋 Customer-Level Data")
st.dataframe(filtered_df.head(50))
