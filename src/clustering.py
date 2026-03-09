from sklearn.cluster import DBSCAN

def pollution_clusters(df):
    features = df[
        [
            "components.pm2_5",
            "components.pm10",
            "components.no2",
            "components.co"
        ]
    ]
    model = DBSCAN(eps=5, min_samples=3)
    df["cluster"] = model.fit_predict(features)
    return df