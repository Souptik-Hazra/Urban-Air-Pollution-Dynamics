from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    features = [
        "temp",
        "humidity",
        "wind",
        "pressure"
    ]
    X = df[features]
    y = df["components.pm2_5"]
    model = RandomForestRegressor()
    model.fit(X, y)
    df["prediction"] = model.predict(X)
    return df, model