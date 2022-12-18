from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Input, Header, Footer, Static

import pathlib as Path

# class NoteTakerWidget(Static):
#     """A note taking widget"""

def compose(self) -> ComposeResult:
    """creates child widgets of the NoteWidget."""
    yield Input("", id="note", placeholder="Notes go here.")

def line_writer(line: str, file_path: Path):
    with open(file_path,'a') as file:
        file.write(line)
        file.write('\n')

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
