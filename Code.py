import streamlit as st
import pandas as pd
import numpy as np

# Sample Forecast Data
dates = pd.date_range(start="2024-01-01", periods=30)
sales_forecast = np.random.randint(50, 200, size=(30,))

# Dashboard UI
st.title("📈 ForecastCrow - AI Sales Forecasting & Inventory Optimization")

st.subheader("🔹 Sales Forecast for Next 30 Days")
st.line_chart(pd.DataFrame({"Date": dates, "Forecast": sales_forecast}).set_index("Date"))

st.subheader("📦 Inventory Recommendations")
st.write("Based on AI analysis, consider restocking the following products:")
inventory_data = {"Product": ["Laptop", "Smartphone", "Tablet"], "Restock Quantity": [50, 100, 75]}
st.table(pd.DataFrame(inventory_data))

st.subheader("⚡ API Connectivity Status")
st.success("Connected to Salla.sa & Zid APIs")

st.sidebar.header("🔍 Select Product")
selected_product = st.sidebar.selectbox("Choose a product:", ["Laptop", "Smartphone", "Tablet"])
st.sidebar.write(f"AI Prediction for {selected_product}: {np.random.randint(100, 300)} units needed")

st.sidebar.button("Update Inventory Automatically ✅")
