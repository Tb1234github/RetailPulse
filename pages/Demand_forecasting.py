import pandas as pd
import plotly.express as px
import streamlit as st

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

st.subheader("🔮 Prophet Forecast")

fig = px.line(
    forecast,
    x="Date",
    y="Forecast",
    title="30-Day Prophet Demand Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("🚀 Hybrid Forecast")

hybrid = pd.read_csv(
    "outputs/hybrid_forecast.csv"
)

fig = px.line(
    hybrid,
    x="Date",
    y="HybridForecast",
    title="Hybrid Prophet + LSTM Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("📊 Forecast KPIs")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Forecast Demand",
        round(
            forecast["Forecast"].sum(),
            0
        )
    )

with col2:
    st.metric(
        "Average Daily Demand",
        round(
            forecast["Forecast"].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Peak Forecast Demand",
        round(
            forecast["Forecast"].max(),
            2
        )
    )
    st.subheader("📈 What-If Analysis")

multiplier = st.slider(
    "Demand Growth %",
    -50,
    100,
    10
)

forecast["AdjustedForecast"] = (
    forecast["Forecast"]
    * (1 + multiplier / 100)
)

fig = px.line(
    forecast,
    x="Date",
    y=[
        "Forecast",
        "AdjustedForecast"
    ],
    title="Forecast vs What-If Scenario"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.download_button(
    label="📥 Download Forecast Report",
    data=forecast.to_csv(index=False),
    file_name="forecast_report.csv",
    mime="text/csv"
)