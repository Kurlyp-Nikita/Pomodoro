import sqlite3
from setings import Settings


setings = Settings()


def get_db_connection() -> sqlite3.Connection:
    return sqlite3.connect(setings.sqlite_db_name)
