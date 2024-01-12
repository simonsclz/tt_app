import streamlit as st


# Author: Simon Schulze
# Date: Nov 26th 2023
# Description: This is a script where the latest news are displayed.


def display_news(news_ph):

    """
    Displays the latest news.
    :param news_ph: An empty Streamlit container to display the news.
    :return: None.
    """

    with news_ph.container():
        c1, c2 = st.columns(2)
        c1.markdown("### Neuigkeiten")
        c2.markdown("### Die nächsten Termine")

        c1.markdown("""- Adorf 1 steht in der Endrunde des Stadtpokals 🤩""")

        c2.markdown("- 15.01.2024: Punktspiel gegen Post SV Chemnitz 2")
        c2.markdown("- 24.01.2024: Punktspiel gegen SV GW Niederwiesa")
        c2.markdown("- 27.01.2024: Vereinsausflug zum HUSS/Schießstand")
