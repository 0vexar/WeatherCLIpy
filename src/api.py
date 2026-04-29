import requests as r
import os
from dotenv import load_dotenv

token = os.getenv("APPID")

endpoints = {
    "search": "http://api.openweathermap.org/geo/1.0/direct",
    "current": "https://api.openweathermap.org/data/2.5/weather"
}

def coords(location: str):
    params = {
        "q": location,
        "appid": token
    }

    return r.get(endpoints["search"],params)

def weather(lat: int,lon: int):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": token
    }

    return r.get(endpoints["current"],params)

print(token)