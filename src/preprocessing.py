import pandas as pd

def preprocess_pollution(records):
    df = pd.json_normalize(records)
    df["datetime"] = pd.to_datetime(df["dt"], unit="s")
    df["date"] = df["datetime"].dt.date
    pollutants = [
        "components.pm2_5",
        "components.pm10",
        "components.no2",
        "components.so2",
        "components.co",
        "components.o3"
    ]
    daily = df.groupby("date")[pollutants].mean().reset_index()
    return daily