from src.api import *
from src.clock import *
from src.services import build_dashboard

from typing import TypedDict
import time

from textual import events, on
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Input, Digits, Rule
from textual.reactive import reactive  
from textual.containers import Vertical, Horizontal, Center

class LocalClock(Digits):
    timezone: reactive[str | None] = reactive(None)

    def on_mount(self) -> None:
        self.timer = self.set_interval(1, self.update_time, pause=True)

    def set_location(self, coordinates: tuple[float, float]) -> None:
        self.timezone = get_timezone(coordinates)

        if self.timezone:
            self.update_time()

    def update_time(self) -> None:
        if not self.timezone:
            self.update("--:--:--")
            return
        
        self.update(get_time(self.timezone))

class WeatherCard(Static):
    def rendermetric(self, label:str, value:str, icon:str):
        self.update(f"{icon} | [$accent blink]{label}[/] - [b]{value}[/b]")

class LocationCard(Static):
    def rendercard(self, city:str, country:str, lat: float, lon: float):
        self.update(f"[b $primary]{city}[/]\n{country}\n[b $accent]{lat}[/] | [b $accent]{lon}[/]")

class ClassDict(TypedDict):
    location: LocationCard
    temp: WeatherCard


class WeatherCLI(App):

    CSS_PATH = "src/style.tcss"
    BINDINGS = [("q", "quit", "Quit")]
    
    def compose(self) -> ComposeResult:
        
        yield Header()
        
        
        with Vertical(id="display-container"):
            with Center():
                yield Static("Enter a location", id="display", classes="start")

        with Horizontal(id="metric-container",classes="hide"):

            # Location Details
            with Vertical(id="details-stack", classes="stack"):
                yield Static(id="license", classes="details card")

                yield LocalClock(id="local-clock", classes="details card")
                yield LocationCard(id="location-card", classes="details card")

            yield Rule("vertical","dashed", classes="hide")

            # Current Weather
            with Vertical(id="weather-stack", classes="stack"):
                yield WeatherCard(id="temp",classes="metric card")

        yield Input(placeholder="Any location...",id="location-input")

    def on_mount(self) -> None:
        clock = self.query_one("#local-clock", LocalClock)

        clock.timer.resume()

    @on(Input.Submitted, "#location-input")
    def search(self, event: Input.Submitted) -> None:
        city = event.value.strip()
        display = self.query(".hide")
        initial = self.query(".start")
        container: Horizontal = self.query_one("#metric-container",Horizontal)

        if city == "q":
            self.app.exit()

        if city:

            # Set Display

            for w in display:
                w.styles.display = "block"

            for w in initial:
                w.styles.display = "none"

            # Initialize Dashboard

            Cards = {
                "location": self.query_one("#location-card",LocationCard),
                "temp": self.query_one("#temp",WeatherCard)
            }

            dashboard = build_dashboard(city)

            # Query Widgets

            clock = self.query_one("#local-clock",LocalClock)
            static_license = self.query_one("#license",Static)

            clock.set_location((dashboard.location.lat, dashboard.location.lon))

            Cards["location"].rendercard(
                dashboard.location.city,
                dashboard.location.country,
                dashboard.location.lat,
                dashboard.location.lon,
            )
            Cards["temp"].rendermetric("Temperature",f"{dashboard.weather.temp_f}°F","🔥")

            static_license.update(f"[i]{dashboard.license}[/]")




        event.input.clear()


    #def on_key(self, event: events.Key) -> None:


if __name__ == "__main__":
    WeatherCLI().run()
