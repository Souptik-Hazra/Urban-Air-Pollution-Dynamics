import pandas as pd
import numpy as np

def create_features(df):
    """
    Add engineered features to DataFrame for modeling and analysis.
    """
    df["pm25_pm10_ratio"] = df["components.pm2_5"] / (df["components.pm10"] + 1)
    df["no2_pm25_ratio"] = df["components.no2"] / (df["components.pm2_5"] + 1)
    df["co_pm25_ratio"] = df["components.co"] / (df["components.pm2_5"] + 1)
    return df.dropna()