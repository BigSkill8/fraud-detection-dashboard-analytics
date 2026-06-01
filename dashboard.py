import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("Bank Transaction Fraud Detection Dashboard")

# Load processed dataset
df = pd.read_csv("cleaned_data.csv")

# ----- Key Metrics -----

total_transactions = len(df)
fraud_transactions = df["Class"].sum()
avg_amount = df["Amount"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", total_transactions)
col2.metric("Fraud Transactions", fraud_transactions)
col3.metric("Average Transaction Amount", round(avg_amount, 2))

st.divider()

# ----- Fraud Distribution -----

st.subheader("Fraud vs Normal Transactions")

fraud_counts = df["Class"].value_counts().reset_index()
fraud_counts.columns = ["Class", "Count"]

fig1 = px.bar(
    fraud_counts,
    x="Class",
    y="Count",
    color="Class",
    title="Fraud Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# ----- Transaction Amount Distribution -----

st.subheader("Transaction Amount Distribution")

fig2 = px.histogram(
    df,
    x="Amount",
    nbins=50,
    title="Transaction Amount Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ----- Transactions by Hour -----

st.subheader("Transactions by Hour")

df["Hour"] = (df["Time"] / 3600) % 24

hourly_tx = df.groupby("Hour").size().reset_index(name="Transactions")

fig3 = px.bar(
    hourly_tx,
    x="Hour",
    y="Transactions",
    title="Transactions per Hour"
)

st.plotly_chart(fig3, use_container_width=True)

# ----- Location Visualization -----

if "Latitude" in df.columns and "Longitude" in df.columns:

    st.subheader("Global Transaction Locations")

    fig4 = px.scatter_geo(
        df.head(1000),
        lat="Latitude",
        lon="Longitude",
        color="Class",
        hover_name="Location",
        hover_data=["Amount"],
        projection="orthographic"
    )

    st.plotly_chart(fig4, use_container_width=True)

# ----- Fraud vs Non-Fraud Distribution -----

    st.subheader("Fraud vs Non-Fraud Distribution")

if "Class" in df.columns:   # many fraud datasets use 'Class' (0 = normal, 1 = fraud)
    
    fraud_counts = df["Class"].value_counts()

    labels = ["Normal Transactions", "Fraud Transactions"]

    fig, ax = plt.subplots()
    ax.pie(fraud_counts, labels=labels, autopct='%1.1f%%', startangle=90)

    ax.set_title("Fraud Transaction Distribution")

    st.pyplot(fig)

# ----- Top Suspicious Transactions -----

st.subheader("Top Suspicious Transactions")

top_risky = df.sort_values("Amount", ascending=False).head(20)

st.dataframe(top_risky)

# ----- Raw Data Viewer -----

st.subheader("Transaction Dataset")

st.dataframe(df.head(100))
