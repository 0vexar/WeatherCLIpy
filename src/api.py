import requests as r

token = "e05a162b9fc1471e09cc6275bf34bb70"

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