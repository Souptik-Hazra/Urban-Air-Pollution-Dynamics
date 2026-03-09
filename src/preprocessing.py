import pandas as pd

def preprocess_pollution(records):
    """
    Normalize pollution records and extract calendar/time features.
    Handles missing values and returns DataFrame.
    """
    df = pd.json_normalize(records)
    df["datetime"] = pd.to_datetime(df["dt"], unit="s")
    df["date"] = df["datetime"].dt.date
    df["hour"] = df["datetime"].dt.hour
    df["minute"] = df["datetime"].dt.minute
    df["time"] = df["datetime"].dt.time
    df["day_of_week"] = df["datetime"].dt.dayofweek
    df["is_weekend"] = df["day_of_week"].isin([5,6])
    df["month"] = df["datetime"].dt.month
    df["year"] = df["datetime"].dt.year
    df["season"] = df["month"].map({
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Spring", 4: "Spring", 5: "Spring",
        6: "Summer", 7: "Summer", 8: "Summer",
        9: "Autumn", 10: "Autumn", 11: "Autumn"
    })
    pollutants = [
        "components.pm2_5",
        "components.pm10",
        "components.no2",
        "components.so2",
        "components.co",
        "components.o3"
    ]
    df = df[pollutants + ["datetime","date","hour","minute","time","day_of_week","is_weekend","month","year","season"]]
    df = df.dropna()
    return df