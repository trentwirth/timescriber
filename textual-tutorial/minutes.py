from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual.widgets import Input
from textual import events

import time


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class Minutes(TextLog):
    def key_enter(self) -> None:
        self.write(get_timestamp())
        self.write(time.time())
        self.write(Input.Changed.bubble.value)
        


class MinutesApp(App):
    """Description goes here."""

    CSS_PATH = "minutes.css"

    def compose(self) -> ComposeResult:
        yield Input(classes="input_box")
        yield Minutes()


if __name__ == "__main__":
    app = MinutesApp()
    app.run()
