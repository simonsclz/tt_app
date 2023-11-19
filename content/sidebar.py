import streamlit as st
from PIL import Image
import sqlite3 as sql
from utils.date import transform
from content.game_attendance import display_attendance


# Author: Simon Schulze
# Date: Nov 17th 2023
# Last change: Nov 18th 2023 by Simon Schulze
# Description: The sidebar will be constructed in this script.


@st.cache_resource(experimental_allow_widgets=True)
def get_image() -> Image:

    """
    Opens the image for the sidebar.
    :return: The image returned as a PIL image.
    """

    return Image.open("/Users/simonschulze/tt/tt_app/images/adorf.jpg")


def display_sidebar(con: sql.Connection, user_name: str, att_ph) -> None:

    """
    This function will display the sidebar for the application.
    :param con: Connection to the database.
    :param user_name: The name of current user.
    :param att_ph: The placeholder for the game attendance.
    :return: None.
    """

    cur = con.cursor()

    img = get_image()

    with st.sidebar:
        st.image(img, width=200)
        st.markdown(f"""**Das ist dein Kontrollzentrum, {user_name}.**
                    Wähle unten ein Spiel aus und gib bescheid, ob Du da bist, oder nicht.
                    Du kannst Deine Entscheidung ändern.
                    Wiederhole dazu den Vorgang und wähle die jeweils andere Option aus.\n""")
        st.divider()

        games = cur.execute("SELECT date, opponent FROM game").fetchall()
        games = [f"{game[1].casefold().capitalize()} ({transform(game[0])})" for game in games]

        selected_game = st.selectbox("Bitte wähle ein Spiel aus:", games)

        # use buttons to update the databases entries
        c1, c2 = st.columns(2)
        attend_clicked = c1.button("Bin da!:white_check_mark:")
        not_attend_clicked = c2.button("Bin nicht da!:x:")

        player_id = cur.execute(f"SELECT id FROM player WHERE first_name = '{user_name}'").fetchall()[0][0]

        # player is going to attend the selected game
        if attend_clicked:
            game_id = cur.execute(f"SELECT game_id FROM game WHERE opponent = '{selected_game.split(' ')[0].upper()}'").fetchall()[0][0]
            cur.execute(f"UPDATE participation SET attends = 1 WHERE player_id = {player_id} AND game_id = {game_id}")
            con.commit()
            st.experimental_rerun()

        # player is not going to attend the selected game
        if not_attend_clicked:
            game_id = cur.execute(
                f"SELECT game_id FROM game WHERE opponent = '{selected_game.split(' ')[0].upper()}'").fetchall()[0][0]
            cur.execute(f"UPDATE participation SET attends = -1 WHERE player_id = {player_id} AND game_id = {game_id}")
            con.commit()
            st.experimental_rerun()
