import pathlib as Path

def line_writer(line: str, file_path: Path):
    with open('csvfile.csv','wb') as file:
        file.write(line)
        file.write('\n')