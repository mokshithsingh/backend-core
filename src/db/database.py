import sqlite3 
from src.config import DB_PATH

def get_db_connection():
    con = sqlite3.connect(DB_PATH)
    return con
