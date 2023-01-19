from textual.app import App, ComposeResult
from textual.widgets import Input, TextLog, Static, Header, Footer
from pathlib import Path

import os
import sys
import time

base_package_path = Path(__file__).parent.parent
print(f"adding base_package_path: {base_package_path} : to sys.path")
sys.path.insert(0, str(base_package_path)) # add parent directory to sys.path

from timescriber.utilities.get_timestamp import get_timestamp
from timescriber.utilities.system_configuration import get_default_output_file_path
from timescriber.utilities.line_writer import line_writer

OUTPUT_FILE_PATH = get_default_output_file_path() # global variable so that it's accessible in InputApp

class InputApp(Input):

    def key_enter(self) -> None:

        note_string = str(time.time()) + ',' + str(get_timestamp()) + ',' + str(self.value)
        print_string = str(get_timestamp()) + ' :: ' + str(self.value)

        line_writer(note_string, file_path=OUTPUT_FILE_PATH)

        self.screen.query_one(TextLog).write(print_string)

        # Clear the text input
        self.value = ''

class TimeScriberApp(App):
    """An app for taking timestamped notes. Saves notes to a `csv` file."""

    CSS_PATH = "timescriber.css"

    BINDINGS = [
        ("ctrl+C", "quit", "Quit")
    ]

    def compose(self) -> ComposeResult:
        # self._output_file_path = get_default_output_file_path()
        # self._file = open(self._output_file_path, "x")
        self._file = open(OUTPUT_FILE_PATH, "x")

        yield Header("TimeScriber")
        yield Static(
            "Wecome to TimeScriber\n"
                "- Take notes in the blue box (bottom left)\n"
                "- Notes are logged in the green box (bottom right)"            )
        yield Static(
        "Below is the path for the file you are writing to:\n"
        "\n"
        # + str(self._output_file_path), classes="file_path_box"
        + str(OUTPUT_FILE_PATH), classes="file_path_box"
        )
        yield InputApp(placeholder ="Take notes here!")
        yield TextLog()
        yield Footer()

if __name__ == "__main__":
    app = TimeScriberApp()
    app.run()
