import streamlit as st
import plotly.express as px

from src.api_fetch import geocode_city, fetch_pollution, fetch_weather
from src.preprocessing import preprocess_pollution
from src.feature_engineering import create_features
from src.statistical_analysis import correlation_matrix
from src.clustering import pollution_clusters
from src.regression_model import train_model
from src.temporal_analysis import seasonal_trends
from src.visualization import pollution_map

st.title("Urban Air Pollution Research Dashboard")

city = st.text_input("Enter City")

if city:
    lat, lon = geocode_city(city)
    records = fetch_pollution(lat, lon)
    pollution = preprocess_pollution(records)
    start = pollution["date"].min().strftime("%Y-%m-%d")
    end = pollution["date"].max().strftime("%Y-%m-%d")
    weather = fetch_weather(lat, lon, start, end)
    df = pollution.merge(weather, on="date")
    df = create_features(df)
    st.subheader("Dataset")
    st.dataframe(df)
    st.subheader("Time Series")
    st.plotly_chart(
        px.line(df, x="date", y="components.pm2_5")
    )
    st.subheader("Correlation")
    corr = correlation_matrix(df)
    st.plotly_chart(px.imshow(corr))
    st.subheader("Pollution Clusters")
    cluster_df = pollution_clusters(df)
    st.plotly_chart(
        px.scatter(
            cluster_df,
            x="components.pm2_5",
            y="components.pm10",
            color="cluster"
        )
    )
    st.subheader("Regression Model")
    reg_df, model = train_model(df)
    st.plotly_chart(
        px.line(
            reg_df,
            x="date",
            y=["components.pm2_5","prediction"]
        )
    )
    st.subheader("Seasonal Trends")
    season = seasonal_trends(df)
    st.plotly_chart(
        px.line(season, x="month", y="components.pm2_5")
    )
    st.subheader("Pollution Map")
    st.plotly_chart(pollution_map(df, lat, lon))