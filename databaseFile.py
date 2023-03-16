import sqlite3


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('PasswordDB.db')
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    website TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL);''')
    conn.commit()


def insert_password(conn, website, username, password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                   (website, username, password))
    conn.commit()


def get_passwords(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords")
    rows = cursor.fetchall()
    return rows
