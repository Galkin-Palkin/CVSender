from entity.cv_file import CVFile
from entity.letter import Letter
from entity.title import Title
from utils.get_cv_files import get_cv_filenames


titles = [Title(id=str(i), title=f"Title {i}") for i in range(3)]
letters = [Letter(id=str(i), name=f"Letter {i}", text=f"Text of letter {i}") for i in range(3)]
files = [CVFile(id=path, path=path) for path in get_cv_filenames()]