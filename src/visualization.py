import plotly.graph_objects as go

def pollution_map(df, lat, lon):
    df["lat"] = lat
    df["lon"] = lon
    fig = go.Figure(go.Scattermapbox(
        lat=df["lat"],
        lon=df["lon"],
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=df["components.pm2_5"],
            color=df["components.pm2_5"],
            colorscale="Viridis",
            showscale=True
        ),
        text=df["components.pm2_5"],
        hoverinfo="text"
    ))
    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            zoom=5,
            center=dict(lat=lat, lon=lon)
        ),
        margin={"r":0,"t":0,"l":0,"b":0}
    )
    return fig