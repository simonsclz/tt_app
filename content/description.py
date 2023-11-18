import streamlit as st


# Author: Simon Schulze
# Date: Nov 18th 2023
# Description: Here will the description of the page be written.


def display_description(user_name: str) -> None:

    """
    The function that should plot the description.
    :return: None.
    """

    st.markdown(f"""**Herzlich Willkommen, {user_name}!**
                Nachfolgend findest Du eine Übersicht, über die anstehenden Spiele.
                Zudem siehst Du, wer zu den Spielen alles da ist.\n""")
