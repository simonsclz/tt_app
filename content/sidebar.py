import streamlit as st


# Author: Simon Schulze
# Date: Nov 17th 2023
# Description: The sidebar will be constructed in this script.


def display_sidebar() -> None:

    """
    This function will display the sidebar for the application.
    :return: None.
    """

    with st.sidebar:
        st.markdown("**Hier wird die Sidebar entstehen!**")
