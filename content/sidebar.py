import streamlit as st
from PIL import Image


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


def display_sidebar(user_name: str) -> None:

    """
    This function will display the sidebar for the application.
    :param user_name: The name of current user.
    :return: None.
    """

    img = get_image()

    with st.sidebar:
        st.image(img, width=200)
        st.markdown(f"""**Das ist dein Kontrollzentrum, {user_name}.**
                    Wähle unten ein Spiel aus und gib bescheid, ob Du da bist, oder nicht.
                    Du kannst Deine Entscheidung ändern.
                    Wiederhole dazu den Vorgang und wähle die jeweils andere Option aus.\n""")
        st.divider()
