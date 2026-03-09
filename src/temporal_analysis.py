import pandas as pd

def seasonal_trends(df):
    df["month"] = pd.to_datetime(df["date"]).dt.month
    seasonal = df.groupby("month")["components.pm2_5"].mean().reset_index()
    return seasonal