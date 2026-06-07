from entity.letter import Letter
from entity.title import Title


titles = [Title(id=str(i), title=f"Title {i}") for i in range(3)]
letters = [Letter(id=str(i), name=f"Letter {i}", text=f"Text of letter {i}") for i in range(3)]