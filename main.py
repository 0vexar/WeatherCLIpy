from src.api import *
from src.clock import *
from typing import TypedDict
import time

from textual import events, on
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Input, Digits, Rule
from textual.containers import Vertical, Horizontal, Center

class WeatherCard(Static):
    def rendermetric(self, label:str, value:str, icon:str):
        self.update(f"{icon} | [$accent blink]{label}[/] - [b]{value}[/b]")

class LocationCard(Static):
    def rendercard(self, city:str, country:str, coords: tuple):
        self.update(f"[b $primary]{city}[/]\n{country}\n{coords}")

class ClassDict(TypedDict):
    location: LocationCard
    temp: WeatherCard

class LocalClock(Digits):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__zone__ = None

    #def on_mount(self):


    def setzone(self, coordinates:tuple):
        self.__zone__ = get_timezone(coordinates)

    #def start(self):


class WeatherCLI(App):

    CSS_PATH = "src/style.tcss"
    BINDINGS = [("q", "quit", "Quit")]

    __coords__ = None
    
    def compose(self) -> ComposeResult:
        
        yield Header(True)
        
        
        with Vertical(id="display-container"):
            with Center():
                yield Static("Enter a city", id="display", classes="start")

        with Horizontal(id="metric-container",classes="hide"):

            # Location Details
            with Vertical(id="details-stack", classes="stack"):
                yield LocalClock(id="clock", classes="details")
                yield LocationCard(id="location-card", classes="details")

            yield Rule("vertical","solid")

            # Current Weather
            with Vertical(id="weather-stack", classes="stack"):
                yield WeatherCard(id="temp",classes="metric")

        yield Input(placeholder="City...",id="city-input")

    def on_mount(self) -> None:
        self.set_interval(1,self.update_clock,pause=True)

    def update_clock(self) -> None:
        local_clock = self.query_one("#clock",LocalClock)

        if isinstance(self.__coords__, tuple):
            tz_str = get_timezone(self.__coords_)

            if tz_str:
                local_clock.setzone(tz_str)

    @on(Input.Submitted, "#city-input")
    def search(self, event: Input.Submitted) -> None:
        city = event.value.strip()
        display = self.query(".hide")
        initial = self.query(".start")
        container: Horizontal = self.query_one("#metric-container",Horizontal)

        if city == "q":
            self.app.exit()

        if city:
            for w in display:
                w.styles.display = "block"

            for w in initial:
                w.styles.display = "none"

            # Initialize Dashboard
            Cards = {
                "location": self.query_one("#location-card",LocationCard),
                "temp": self.query_one("#temp",WeatherCard)
            }

            coordinates, self.__coords__ = coords(city)

            location_info = get_location_details(coordinates)

            current_weather = weather(coordinates)

            Cards["location"].rendercard(location_info["city"],location_info["country"],coordinates)
            Cards["temp"].rendermetric("Temperature",f"{current_weather['temp']}°F","🔥")


        event.input.clear()


    #def on_key(self, event: events.Key) -> None:


if __name__ == "__main__":
    WeatherCLI().run()
