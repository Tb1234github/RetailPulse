import streamlit as st
from prometheus_client import Counter
from prometheus_client import start_http_server

# Start metrics server
start_http_server(8000)

# KPI Counter
REQUEST_COUNT = Counter(
    "retailpulse_requests_total",
    "Total Dashboard Visits"
)

REQUEST_COUNT.inc()

st.set_page_config(
    page_title="RetailPulse",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RetailPulse")

st.markdown("""
### AI-Powered Customer Analytics & Demand Forecasting Platform

#### Features

- EDA Dashboard
- Demand Forecasting
- Customer Segmentation
- Churn Prediction
- Inventory Optimization
- Real-Time Monitoring
- Report Export
""")

st.sidebar.success(
    "Select a module from sidebar"
)