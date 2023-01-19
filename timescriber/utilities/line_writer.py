from pathlib import Path

def line_writer(line: str, file_path: Path):
    with open(file_path,'a') as file:
        file.write(line)
        file.write('\n')