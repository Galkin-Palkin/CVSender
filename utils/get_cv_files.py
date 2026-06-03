import os
from posixpath import basename
from typing import Sequence
from dotenv import load_dotenv

from constants import ALLOWED_EXTENSIONS, STORAGE_DIR

load_dotenv()

class File:
    filename: str
    basename: str
    bytes: bytes

    def __init__(self, filename: str, basename: str, bytes: bytes):
        self.filename = filename
        self.basename = basename
        self.bytes = bytes
    

def get_cv_filenames() -> Sequence[str]:
    cv_files = []
    for file in os.listdir(path=STORAGE_DIR):
        if file.split('.')[-1] in ALLOWED_EXTENSIONS:
            cv_files.append(file)
    return cv_files

def get_files(filenames: Sequence[str]) -> Sequence[File]:
    files_bytes = []
    for filename in filenames:
        path = os.path.join(STORAGE_DIR, basename(filename))
        print(path)
        with open(path, 'rb') as file:
            bytes = file.read()
            files_bytes.append(
                File(
                    filename=filename,
                    basename=basename(filename),
                    bytes=bytes
                )
            )
    return files_bytes

print(get_cv_filenames())