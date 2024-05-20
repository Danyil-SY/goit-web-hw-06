import sqlite3
from contextlib import contextmanager
from typing import Generator

database = "./study.db"


@contextmanager
def create_connection(db_file: str) -> Generator[sqlite3.Connection, None, None]:
    """Creates a connection to the SQLite database."""
    conn = sqlite3.connect(db_file)
    try:
        yield conn
    finally:
        conn.rollback()
        conn.close()
