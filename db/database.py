import json
import sqlite3
from datetime import timedelta
from pathlib import Path

DB_FILE = Path(__file__).with_name("human_resource.db")
SCHEMA_FILE = Path(__file__).with_name("hrSystem.sql")

def get_connection():
    connection = sqlite3.connect(DB_FILE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def initialize_db():
    connection = get_connection()
    cursor = connection.cursor()

    with open(SCHEMA_FILE, "r") as file:
        cursor.executescript(file.read())

    connection.commit()
    connection.close()