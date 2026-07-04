from sqlite3 import Cursor
import sqlite3
from types import FunctionType

from constants import DATABASE_PATH
from entity.title import Title

class DatabaseV1:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
    
    def create_database_if_not_exist(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Titles(
                                id INT PRIMARY KEY,
                                title VARCHAR(128)
                            )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Letters(
                                id INT PRIMARY KEY,
                                name VARCHAR(64),
                                text TEXT
                            )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS CV_Files(
                                id INT PRIMARY KEY,
                                name VARCHAR(256),
                                filename VARCHAR(256)
                            )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Settings(
                                property_name VARCHAR(64),
                                property_value VARCHAR(128)
                            )""")
        cursor.execute("""INSERT OR IGNORE INTO Settings (property_name, property_value) VALUES ("database_version", "1")""")
        self.connection.commit()
    
    def close(self):
        self.connection.close()
