"""
Class created to stringfy inputs, lower-case strings, switch special characters
and question marks.

"""
import re

from unidecode import unidecode


def clean_str(my_str):
    if isinstance(my_str, bool):
        if my_str:
            my_str = 'TRUE'
        else:
            my_str = 'FALSE'

    if isinstance(my_str, int) or isinstance(my_str, float):
        my_str = str(my_str)

    my_str = my_str.lower()
    my_str = my_str.replace("  ", " ").strip()
    my_str = unidecode(my_str)

    my_str = re.sub(r'\001', '', my_str)
    my_str = re.sub(r"[^A-Za-z0-9///' ]", '', my_str)
    my_str = my_str.replace("  ", " ").strip()

    return my_str
