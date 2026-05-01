import requests as r
import os, iso3166
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("APPID")

endpoints = {
    "search": "http://api.openweathermap.org/geo/1.0/direct",
    "current": "https://api.openweathermap.org/data/2.5/weather",
    "r-geocoding": "http://api.openweathermap.org/geo/1.0/reverse"
}

def coords(location: str):
    params = {
        "q": location,
        "appid": token
    }

    response = r.get(endpoints["search"],params).json()[0]

    return (response["lat"], response["lon"])

def weather(lat: float,lon: float):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": token
    }

    return r.get(endpoints["current"],params)

def get_location_details(coordinates: tuple):
    params = {
        "lat": coordinates[0],
        "lon": coordinates[1],
        "appid": token
    }

    response = r.get(endpoints["r-geocoding"],params).json()

    return_list = {
        "city": response[0]["local_names"]["en"],
        "country": iso3166.countries.get(response[0]["country"]).name,
        "state": response[0]["state"]
    }

    return return_list