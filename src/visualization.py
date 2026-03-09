import plotly.express as px

def pollution_map(df, lat, lon):
    df["lat"] = lat
    df["lon"] = lon
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        color="components.pm2_5",
        size="components.pm2_5",
        zoom=5,
        mapbox_style="open-street-map"
    )
    return fig