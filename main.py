from src.api import coords, weather

from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, ContentSwitcher, Input

class WeatherCLI(App):

    CSS_PATH = "src/style.tcss"
    
    def compose(self) -> ComposeResult:
        
        yield Header(True)
        
        
        with ContentSwitcher(id="main",classes="top", initial="data"):
            yield Static("Input city", id="data", expand=True)

        yield Input(placeholder="City...",id="input")

    def on_key(self, event: events.Key) -> None:
        match event.key:
            case "q":
                self.exit()


if __name__ == "__main__":
    WeatherCLI().run()