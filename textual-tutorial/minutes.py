from textual.app import App, ComposeResult
from textual.widgets import Input, TextLog, Static
# from textual import events

import time
import pathlib as Path
import csv


file_path_str = '/Users/trent/Documents/GitHub/Usability-Testing-TUI/file_output/test.csv' 

def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def line_writer(line: str, file_path: Path):
    with open(file_path,'a') as file:
        file.write(line)
        file.write('\n')

class FilePathSetter(Input):

    def key_enter(self) -> None:

        print(self.value)

class InputApp(Input):

    def key_enter(self) -> None:

        print(self.value)

        note_string = str(time.time()) + ',' + str(get_timestamp()) + ',' + str(self.value)
        print_string = str(get_timestamp()) + ' :: ' + str(self.value)

        line_writer(note_string, file_path=file_path_str)

        self.screen.query_one(TextLog).write(print_string)

        # Clear the text input
        self.value = ''

class MinutesApp(App):
    """Description goes here."""

    CSS_PATH = "minutes.css"

    def compose(self) -> ComposeResult:
        yield Static(
            "Wecome to TimeScribe\n"
                "- Take notes in the blue box (top right)\n"
                "-- notes are logged in the green box (bottom right)\n"
                "- Set your file path in the red box (bottom left)"
            )
        yield InputApp(placeholder ="Take notes here!", classes="input_box")
        yield FilePathSetter(placeholder="Set your file path here...")
        yield TextLog()

if __name__ == "__main__":
    app = MinutesApp()
    app.run()
