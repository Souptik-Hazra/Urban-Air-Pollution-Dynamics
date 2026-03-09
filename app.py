import streamlit as st
import plotly.graph_objects as go

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
    # Merge on both date and hour for hourly analysis
    if not pollution.empty and not weather.empty:
        df = pollution.merge(weather, on=["date", "hour"], how="inner")
        df = create_features(df)
        # Remove minute-related columns if present
        for col in ["minute", "minutex", "miny", "minute_x", "minute_y"]:
            if col in df.columns:
                df = df.drop(columns=col)
        df = df.dropna()
        st.subheader("Dataset")
        st.dataframe(df)
        st.subheader("Time Series")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["date"], y=df["components.pm2_5"], mode="lines", name="PM2.5"))
        st.plotly_chart(fig, key="time_series")
        st.subheader("Correlation")
        corr = correlation_matrix(df)
        fig_corr = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns, y=corr.index))
        st.plotly_chart(fig_corr, key="correlation")
        st.subheader("Pollution Clusters")
        cluster_df = pollution_clusters(df)
        fig_cluster = go.Figure()
        for cluster in cluster_df['cluster'].unique():
            cluster_data = cluster_df[cluster_df['cluster'] == cluster]
            fig_cluster.add_trace(go.Scatter3d(
                x=cluster_data['components.pm2_5'],
                y=cluster_data['components.pm10'],
                z=cluster_data['components.no2'],
                mode='markers',
                name=f'Cluster {cluster}',
                marker=dict(
                    size=6,
                    opacity=0.85,
                    color=cluster_data['components.pm2_5'],
                    colorscale='Viridis',
                    line=dict(
                        color='black',
                        width=1
                    )
                ),
                text=cluster_data['cluster'],
                hoverinfo='text'
            ))
        fig_cluster.update_layout(
            scene=dict(
                xaxis_title='PM2.5',
                yaxis_title='PM10',
                zaxis_title='NO2',
                bgcolor='rgb(20,20,20)'
            ),
            title='Pollution Clusters (3D)',
            paper_bgcolor='rgb(20,20,20)',
            plot_bgcolor='rgb(20,20,20)'
        )
        st.plotly_chart(fig_cluster, key="clusters")
        st.subheader("Regression Model")
        reg_df, model = train_model(df)
        fig_reg = go.Figure()
        fig_reg.add_trace(go.Scatter(x=reg_df["date"], y=reg_df["components.pm2_5"], mode="lines", name="PM2.5"))
        fig_reg.add_trace(go.Scatter(x=reg_df["date"], y=reg_df["prediction"], mode="lines", name="Prediction"))
        fig_reg.update_layout(title="Regression Model")
        st.plotly_chart(fig_reg, key="regression")
        from src.temporal_analysis import hourly_trends, daily_trends, monthly_trends, seasonal_trends, yearly_trends
        st.subheader("Hourly PM2.5 Trends")
        hourly = hourly_trends(df)
        hourly_pivot = hourly.pivot(index="hour", columns="date", values="components.pm2_5")
        fig_hourly = go.Figure(data=go.Heatmap(z=hourly_pivot.values, x=hourly_pivot.columns, y=hourly_pivot.index))
        fig_hourly.update_layout(title="Hourly PM2.5 Heatmap")
        st.plotly_chart(fig_hourly, key="hourly")
        st.subheader("Daily PM2.5 Trends")
        daily = daily_trends(df)
        fig_daily = go.Figure()
        fig_daily.add_trace(go.Scatter(x=daily["date"], y=daily["components.pm2_5"], mode="lines", name="Daily PM2.5"))
        fig_daily.update_layout(title="Daily PM2.5")
        st.plotly_chart(fig_daily, key="daily")
        st.subheader("Monthly PM2.5 Trends")
        monthly = monthly_trends(df)
        fig_monthly = go.Figure()
        fig_monthly.add_trace(go.Scatter(x=monthly["month"], y=monthly["components.pm2_5"], mode="lines", name="Monthly PM2.5"))
        fig_monthly.update_layout(title="Monthly PM2.5")
        st.plotly_chart(fig_monthly, key="monthly")

        st.subheader("Seasonal PM2.5 Trends")
        season = seasonal_trends(df)
        fig_season = go.Figure()
        fig_season.add_trace(go.Bar(x=season["season"], y=season["components.pm2_5"], name="Seasonal PM2.5"))
        fig_season.update_layout(title="Seasonal PM2.5")
        st.plotly_chart(fig_season)
        st.subheader("Yearly PM2.5 Trends")
        yearly = yearly_trends(df)
        fig_yearly = go.Figure()
        fig_yearly.add_trace(go.Scatter(x=yearly["year"], y=yearly["components.pm2_5"], mode="lines", name="Yearly PM2.5"))
        fig_yearly.update_layout(title="Yearly PM2.5")
        st.plotly_chart(fig_yearly, key="yearly")
        st.subheader("Pollution Map")
        st.plotly_chart(pollution_map(df, lat, lon), key="map")
    else:
        st.error("No data available for selected city or time period.")
