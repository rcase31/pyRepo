# coding=utf-8
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


def del_prepositions(lst) -> list:
    """
        >>> del_prepositions(['a','porque','per','jamais'])
        ['porque', 'jamais']
    """
    prep_list = 'a,ante,após,até,com,contra,de,desde,em,entre,para,perante,' \
                'por,sem,sob,sobre,trás'.split(',')
    tmp = []
    while len(lst) != 0:
        word = lst.pop()
        flg = True
        for prep in prep_list:
            if prep == word:
                flg = False
        if flg:
            tmp.append(word)
    return tmp


def compare_cells(cell_1, cell_2) -> int:
    """
        >>> CELL_1 = 'qual e a condição da caixa de estepe'
        >>> CELL_2 = 'qual e ante condicao da caixa de estepe'
        >>> compare_cells(CELL_1, CELL_2)
        100.0
    """

    cell_1 = cell_1.split(' ')
    cell_1 = del_prepositions(cell_1)

    cell_2 = cell_2.split(' ')
    cell_2 = del_prepositions(cell_2)

    total = len(cell_1)
    match = 0
    for word_1 in cell_1:
        for word_2 in cell_2:
            if clean_str(word_1) == clean_str(word_2):
                match += 1
    return match / total * 100
