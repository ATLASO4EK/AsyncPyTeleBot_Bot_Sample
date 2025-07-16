import sqlite3

def connect():
    conn = sqlite3.connect('BotDB.db')
    cursor = conn.cursor()

    return conn, cursor

def create_user_table(conn, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY NOT NULL,
    tg_id INTEGER NOT NULL, 
    admin INTEGER NOT NULL
    )
    ''')
    conn.commit()