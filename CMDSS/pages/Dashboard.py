import streamlit as st
import pandas as pd
from utils.db_handler import fetch_sales_data
from utils.processor import generate_historical_insights

st.title("📊 Smart Dashboard")

if "owner_id" not in st.session_state:
    st.error("Please login")
    st.stop()

df = fetch_sales_data(st.session_state["owner_id"])

if df.empty:
    st.warning("No historical sales data")
    st.stop()

# Ensure correct data types
df["quantity"] = df["quantity"].astype(int)
df["date"] = pd.to_datetime(df["date"])

# Metrics
st.subheader("📈 Overall Performance")
st.metric("Total Units Sold", df["quantity"].sum())

# Insights
st.subheader("🔍 Insights from Past Data")
try:
    insights = generate_historical_insights(df)
    for insight in insights:
        st.success(insight)
except:
    st.warning("Could not generate insights")

# Item-wise Sales
st.subheader("📦 Item-wise Sales")
st.bar_chart(df.groupby("item")["quantity"].sum())

# Daily Trend
st.subheader("📅 Daily Sales Trend")
st.line_chart(df.groupby("date")["quantity"].sum())
