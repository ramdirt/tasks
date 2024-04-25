import sqlite3
from settings import Settings

settings = Settings()


def get_db_connection() -> sqlite3.Connection:
    return sqlite3.connect(settings.SQLITE_DB_NAME)