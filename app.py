import streamlit as st

try:
    from prometheus_client import Counter

    REQUEST_COUNT = Counter(
        "streamlit_requests_total",
        "Total Streamlit Requests"
    )

    REQUEST_COUNT.inc()

except Exception:
    pass

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