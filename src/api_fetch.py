import requests
import pandas as pd
import time

API_KEY = "dd0c18b04802ed759e2be4594083c862"

OWM_URL = "https://api.openweathermap.org/data/2.5/air_pollution/history"
OPEN_METEO_URL = "https://archive-api.open-meteo.com/v1/archive"
WEATHER_VARS = "temperature_2m,relative_humidity_2m,wind_speed_10m,surface_pressure,precipitation,cloud_cover"

def geocode_city(city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    r = requests.get(url, params={
        "q": city,
        "limit": 1,
        "appid": API_KEY
    })
    data = r.json()
    if not data:
        return None, None
    return data[0]["lat"], data[0]["lon"]

def fetch_pollution(lat, lon, days=90):
    end = int(time.time())
    start = end - days * 86400
    records = []
    chunk = 5 * 24 * 3600
    current = start
    while current < end:
        chunk_end = min(current + chunk, end)
        r = requests.get(OWM_URL, params={
            "lat": lat,
            "lon": lon,
            "start": current,
            "end": chunk_end,
            "appid": API_KEY
        })
        data = r.json()
        if "list" in data:
            records.extend(data["list"])
        current = chunk_end
        time.sleep(0.2)
    return records

def fetch_weather(lat, lon, start, end):
    try:
        r = requests.get(OPEN_METEO_URL, params={
            "latitude": lat,
            "longitude": lon,
            "start_date": start,
            "end_date": end,
            "hourly": WEATHER_VARS,
            "timezone": "auto"
        })
        r.raise_for_status()
        data = r.json()
        hourly = data["hourly"]
        df = pd.DataFrame({
            "time": pd.to_datetime(hourly["time"]),
            "temp": hourly["temperature_2m"],
            "humidity": hourly["relative_humidity_2m"],
            "wind": hourly["wind_speed_10m"],
            "pressure": hourly["surface_pressure"],
            "precip": hourly["precipitation"],
            "cloud": hourly["cloud_cover"]
        })
        df["date"] = df["time"].dt.date
        df["hour"] = df["time"].dt.hour
        df["minute"] = df["time"].dt.minute
        return df
    except Exception as e:
        print(f"Weather API error: {e}")
        return pd.DataFrame()