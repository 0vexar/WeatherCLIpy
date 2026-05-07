import requests as r
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("APPID")

endpoints = {
    "search": "https://nominatim.openstreetmap.org/search",
    "current": "https://api.openweathermap.org/data/2.5/weather",
    "r-geocoding": "http://api.openweathermap.org/geo/1.0/reverse"
}

def search(location: str) -> dict:

    headers = {
        'User-Agent': 'WeatherCLI/1.0 (https://github.com/0vexar/WeatherCLIpy; 29huttners@gmail.com)'
    }

    params = {
        "q": location,
        "format": "jsonv2",
        "limit": 1,
        "accept-language": "en",
        "extratags": 1,
        "addressdetails": 1,
    }

    return r.get(endpoints["search"],params,headers=headers).json()[0]

def weather(coordinates:tuple):
    params = {
        "lat": coordinates[0],
        "lon": coordinates[1],
        "units": "metric",
        "appid": token
    }

    response = r.get(endpoints["current"],params).json()

    weather_list = {
        "temp": ( round((response["main"]["temp"]*9/5) + 32) )
    }

    return weather_list