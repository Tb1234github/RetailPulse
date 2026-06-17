import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Customer Analytics")

customers = pd.read_csv(
    "outputs/churn_customers.csv"
)

st.metric(
    "Total Customers",
    len(customers)
)

st.metric(
    "Churn Risk Customers",
    customers["Churn"].sum()
)

fig = px.scatter(
    customers,
    x="Frequency",
    y="Monetary",
    color="Churn",
    title="Customer Churn Risk"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    customers.head()
)