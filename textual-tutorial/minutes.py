from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual.widgets import Input
from textual import events

import time


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class Minutes(TextLog):

    async def key_enter(self, s: str|int) -> None:
        self.write(get_timestamp())
        self.write(time.time())
        self.write(s)

class InputApp(Input):

    async def key_enter(self) -> None:

        print('Printing text for debugging')

        print(self.value)

        self.emit(Minutes.key_enter(TextLog,self.value))

        # Clear the text input
        self.value = ''

        
    

class MinutesApp(App):
    """Description goes here."""

    CSS_PATH = "minutes.css"

    def compose(self) -> ComposeResult:
        yield InputApp(classes="input_box")
        yield Minutes()


if __name__ == "__main__":
    app = MinutesApp()
    app.run()
