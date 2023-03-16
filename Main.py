from cryptography.fernet import Fernet
import sqlite3
from databaseFile import create_connection, create_table, insert_password


def main():
    conn = create_connection()
    create_table(conn)

    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(password.encode())

    insert_password(conn, website, username, ciphered_text)

    print("Password saved successfully!")

    conn.close()


if __name__ == '__main__':
    main()
