import streamlit as st
import time
from content.content import display
from login.login import login
import sqlite3 as sql
import extra_streamlit_components as stx


# Author: Simon Schulze
# Date: Nov 16th 2023
# Last change: Nov 26th 2023 by Simon Schulze
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


def logout():

    """
    Function that handles the logout of a user.
    :return: None
    """

    del st.session_state["password_correct"]


def app() -> None:
    """
    Runs the main app.
    :return: None.
    """

    st.set_page_config(page_title="Tischtennis Adorf", page_icon="🏓", layout="wide")
    st.title("Tischtennis Adorf")

    con = establish_connection()
    cm = get_manager()

    c1, c2 = st.columns([4, 1])
    c1.header("Tischtennis Adorf 1. Mannschaft")
    # c2.image(Image.open("./images/adorf.jpg"), width=125)
    with c2:
        logout_ph = st.empty()
        logout_ph.header("🏓" * 3)

    form_ph = st.empty()
    data_ph = st.empty()
    news_ph = st.empty()

    logged_in = login(form_ph, data_ph, con, cm)

    if not logged_in:  # also test the log-in-cookie
        st.stop()

    logout_ph.empty()
    with logout_ph.container():
        st.markdown(open("/mount/src/tt_app/"
                         "button_styles/logout_button.html").read(), unsafe_allow_html=True)
        st.button("Logout", on_click=logout)

    form_ph.empty()
    data_ph.empty()

    if logged_in:
        display(data_ph, news_ph, con, st.session_state["user"])


if __name__ == "__main__":
    app()
