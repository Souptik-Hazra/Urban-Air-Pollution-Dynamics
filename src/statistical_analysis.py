import pandas as pd
from scipy.stats import pearsonr

def correlation_matrix(df):
    return df.corr(numeric_only=True)

def pollution_weather_correlation(df):
    results = {}
    variables = ["temp","humidity","wind","pressure"]
    for var in variables:
        corr, _ = pearsonr(df[var], df["components.pm2_5"])
        results[var] = corr
    return results