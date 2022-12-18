from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual.widgets import Input
from textual import events

import time


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class InputApp(Input):
    async def get_text(self) -> str:
        print('Text print test')
        return self.Changed.bubble

    async def key_enter(self, TextLog) -> None:
        print('Printing text for debugging')
        print(self.value)

        self.value = ''

        # Minutes.key_enter(, 'string2')

        # self.query_one(TextLog).write('String2')

class Minutes(TextLog):

    # def on_input_submit(self, event: Input.Submitted) -> None:
    #     self.write(get_timestamp())
    #     self.write(time.time())
    #     self.write(event.__str__)

    # def key_enter(self, s: str) -> None:
    #     self.write(get_timestamp())
    #     self.write(time.time())
    #     self.write(s)

    pass
    

class MinutesApp(App):
    """Description goes here."""

    CSS_PATH = "minutes.css"

    def compose(self) -> ComposeResult:
        yield InputApp(classes="input_box")
        yield TextLog()


if __name__ == "__main__":
    app = MinutesApp()
    app.run()
