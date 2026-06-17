import pandas as pd
import plotly.express as px
import streamlit as st

st.title("📈 EDA Dashboard")

df = pd.read_excel(
    "data/online_retail_II.xlsx"
)

st.dataframe(
    df.head()
)

st.write(
    df.describe()
)

missing = df.isnull().sum()

fig = px.bar(
    x=missing.index,
    y=missing.values,
    title="Missing Values"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

sales = (
    df.groupby("InvoiceDate")
    ["Quantity"]
    .sum()
    .reset_index()
)

fig = px.line(
    sales,
    x="InvoiceDate",
    y="Quantity",
    title="Sales Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)