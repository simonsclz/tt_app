import streamlit as st
import sqlite3 as sql
from utils.date import transform
from content.sidebar import display_sidebar


# Author: Simon Schulze
# Date: Nov 16th 2023
# Last change: Nov 17th 2023 by Simon Schulze
# Description: This is the script that runs the content when logged in.


def display(descr_ph, con: sql.Connection):

    """
    Displays the main content after successful log-in.
    :param descr_ph: An empty Streamlit-container that will get the description.
    :param con: The specific SQLite3-connection.
    :return: None.
    """

    cur = con.cursor()

    display_sidebar()

    with descr_ph.container():
        num_columns = int(cur.execute("SELECT COUNT(date) FROM game").fetchall()[0][0])
        columns = st.columns([2] + [3] * num_columns)

        # print headers
        columns[0].markdown("**Spieler**")

        games = cur.execute("SELECT * FROM game").fetchall()

        # print games
        for column_index in range(1, len(columns)):
            columns[column_index].write(games[column_index - 1][1].casefold().capitalize() +
                                        " " + f"({transform(games[column_index - 1][0])})")
