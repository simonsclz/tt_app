import streamlit as st
import sqlite3 as sql
from utils.date import transform
from content.sidebar import display_sidebar
from content.description import display_description
from content.game_attendance import display_attendance
from content.news import display_news


# Author: Simon Schulze
# Date: Nov 16th 2023
# Last change: Nov 26th 2023 by Simon Schulze
# Description: This is the script that runs the content when logged in.


def display(descr_ph, news_ph, con: sql.Connection, user_name: str):

    """
    Displays the main content after successful log-in.
    :param descr_ph: An empty Streamlit-container that will get the description.
    :param news_ph: An empty Streamlit-container that will display the latest news.
    :param con: The specific SQLite3-connection.
    :param user_name: The user that is logged in.
    :return: None.
    """

    with descr_ph.container():
        display_description(user_name)
        st.divider()

    # display the latest news
    display_news(news_ph)

    st.divider()

    # use an empty container and our display_attendance()-function
    st.subheader("Anwesenheiten")
    game_attendance_ph = st.empty()
    display_attendance(game_attendance_ph, con)

    # sidebar needs the attendance placeholder
    display_sidebar(con, user_name, game_attendance_ph)
