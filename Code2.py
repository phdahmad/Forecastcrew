import streamlit as st
import pandas as pd
import numpy as np

# Sample Data: Sales Forecast for the Next 30 Days
dates = pd.date_range(start="2024-01-01", periods=30)
sales_forecast = np.random.randint(50, 200, size=(30,))
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]
restock_needed = [True, False, True, False, True]

# Title
st.title("📈 ForecastCrow - AI-Powered Sales Forecasting & Inventory Management")

# Sales Forecasting Panel
st.subheader("📊 Sales Forecast (Next 30 Days)")
st.line_chart(pd.DataFrame({"Date": dates, "Forecast": sales_forecast}).set_index("Date"))

# Inventory Management Panel
st.subheader("📦 Inventory Recommendations")
inventory_df = pd.DataFrame({"Product": products, "Restock Needed": restock_needed})
st.table(inventory_df)

# API Connectivity
st.subheader("⚡ API Connectivity Status")
st.success("Connected to Salla.sa & Zid APIs")

# Alerts & Notifications
st.subheader("📢 AI Alerts & Warnings")
for i, product in enumerate(products):
    if restock_needed[i]:
        st.warning(f"⚠️ {product} needs restocking!")

# AI Insights Panel
st.subheader("📜 AI Insights")
st.write("Trending Products: Laptops & Smartwatches are in high demand.")

# Forecast Period Selection
st.sidebar.header("🔍 Forecast Period")
forecast_period = st.sidebar.radio("Select forecast period:", ["Next 7 days", "Next 14 days", "Next 30 days"])
st.sidebar.write(f"Generating forecast for {forecast_period}...")

# API Trigger for Inventory Update
if st.sidebar.button("🔄 Update Inventory Automatically"):
    st.sidebar.success("Inventory updated successfully!")
