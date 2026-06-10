from sqlite3 import Connection


def apply_migrations(connection: Connection):
    cursor = connection.cursor()
    database_version = cursor.execute("""SELECT property_value FROM Settings WHERE property_name = 'database_version'""").fetchone()
    database_version = int(database_version)
