import pandas as pd

def hourly_trends(df):
    df["hour"] = pd.to_datetime(df["datetime"]).dt.hour
    hourly = df.groupby(["date", "hour"])["components.pm2_5"].mean().reset_index()
    return hourly

def daily_trends(df):
    daily = df.groupby("date")["components.pm2_5"].mean().reset_index()
    return daily

def monthly_trends(df):
    monthly = df.groupby("month")["components.pm2_5"].mean().reset_index()
    return monthly

def seasonal_trends(df):
    seasonal = df.groupby("season")["components.pm2_5"].mean().reset_index()
    return seasonal

def yearly_trends(df):
    yearly = df.groupby("year")["components.pm2_5"].mean().reset_index()
    return yearly