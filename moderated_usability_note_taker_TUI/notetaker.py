from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Input, Header, Footer, Static


class TimeDisplay(Static):
    """A widget to display elapsed time."""

    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def update_time(self) -> None:
        """Method to update time to current."""
        self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        """Method to start (or resume) time updating."""
        self.start_time = monotonic()
        self.update_timer.resume()

class NoteTakerWidget(Static):
    """A note taking widget"""

    def compose(self) -> ComposeResult:
        """creates child widgets of the NoteWidget."""
        yield Input("", id="note", placeholder="Notes go here.")
        yield Button("Enter", id="enter", variant="success")

class NotetakerApp(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "notetaker.css"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        yield Container(NoteTakerWidget())


if __name__ == "__main__":
    app = NotetakerApp()
    app.run()
