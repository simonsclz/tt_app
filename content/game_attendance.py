import streamlit as st
import sqlite3 as sql
from utils.date import transform


# Author: Simon Schulze
# Date: Nov 18th 2023
# Last change: Nov 26th 2023 by Simon Schulze
# Description: The game attendance overview will be managed here.


def display_attendance(content_ph, con: sql.Connection):
    """
    This function displays the content of the database (attendances of players).
    :param content_ph: The placeholder (Streamlit-container) for the content.
    :param con: The SQL-database-connection.
    :return: None.
    """

    cur = con.cursor()

    num_columns = int(cur.execute("SELECT COUNT(date) FROM game").fetchall()[0][0])
    columns = st.columns([2] + [3] * num_columns)

    games = cur.execute("SELECT date, opponent FROM game").fetchall()
    column_indices = dict()

    columns[0].markdown("**Spieler** :arrow_down_small:")

    # order by player_id to ensure the correct plotting of the table
    attendances = cur.execute("""SELECT first_name, opponent, attends
                                FROM (player INNER JOIN participation ON player.id = participation.player_id) T
                                INNER JOIN game on T.game_id = game.game_id
                                ORDER BY player_id""").fetchall()

    with content_ph.container():

        # print games
        for column_index in range(1, len(columns)):
            columns[column_index].markdown(f"**{games[column_index - 1][1].casefold().capitalize()}**")

            column_indices[games[column_index - 1][1]] = column_index

        last_name = ""
        for player_name, opponent, attends in attendances:

            # print new line when new names comes
            if player_name != last_name:
                columns[0].markdown(f"*{player_name}*")
                last_name = player_name
            emoji = "✅" if attends == 1 else ("❌" if attends == 0 else "❔")
            columns[column_indices[opponent]].write(emoji)
