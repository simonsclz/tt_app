import streamlit as st
from PIL import Image
from content.content import display
from login.login import login
import sqlite3 as sql
import extra_streamlit_components as stx


# Author: Simon Schulze
# Date: Nov 16th 2023
# Last change: Nov 19th 2023 by Simon Schulze
# Description: This is the main application with its basic structure.


@st.cache_resource(experimental_allow_widgets=True)
def establish_connection() -> sql.Connection:

    """
    Establishes the connection to the database. Uses Streamlit caching to speed up.
    :return: None.
    """

    # Connect to the local database
    con = sql.connect("login/login_data.sql", check_same_thread=False)
    return con


@st.cache_resource(experimental_allow_widgets=True)
def get_manager() -> stx.CookieManager:

    """
    Creates a cookie manager from extra_streamlit_components package.
    :return: The cookie manager.
    """

    return stx.CookieManager()


def app() -> None:

    """
    Runs the main app.
    :return: None.
    """

    con = establish_connection()
    cm = get_manager()

    c1, c2 = st.columns([4, 1])
    c1.header("Tischtennis Adorf 1. Mannschaft")
    # c2.image(Image.open("./images/adorf.jpg"), width=125)
    c2.header(":table_tennis_paddle_and_ball:" * 3)

    form_ph = st.empty()
    data_ph = st.empty()

    st.session_state['logged_in'] = False
    logged_in, user_name = login(form_ph, data_ph, con, cm)

    if not st.session_state['logged_in'] and cm.get("logged_in") is None:  # also test the log-in-cookie
        st.stop()

    form_ph.empty()
    display(data_ph, con, cm.get("user_name"))  # gets executed only if logged in


if __name__ == "__main__":
    app()
