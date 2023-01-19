from pathlib import Path
from typing import Union
from timescriber.utilities.get_timestamp import get_timestamp

DEFAULT_OUTPUT_FOLDER_NAME  = "timescriber_output"

def get_base_folder_path(base_folder_location:Union[str,Path] = None):
    
    if base_folder_location is None:
        base_folder_location = Path().home()

    base_folder_path = Path(base_folder_location) / DEFAULT_OUTPUT_FOLDER_NAME
    base_folder_path.mkdir(exist_ok=True, parents=True)

    return str(base_folder_path)

def get_default_file_name():
    file_name = get_timestamp() # I thought about using uuid, but I think that 
                                               # the time stamp down to tenths of a second is fine-grained enough
    return file_name + '.csv'


def get_default_output_file_path():
    base_folder_path = Path(get_base_folder_path())
    return str(base_folder_path / get_default_file_name())
    