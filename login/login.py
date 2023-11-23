import streamlit as st
from hashlib import sha512
import time
import datetime
import extra_streamlit_components as stx
import sqlite3 as sql


# Author: Simon Schulze
# Date: Nov 16th 2023
# Last change: Nov 20th 2023 by Simon Schulze
# Description: This is the script that handles the login process.


def login(form_ph, warning_ph, con: sql.Connection, cm: stx.CookieManager) -> (bool, str):
    """
    Runs the login script for the application.
    :param form_ph: The empty Streamlit-container for the form.
    :param con: The connection to the database.
    :param cm: The cookie manager used to set the log-in-cookie.
    :return: True or false, whether the authentication was successful or not.
    """

    def show_login(form_ph):
        with form_ph.container():
            with st.form(key="login_form"):
                st.text_input("Benutzername:", key="user_name")
                st.text_input("Passwort:", type="password", key="password")
                st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Koulen&family=Lato&family=Nunito&family=Playfair+Display:ital@1&family=Prata&family=Raleway:ital,wght@1,100&family=Roboto&family=Roboto+Condensed&family=Teko&display=swap');
                    div.stButton > button:first-child{
                        font-family: Roboto, sans-serif;
                        font-weight: 0;
                        font-size: 14px;
                        color: #fff;
                        background-color: #d62828;
                        padding: 10px 10px;
                        border: solid #264653 3px;
                        box-shadow: rgb(0, 0, 0) 0px 0px 0px 0px;
                        border-radius: 50px;
                        transition : 1000ms;
                        transform: translateY(0);
                        display: flex;
                        flex-direction: row;
                        align-items: center;
                        cursor: pointer;
                    }
                    div.stButton > button:first-child:hover{
                        transition : 1000ms;
                        padding: 10px 25px;
                        transform : translateY(-0px);
                        background-color: #d6282877;
                        color: #264653;
                        border: solid 3px #264653;
                    }
                    </style>""", unsafe_allow_html=True)
                st.form_submit_button("Anmelden!", on_click=check_password)

    def check_password():
        if not st.session_state.get("password", False) or not st.session_state.get("user_name", False):
            return False

        password = sha512(st.session_state["password"].encode('utf-8'))
        user_name = st.session_state["user_name"]

        # get the password from the specified user
        cur = con.cursor()
        result = cur.execute(f"SELECT password FROM player WHERE first_name = '{user_name}'")
        result = result.fetchall()

        if len(result) == 1:  # check the password hashes
            if result[0][0] == password.hexdigest():

                # set the log-in-cookie to keep users logged in for 10 minutes

                expires_at = datetime.datetime.now() + datetime.timedelta(0, 600)
                cm.set(cookie="logged_in",
                       val=True, expires_at=expires_at, same_site="lax")
                # cm.set(key="usr", cookie=cur.execute(f"""SELECT id FROM player
                # WHERE first_name = '{user_name}'""").fetchall()[0][0],
                # val=user_name, expires_at=expires_at, same_site="lax")
                st.session_state["password_correct"] = True
                st.session_state["user"] = user_name
                del st.session_state["user_name"]
                del st.session_state["password"]
                return True
            else:
                st.session_state["password_correct"] = False
                return False  # hashes do not match
        else:
            st.session_state["password_correct"] = False
            return False  # no such username

    if st.session_state.get("password_correct", False):
        return True

    show_login(form_ph)

    if "password_correct" in st.session_state:
        with warning_ph.container():
            st.error("Diese Anmeldedaten existieren nicht!")

    return False
