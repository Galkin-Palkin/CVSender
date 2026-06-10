from sqlite3 import Connection

from entity.letter import Letter


class LetterRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection
        
    def add_letter(self, letter: Letter):
        cursor = self.__connection.cursor()
        cursor.execute("""INSERT INTO Letters(id, name, text) VALUES (?, ?, ?)""", (letter.id, letter.name, letter.text))
        self.__connection.commit()
    
    def update_letter(self, letter: Letter):
        cursor = self.__connection.cursor()
        cursor.execute("""UPDATE Letters SET name = ?, text = ? WHERE id = ?""", (letter.name, letter.text, letter.id))
        self.__connection.commit()
    
    def delete_letter(self, letter_id: str):
        cursor = self.__connection.cursor()
        cursor.execute("""DELETE FROM Letters WHERE id = ?""", (letter_id,))
        self.__connection.commit()
    
    def get_letter(self, letter_id: str) -> Letter:
        cursor = self.__connection.cursor()
        _, name, text = cursor.execute("""SELECT * FROM Letters WHERE id = ?""", (letter_id,)).fetchone()
        return Letter(
            id=letter_id,
            name=name,
            text=text
        )

