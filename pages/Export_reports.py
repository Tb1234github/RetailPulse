import streamlit as st
import pandas as pd

st.title("📥 Export Reports")

forecast = pd.read_csv(
    "outputs/forecast.csv"
)

inventory = pd.read_csv(
    "outputs/inventory_plan.csv"
)

customers = pd.read_csv(
    "outputs/churn_customers.csv"
)

st.download_button(
    "Download Forecast Report",
    forecast.to_csv(index=False),
    "forecast.csv"
)

st.download_button(
    "Download Inventory Report",
    inventory.to_csv(index=False),
    "inventory_plan.csv"
)

st.download_button(
    "Download Churn Report",
    customers.to_csv(index=False),
    "churn_customers.csv"
)