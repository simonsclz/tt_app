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

        c1.markdown("""- aktueller Punktspielbericht: [Spielbericht
        Rabenstein-Adorf](http://tischtennis-adorf.de/psb_adorf1-rabenstein-hr2023)""")
        c1.markdown("- Plakate wurden in Adorf aufgehangen!")

        c2.markdown("- 14.12.2023: Pokalabend der zweiten Mannschaft")
        c2.markdown("- 15.12.2023: VRL 6")
        c2.markdown("- 21.12.2023: Weihnachtsdoppelturnier")
