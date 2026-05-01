from src.api import *
from typing import TypedDict
import time

from textual import events, on
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, ContentSwitcher, Input
from textual.containers import Vertical, Horizontal, Center

class WeatherCard(Static):
    def rendermetric(self, label:str, value:str, icon:str):
        self.update(f"{icon} | [$accent][blink]{label}[/][/] - [b]{value}[/b]")

class LocationCard(Static):
    def rendercard(self, city:str, country:str, coords: tuple):
        self.update(f"[b $primary]{city}[/]\n{country} | {coords}")

class ClassDict(TypedDict):
    location: LocationCard
    temp: WeatherCard

class WeatherCLI(App):

    CSS_PATH = "src/style.tcss"
    BINDINGS = [("q", "quit", "Quit")]
    
    def compose(self) -> ComposeResult:
        
        yield Header(True)
        
        
        with Vertical(id="display-container"):
            with Center():
                yield Static("Enter a city", id="display", classes="start")

        with Horizontal(id="metric-container",classes="hide"):
            yield LocationCard(id="location-card")
            yield WeatherCard(id="temp",classes="metric")

        #with Horizontal(classes="hide"):
            #yield Static("Hi")

        yield Input(placeholder="City...",id="city-input")

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

            coordinates = coords(city)

            location_info = get_location_details(coordinates)

            Cards["location"].rendercard(location_info["city"],location_info["country"],coordinates)
            Cards["temp"].rendermetric("Temperature",f"Value","🔥")


        event.input.clear()


    #def on_key(self, event: events.Key) -> None:


if __name__ == "__main__":
    WeatherCLI().run()
