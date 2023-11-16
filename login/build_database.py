import sqlite3 as sql
from hashlib import sha512


# Author: Simon Schulze
# Date: Nov 16th 2023
# Description: This is the script which was used to build the database.


def build():
    con = sql.Connection("login_data.sql")
    cur = con.cursor()
    cur.execute("CREATE TABLE player(id, last_name, first_name, password, PRIMARY KEY (id))")
    con.commit()


def insert_content():
    con = sql.Connection("login_data.sql")
    cur = con.cursor()
    pw = sha512(''.encode('utf-8'))
    cur.execute(f"INSERT INTO player VALUES (6, 'Sieber', 'Maximilian', '{pw.hexdigest()}')")
    con.commit()


if __name__ == "__main__":
    insert_content()
