import streamlit as st
import sqlite3 as sql


# Author: Simon Schulze
# Date: Nov 16th 2023
# Description: This is the script that runs the content when logged in.


def display(descr_ph, con: sql.Connection):

    """
    Displays the main content after successful log-in.
    :param descr_ph: An empty Streamlit-container that will get the description.
    :param con: The specific SQLite3-connection.
    :return: None.
    """

    cur = con.cursor()

    with descr_ph.container():
        num_columns = int(cur.execute("SELECT COUNT(date) FROM game").fetchall()[0][0])
        columns = st.columns([2] + [1] * num_columns)

        # print headers
        columns[0].subheader("Spieler")
