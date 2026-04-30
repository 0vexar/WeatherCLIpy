from src.api import coords, weather

from textual import events, on
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, ContentSwitcher, Input
from textual.containers import Vertical, Horizontal, Center

class WeatherCLI(App):

    CSS_PATH = "src/style.tcss"
    BINDINGS = [("q", "quit", "Quit")]
    
    def compose(self) -> ComposeResult:
        
        yield Header(True)
        
        
        with Vertical(id="weather-container"):
            with Center():
                yield Static("Enter a city", id="display")


        yield Input(placeholder="City...",id="city-input")

    @on(Input.Submitted, "#city-input")
    def search(self, event: Input.Submitted) -> None:
        city = event.value.strip()
        display: Static = self.query_one("#display",Static)
        if city:
            display.update(city)
        event.input.clear()


    #def on_key(self, event: events.Key) -> None:


if __name__ == "__main__":
    WeatherCLI().run()