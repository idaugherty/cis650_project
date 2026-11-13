import json
import sqlite3
from datetime import timedelta
from pathlib import Path
import pandas as pd

DB_FILE = Path(__file__).with_name("human_resource.db")
SCHEMA_FILE = Path(__file__).with_name("hrSystem.sql")

def get_connection():
    connection = sqlite3.connect(DB_FILE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def initialize_db():
    connection = get_connection()
    try:
        schema_script = SCHEMA_FILE.read(encoding="utf-8")
        connection.executescript(schema_script)
        connection.commit()
    finally:
        connection.close()
    print ("Database successfully initialized")