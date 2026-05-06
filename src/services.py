from src.api import search, weather
from src.clock import get_timezone, get_time
from src.models import DashboardData, LocationData, WeatherData

def build_dashboard(city: str) -> DashboardData:
    # 1. Fetch raw data
    search_results = search(city)
    lat, lon = search_results["lat"], search_results["lon"]
    address = search_results["address"]

    # 2. Derive secondary data
    weather_info = weather((lat, lon))
    timezone = get_timezone((lat, lon))
    local_time = get_time(timezone) if timezone else "--:--:--"

    # 3. Map to structured models
    location = LocationData(
        city=address.get("city") or address.get("town") or address.get("village") or "N/A",
        country=address.get("country", "No Country"),
        state=address.get("state") or address.get("province") or address.get("region") or "N/A",
        lat=lat,
        lon=lon,
        timezone=timezone
    )

    return DashboardData(
        location=location,
        weather=WeatherData(temp_f=weather_info["temp"]),
        local_time=local_time,
        license=search_results.get('licence') # type: ignore
    )