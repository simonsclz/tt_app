# Author: Simon Schulze
# Date: Nov 17th 2023
# Description: Contains a function that transforms the database date-indices to readable dates.


def transform(date_str: str) -> str:

    """
    Transforms the date string to dd.mm.yyyy.
    :param date_str: The date string from the database.
    :return: Transformed date string as dd.mm.yyyy.
    """

    return date_str[0:2] + "." + date_str[2:4] + "." + date_str[4::]
