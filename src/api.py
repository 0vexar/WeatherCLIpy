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
    }

    if "state" in response[0]:
        return_list["state"] = response[0]["state"]

    if "local_names" in response[0]["local_names"]:
        return_list["city"] = response[0]["local_names"]["en"]
    else:
        return_list["city"] = response[0]["name"]

    return return_list