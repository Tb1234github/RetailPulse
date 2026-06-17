import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Real-Time Business Metrics")

# Load Data
forecast = pd.read_csv(
    "outputs/forecast.csv"
)

inventory = pd.read_csv(
    "outputs/inventory_plan.csv"
)

# ==========================
# KPI SECTION
# ==========================

forecast_revenue = round(
    forecast["Forecast"].sum(),
    2
)

products_tracked = len(
    inventory
)

low_stock = len(
    inventory[
        inventory["SuggestedInventory"] < 20
    ]
)

inventory_health = round(
    (
        (products_tracked - low_stock)
        / products_tracked
    ) * 100,
    2
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Forecasted Revenue",
        f"${forecast_revenue:,.2f}"
    )

with col2:
    st.metric(
        "Products Tracked",
        products_tracked
    )

with col3:
    st.metric(
        "Low Stock Alerts",
        low_stock
    )

with col4:
    st.metric(
        "Inventory Health %",
        f"{inventory_health}%"
    )

# ==========================
# ALERTS
# ==========================

st.subheader("⚠️ Inventory Alerts")

if low_stock > 0:
    st.warning(
        f"{low_stock} products require immediate attention."
    )

    low_stock_products = inventory[
        inventory["SuggestedInventory"] < 20
    ]

    st.dataframe(
        low_stock_products.head(20)
    )

else:
    st.success(
        "Inventory levels are healthy."
    )

# ==========================
# FORECAST TREND
# ==========================

st.subheader(
    "📊 Revenue Forecast Trend"
)

fig = px.line(
    forecast,
    x="Date",
    y="Forecast",
    title="Forecasted Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# INVENTORY DISTRIBUTION
# ==========================

st.subheader(
    "📦 Inventory Distribution"
)

top_inventory = (
    inventory
    .sort_values(
        "SuggestedInventory",
        ascending=False
    )
    .head(20)
)

fig2 = px.bar(
    top_inventory,
    x="StockCode",
    y="SuggestedInventory",
    title="Top 20 Inventory Requirements"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================
# DOWNLOAD REPORT
# ==========================

st.subheader(
    "📥 Export Metrics Report"
)

csv = inventory.to_csv(
    index=False
)

st.download_button(
    label="Download Inventory Report",
    data=csv,
    file_name="inventory_plan.csv",
    mime="text/csv"
)