from textual.app import App, ComposeResult
from textual.containers import Content
from textual.widgets import Input, Static
# from textual import events

import time
import pathlib as Path
import csv


file_path_str = '/Users/trent/Documents/GitHub/Usability-Testing-TUI/file_output/test.csv' 
results = str(["starter", "list", "yay"])

def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def line_writer(line: str, file_path: Path):
    with open(file_path,'a') as file:
        file.write(line)
        file.write('\n')

class InputApp(Input):

    def key_enter(self) -> None:

        print(self.value)

        note_string = str(time.time()) + ',' + str(get_timestamp()) + ',' + str(self.value)

        line_writer(note_string, file_path=file_path_str)

        # Clear the text input
        self.value = ''

        with open(file_path_str, newline='') as csvfile:

            file_read = csv.reader(csvfile, delimiter=',')

            print('reading csv')  

            file_read = list(file_read)    

            print(file_read)

class MinutesApp(App):
    """Description goes here."""

    CSS_PATH = "minutes.css"

    def compose(self) -> ComposeResult:
        yield InputApp(classes="input_box")
        yield Static(results)

if __name__ == "__main__":
    app = MinutesApp()
    app.run()
