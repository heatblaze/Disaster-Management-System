import requests

# API Keys
WEATHER_API_KEY = "your_openweathermap_api_key"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
ALERTS_URL = "https://api.openweathermap.org/data/3.0/onecall"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY
    }
    response = requests.get(WEATHER_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']
        temp = data['main']['temp'] - 273.15  # Kelvin to Celsius
        return weather, temp
    else:
        return None, None

def fetch_alerts(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": WEATHER_API_KEY
    }
    response = requests.get(ALERTS_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        alerts = data.get('alerts', [])
        return alerts
    return []
