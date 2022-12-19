from textual.app import App, ComposeResult
from textual.widgets import Input, TextLog, Static, Header, Footer

import time
import os
import pathlib as Path
import uuid


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def line_writer(line: str, file_path: Path):
    with open(file_path,'a') as file:
        file.write(line)
        file.write('\n')

### CREATE OUTPUT FILE ON START ###
this_file_path = os.getcwd()

session_id = str(uuid.uuid4())

output_file_path = this_file_path + '/output/' + get_timestamp() + '_' + session_id + '.csv'

print(output_file_path)

f = open(output_file_path, "x")
###################################

class InputApp(Input):

    def key_enter(self) -> None:

        note_string = str(time.time()) + ',' + str(get_timestamp()) + ',' + str(self.value)
        print_string = str(get_timestamp()) + ' :: ' + str(self.value)

        line_writer(note_string, file_path=output_file_path)

        self.screen.query_one(TextLog).write(print_string)

        # Clear the text input
        self.value = ''

class TimeScriberApp(App):
    """Description goes here."""

    CSS_PATH = "timescriber.css"

    def compose(self) -> ComposeResult:
        yield Header("TimeScriber")
        yield Static(
            "Wecome to TimeScriber\n"
                "- Take notes in the blue box (bottom left)\n"
                "- Notes are logged in the green box (bottom right)"            )
        yield Static(
        "Below is the path for the file you are writing to:\n"
        "\n"
        + str(output_file_path), classes="file_path_box"
        )
        yield InputApp(placeholder ="Take notes here!", classes="input_box")
        yield TextLog()
        yield Footer()

if __name__ == "__main__":
    app = TimeScriberApp()
    app.run()
