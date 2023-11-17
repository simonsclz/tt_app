import streamlit as st
import sqlite3 as sql
from hashlib import sha512
import datetime
import extra_streamlit_components as stx


# Author: Simon Schulze
# Date: Nov 16th 2023
# Last change: Nov 17th 2023 by Simon Schulze
# Description: This is the script that handles the login process.


def login(form_ph, warning_ph, con: sql.Connection, cm: stx.CookieManager) -> bool:

    """
    Runs the login script for the application.
    :param form_ph: The empty Streamlit-container for the form.
    :param con: The connection to the database.
    :param cm: The cookie manager used to set the log-in-cookie.
    :return: True or false, whether the authentication was successful or not.
    """

    with form_ph.container():
        with st.form(key="login_form"):
            user_name = st.text_input("Benutzername:")
            password = st.text_input("Passwort:", type="password")
            clicked = st.form_submit_button("Anmelden!")

    if clicked:
        password = sha512(password.encode('utf-8'))

        # get the password from the specified user
        cur = con.cursor()
        result = cur.execute(f"SELECT password FROM player WHERE first_name = '{user_name}'")
        result = result.fetchall()

        if len(result) == 1:  # check the password hashes
            if result[0][0] == password.hexdigest():

                # set the log-in-cookie to keep users logged in

                expires_at = datetime.datetime.now() + datetime.timedelta(0, 600)
                cm.set("logged_in", True, expires_at=expires_at)
                return True
            else:
                with warning_ph.container():
                    st.warning("Diese Anmeldedaten existieren nicht!")
                return False  # hashes do not match
        else:
            with warning_ph.container():
                st.warning("Diese Anmeldedaten existieren nicht!")
                return False  # no such username

    return False
