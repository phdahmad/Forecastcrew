import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI Configuration
st.set_page_config(page_title="ForecastCrow", layout="wide")

# Sample Data: Historical Sales & Future Predictions
dates_past = pd.date_range(start="2024-01-01", periods=30)
sales_past = np.random.randint(80, 200, size=(30,))
dates_future = pd.date_range(start="2024-02-01", periods=14)
sales_future = np.random.randint(150, 250, size=(14,))

df_past = pd.DataFrame({"Date": dates_past, "Sales": sales_past})
df_future = pd.DataFrame({"Date": dates_future, "Sales": sales_future})

# Header with Modern UI Styling
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>📈 ForecastCrow - AI-Powered Sales Forecasting</h1>", unsafe_allow_html=True)

# Forecasting Panel with Clear Future Predictions
st.subheader("📊 Sales Forecasting Overview")
st.write("The blue section represents historical sales, while the **orange section** highlights AI-predicted future sales.")

# Plotting forecast vs. historical data with different colors
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_past["Date"], df_past["Sales"], label="Historical Sales", color="blue", linestyle="-", marker="o")
ax.plot(df_future["Date"], df_future["Sales"], label="AI Forecasted Sales", color="orange", linestyle="--", marker="o")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.legend()
ax.set_title("Sales Forecast")
ax.grid(True)
st.pyplot(fig)

# Inventory Management Panel
st.subheader("📦 AI-Driven Inventory Insights")
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]
restock_needed = [True, False, True, False, True]
inventory_df = pd.DataFrame({"Product": products, "Restock Needed": restock_needed})
st.table(inventory_df)

# AI Chatbot Assistant for Forecast Queries
st.subheader("🤖 AI Chatbot Assistant")
st.write("Ask anything related to sales forecasts (e.g., 'What’s my sales forecast for next week?').")

# Simulated Chatbot Response
user_input = st.text_input("💬 Enter your question here:")
if st.button("Ask AI"):
    response = f"🤖 AI Response: The sales forecast for the next 7 days is approximately {np.sum(sales_future[:7])} units."
    st.success(response)

# API Connectivity Panel
st.subheader("⚡ API Connectivity Status")
st.success("✅ Connected to Salla.sa & Zid APIs")

# AI Insights and Alerts
st.subheader("📢 AI Alerts & Insights")
for i, product in enumerate(products):
    if restock_needed[i]:
        st.warning(f"⚠️ {product} is running low on stock! AI suggests restocking soon.")

# Forecast Period Selection
st.sidebar.header("🔍 Select Forecast Period")
forecast_period = st.sidebar.radio("Choose forecast period:", ["Next 7 days", "Next 14 days", "Next 30 days"])
st.sidebar.write(f"📡 Generating forecast for {forecast_period}...")

# API-Based Inventory Update
if st.sidebar.button("🔄 Sync Inventory with AI"):
    st.sidebar.success("✅ Inventory levels updated automatically!")

st.markdown("<br><p style='text-align: center;'>🚀 Powered by AI & ML - ForecastCrow 2025</p>", unsafe_allow_html=True)
