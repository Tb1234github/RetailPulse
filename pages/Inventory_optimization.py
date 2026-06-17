import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Inventory Optimization")

# Load Inventory Data
inventory = pd.read_csv(
    "outputs/inventory_plan.csv"
)

# ==========================
# KPI Metrics
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Products Tracked",
        len(inventory)
    )

with col2:
    st.metric(
        "Average Inventory",
        round(
            inventory["SuggestedInventory"].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Maximum Inventory",
        round(
            inventory["SuggestedInventory"].max(),
            2
        )
    )

# ==========================
# Product Search
# ==========================

st.subheader("🔍 Search Product")

product = st.text_input(
    "Enter Stock Code"
)

if product:
    filtered = inventory[
        inventory["StockCode"]
        .astype(str)
        .str.contains(
            product,
            case=False
        )
    ]

    st.dataframe(filtered)

# ==========================
# Low Stock Alerts
# ==========================

low_stock = inventory[
    inventory["SuggestedInventory"] < 20
]

st.subheader("⚠️ Low Stock Alerts")

if len(low_stock) > 0:

    st.warning(
        f"{len(low_stock)} products require restocking."
    )

    st.dataframe(
        low_stock.head(20)
    )

else:
    st.success(
        "No low-stock products found."
    )

# ==========================
# Inventory Table
# ==========================

st.subheader("📋 Inventory Plan")

st.dataframe(
    inventory.head(20)
)

# ==========================
# Inventory Chart
# ==========================

st.subheader(
    "📊 Recommended Inventory Levels"
)

top_inventory = (
    inventory
    .sort_values(
        "SuggestedInventory",
        ascending=False
    )
    .head(20)
)

fig = px.bar(
    top_inventory,
    x="StockCode",
    y="SuggestedInventory",
    color="SuggestedInventory",
    title="Top 20 Products by Suggested Inventory"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# Download Report
# ==========================

st.subheader("📥 Export Inventory Report")

csv = inventory.to_csv(
    index=False
)

st.download_button(
    label="Download Inventory Report",
    data=csv,
    file_name="inventory_plan.csv",
    mime="text/csv"
)