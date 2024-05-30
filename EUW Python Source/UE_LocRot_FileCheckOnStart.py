import os

FILE_NAME = 'LocRotData.txt'
DATA_PATH = data_path

# making script reading local data file
file_path = fr"{DATA_PATH}\{FILE_NAME}"
not_found = f"{FILE_NAME} not found. Setup data file directory."

if os.path.isfile(file_path):
    not_found = f"{FILE_NAME} found."