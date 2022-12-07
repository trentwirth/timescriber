from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Input, Header, Footer, Static

# class NoteTakerWidget(Static):
#     """A note taking widget"""

#     def compose(self) -> ComposeResult:
#         """creates child widgets of the NoteWidget."""
#         yield Input("", id="note", placeholder="Notes go here.")
        
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
        yield Container(Input("",id="note",placeholder="Stage 1"))


if __name__ == "__main__":
    app = NotetakerApp()
    app.run()
