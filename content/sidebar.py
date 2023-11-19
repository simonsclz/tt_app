import streamlit as st
from PIL import Image
import sqlalchemy as sqla
from sqlalchemy.sql import text
from utils.date import transform
from content.game_attendance import display_attendance


# Author: Simon Schulze
# Date: Nov 17th 2023
# Last change: Nov 19th 2023 by Simon Schulze
# Description: The sidebar will be constructed in this script.


@st.cache_resource(experimental_allow_widgets=True)
def get_image() -> Image:

    """
    Opens the image for the sidebar.
    :return: The image returned as a PIL image.
    """

    return Image.open("/Users/simonschulze/tt/tt_app/images/adorf.jpg")


@st.cache_resource
def get_write_connection():

    """
    Since writing in an SQL-database is not possible with SQLite3 when running on
    Streamlit-cloud, we need to create a Streamlit-DB-connection.
    :return:
    """

    return st.experimental_connection("login_data", type="sql")


def display_sidebar(con, user_name: str, att_ph) -> None:

    """
    This function will display the sidebar for the application.
    :param con: Connection to the database.
    :param user_name: The name of current user.
    :param att_ph: The placeholder for the game attendance.
    :return: None.
    """

    cur = get_write_connection().session

    # img = get_image()

    with st.sidebar:
        st.image("http://sv-adorf-erzgebirge-sport.de/wp-content/uploads/2022/03/Logo-1.jpg", width=225)
        st.markdown(f"""**Das ist dein Kontrollzentrum, {user_name}.**
                    Wähle unten ein Spiel aus und gib bescheid, ob Du da bist, oder nicht.
                    Du kannst Deine Entscheidung ändern.
                    Wiederhole dazu den Vorgang und wähle die jeweils andere Option aus.\n""")
        st.divider()

        games = cur.execute(text("SELECT date, opponent FROM game")).all()
        games = [f"{game[1].casefold().capitalize()} ({transform(game[0])})" for game in games]

        selected_game = st.selectbox("Bitte wähle ein Spiel aus:", games)

        # use buttons to update the databases entries
        c1, c2 = st.columns(2)
        attend_clicked = c1.button("Bin da!:white_check_mark:")
        not_attend_clicked = c2.button("Bin nicht da!:x:")

        write_connection = get_write_connection()

        # player is going to attend the selected game
        if attend_clicked:
            with write_connection.session as s:
                player_id = s.execute(text(f"SELECT id FROM player WHERE first_name = '{user_name}'")).all()[0][0]
                game_id = s.execute(text(
                    f"SELECT game_id FROM game WHERE opponent = '{selected_game.split(' ')[0].upper()}'")).all()[0][0]
                s.execute(text(f"UPDATE participation SET attends = 1 WHERE player_id = {player_id} AND game_id = {game_id}"))
                s.commit()
            st.experimental_rerun()

        # player is not going to attend the selected game
        if not_attend_clicked:
            with write_connection.session as s:
                player_id = s.execute(text(f"SELECT id FROM player WHERE first_name = '{user_name}'")).all()[0][0]
                game_id = s.execute(text(
                    f"SELECT game_id FROM game WHERE opponent = '{selected_game.split(' ')[0].upper()}'")).all()[0][0]
                s.execute(text(f"UPDATE participation SET attends = -1 WHERE player_id = {player_id} AND game_id = {game_id}"))
                s.commit()
            st.experimental_rerun()
