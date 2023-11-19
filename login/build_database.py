import sqlite3 as sql
from hashlib import sha512


# Author: Simon Schulze
# Date: Nov 16th 2023
# Last change: Nov 19th 2023 by Simon Schulze
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


def build_participation():
    con = sql.Connection("login_data.sql")
    cur = con.cursor()
    users = cur.execute("SELECT id FROM player").fetchall()
    games = cur.execute("SELECT game_id FROM game").fetchall()
    for user in users:
        user = user[0]
        for game in games:
            game = game[0]
            cur.execute(f"INSERT INTO participation VALUES ({user}, {game}, 0)")
    con.commit()


def change_password():
    con = sql.Connection("login_data.sql")
    cur = con.cursor()
    pw = sha512(''.encode('utf-8'))
    cur.execute(f"UPDATE player SET password = '{pw.hexdigest()}' WHERE id BETWEEN 1 AND 6")
    con.commit()


if __name__ == "__main__":
    change_password()
