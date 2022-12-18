from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual.widgets import Input
from textual import events

import time


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class InputApp(Input):
    async def get_text(self) -> str:
        return self.Changed.bubble

class Minutes(TextLog):

    def on_input_submit(self, event: Input.Submitted) -> None:
        self.write(get_timestamp())
        self.write(time.time())
        self.write(event.__str__)


    def key_enter(self) -> None:
        self.write(get_timestamp())
        self.write(time.time())
        self.write("Text will go here.")
    

class MinutesApp(App):
    """Description goes here."""

    CSS_PATH = "minutes.css"

    def compose(self) -> ComposeResult:
        yield InputApp(classes="input_box")
        yield Minutes()


if __name__ == "__main__":
    app = MinutesApp()
    app.run()
