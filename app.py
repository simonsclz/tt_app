import streamlit as st
from PIL import Image
from content.content import display
from login.login import login
import sqlite3 as sql
import utils.state as state


# Author: Simon Schulze
# Date: Nov 16th 2023
# Description: This is the main application with its basic structure.


def app():

    """
    Runs the main app.
    :return: None.
    """

    # Connect to the local database
    con = sql.Connection("login/login_data.sql")

    c1, c2 = st.columns([4, 1])
    c1.header("Tischtennis Adorf 1. Mannschaft")
    c2.image(Image.open("./images/adorf.jpg"), width=125)

    form_ph = st.empty()
    data_ph = st.empty()

    if not state.logged_in:
        login(form_ph, data_ph, con)
    else:
        display(form_ph, con)  # recycling the form placeholder again


if __name__ == "__main__":
    app()
