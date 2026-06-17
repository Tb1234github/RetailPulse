import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔮 Demand Forecasting")

forecast = pd.read_csv(
    "outputs/forecast.csv"
)

st.dataframe(forecast)

fig = px.line(
    forecast,
    x="Date",
    y="Forecast",
    title="30-Day Demand Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("What-If Analysis")

multiplier = st.slider(
    "Demand Growth %",
    0,
    100,
    10
)

forecast["AdjustedForecast"] = (
    forecast["Forecast"]
    * (1 + multiplier/100)
)

st.line_chart(
    forecast.set_index("Date")
    [["AdjustedForecast"]]
)