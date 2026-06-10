from sqlite3 import Connection

from entity.cv_file import CVFile


class CVFileRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection
        
    def add_cvfile(self, cvfile: CVFile):
        cursor = self.__connection.cursor()
        cursor.execute("""INSERT INTO CV_Files(id, name, path) VALUES (?, ?, ?)""", (cvfile.id, cvfile.name, cvfile.path))
        self.__connection.commit()
    
    def update_cvfile(self, cvfile: CVFile):
        cursor = self.__connection.cursor()
        cursor.execute("""UPDATE CV_Files SET name = ?, path = ? WHERE id = ?""", (cvfile.name, cvfile.path, cvfile.id))
        self.__connection.commit()
    
    def delete_cvfile(self, cvfile_id: str):
        cursor = self.__connection.cursor()
        cursor.execute("""DELETE FROM CV_Files WHERE id = ?""", (cvfile_id,))
        self.__connection.commit()
    
    def get_cvfile(self, cvfile_id: str) -> CVFile:
        cursor = self.__connection.cursor()
        _, name, path = cursor.execute("""SELECT * FROM CV_Files WHERE id = ?""", (cvfile_id,)).fetchone()
        return CVFile(
            id=cvfile_id,
            name=name,
            path=path
        )
