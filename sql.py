import sqlite3

def connect():
    try:
        conn = sqlite3.connect('static/inventory.db')
        return conn
    except Error as e:
        return None