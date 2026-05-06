from dataclasses import dataclass

@dataclass
class LocationData:
    # Geographic
    city: str
    country: str
    state: str
    lat: float
    lon: float

    # Time
    timezone: str | None

@dataclass
class WeatherData:
    temp_f: int

@dataclass
class DashboardData:
    location: LocationData
    weather: WeatherData
    local_time: str
    license: str
