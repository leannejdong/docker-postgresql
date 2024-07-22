# db_operations.py

import psycopg2
from config import DATABASE_CONFIG

def create_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

def create_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def drop_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS users')
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name, age):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_user_by_name(name):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE name = %s', (name,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row
