from sqlite3 import Connection

from entity.title import Title


class TitleRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection
        
    def add_title(self, title: Title):
        cursor = self.__connection.cursor()
        cursor.execute("""INSERT INTO Titles(id, title) VALUES (?, ?)""", (title.id, title.title))
        self.__connection.commit()
    
    def update_title(self, title: Title):
        cursor = self.__connection.cursor()
        cursor.execute("""UPDATE Titles SET title = ? WHERE id = ?""", (title.title, title.id))
        self.__connection.commit()
    
    def delete_title(self, title_id: str):
        cursor = self.__connection.cursor()
        cursor.execute("""DELETE FROM Titles WHERE id = ?""", (title_id,))
        self.__connection.commit()
    
    def get_title(self, title_id: str) -> Title:
        cursor = self.__connection.cursor()
        _, title = cursor.execute("""SELECT * FROM Titles WHERE id = ?""", (title_id,)).fetchone()
        return Title(
            id=title_id,
            title=title
        )

