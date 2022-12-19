from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual.widgets import Input
from textual.widgets import Static
from textual import events

import time


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class InputApp(Input):

    class Debug_Print():

        def debug_print() -> None:
            print('debug-001')

    def key_enter(self) -> None:

        print(self.value)

        Minutes.log_minutes(TextLog, self.value)

        # Clear the text input
        self.value = ''

        InputApp.Debug_Print.debug_print()

class Minutes(TextLog):

        def log_minutes(self, s: str|int) -> None:
            print(get_timestamp())
            self.write(get_timestamp())
            self.write(time.time())
            self.write(s)

            print('In log_minutes')


class MinutesApp(App):
    """Description goes here."""

    CSS_PATH = "minutes.css"

    def compose(self) -> ComposeResult:
        yield InputApp(classes="input_box")
        yield Minutes()


if __name__ == "__main__":
    app = MinutesApp()
    app.run()
