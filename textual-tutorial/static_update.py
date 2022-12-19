from textual.app import App, ComposeResult
from textual.widgets import Static

import uuid

class TextDisplay(Static):

    text = 'start'
    print(text)

    def update_text(self) -> None:
        """Method to update text."""
        self.text = uuid.uuid4()
        print(self.text)

class TextApp(App):

    CSS_PATH = "static_update.css"

    def key_space(self):
        TextDisplay.update_text()

    def compose(self) -> ComposeResult:
        yield TextDisplay()