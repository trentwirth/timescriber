from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual import events

import time


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class KeyLogger(TextLog):
    def on_key(self, event: events.Key) -> None:
        self.write(get_timestamp())
        self.write(time.time())
        self.write(event)


class InputApp(App):
    """App to display key events."""

    CSS_PATH = "key03.css"

    def compose(self) -> ComposeResult:
        yield KeyLogger()
        yield KeyLogger()
        yield KeyLogger()
        yield KeyLogger()


if __name__ == "__main__":
    app = InputApp()
    app.run()
