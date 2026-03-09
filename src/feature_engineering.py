import pandas as pd
import numpy as np

def create_features(df):
    df["month"] = pd.to_datetime(df["date"]).dt.month
    df["day_of_week"] = pd.to_datetime(df["date"]).dt.dayofweek
    df["pm25_lag1"] = df["components.pm2_5"].shift(1)
    df["pm25_lag2"] = df["components.pm2_5"].shift(2)
    df["pm25_roll7"] = df["components.pm2_5"].rolling(7).mean()
    df["pm25_pm10_ratio"] = df["components.pm2_5"] / (df["components.pm10"] + 1)
    return df.dropna()