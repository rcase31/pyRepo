# coding=utf-8
import re

from unidecode import unidecode


def clean_str(my_str):
    """
    Purifies a string of any accents and/or marks.
    :param my_str: string to be purged
    :return: my cleansed string
    """
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
    my_str = my_str.replace('\u0001', 'a')
    my_str = my_str.replace('-', '')
    my_str = re.sub(r'\001', '', my_str)
    my_str = re.sub(r"[^A-Za-z0-9///' ]", '', my_str)
    my_str = my_str.replace("  ", " ").strip()

    return my_str


def del_prepositions(lst) -> list:
    """
    Deletes any preposition in a list of words, returning the cleaned list.
    This is a mutating function, so beware that the input will be corrupted.
    :param lst: a set of .
    :return: a set of words, without any preposition.
        >>> del_prepositions(['a','porque','per','jamais'])
        ['porque', 'jamais']
    """
    prep_list = 'a,ante,após,até,com,contra,de,desde,em,entre,para,perante,' \
                'por,sem,sob,sobre,trás,da,do,o,a,os,as,qual,e'.split(',')
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
    Compares 2 sets of words.
    :param cell_1: first set of words separated by spaces
    :param cell_2: second set of words separated by spaces
    :return: their likelihood
        >>> CELL_1 = 'qual e a condição da caixa de estepe'
        >>> CELL_2 = 'qual e ante condicao da caixa de estepe'
        >>> compare_cells(CELL_1, CELL_2)
        100.0
    """

    cell_1 = cell_1.split(' ')
    cell_1 = del_prepositions(cell_1)

    cell_2 = cell_2.split(' ')
    cell_2 = del_prepositions(cell_2)

    # We consider the maximum length among both cells to use as reference for
    # percentage on likelihood calculation.
    total = max(len(cell_1), len(cell_2))
    match = 0
    for word_1 in cell_1:
        for word_2 in cell_2:
            if clean_str(word_1) == clean_str(word_2):
                match += 1
    return match / total * 100


def compare_lists(lst1, lst2, likelihood_threshold=0) -> (list, list, list):
    """
    Compares 2 same-sized sets of sets of words, returning a match-ordered list
    and an extra list containing the likelihood of each set.
    :param lst1: first list of sets of words.
    :param lst2: second list of sets of words.
    :param likelihood_threshold: lower acceptable limit of likelihood for output.
    :return: a tuple containing the 3 lists mentioned on the description.
        >>> lst1 = ["a vaca do vizinho", "parou de assoviar","e começou a mentir" ]
        >>> lst2 = ["parou de assoviar", "e não fala mais", "a vaca da vizinha", "asasasa sasas asdkjds", "blalsalsa blaslasla"]
        >>> lst1, lst2, lst3 = compare_lists(lst1, lst2, 40)
        >>> print(lst1)
        ['a vaca do vizinho', 'parou de assoviar', 'e começou a mentir']
        >>> print(lst2)
        ['a vaca da vizinha', 'parou de assoviar', None]
        >>> print(lst3)
        [50.0, 100.0, 33.33333333333333]
    """
    out2 = []
    out3 = []
    for set_of_words in lst1:
        most_similar = -1  # sentinela
        likelihood = 0
        for index in range(len(lst2)):
            likelihood_tmp = compare_cells(set_of_words, lst2[index])
            if likelihood_tmp > likelihood:
                likelihood = likelihood_tmp
                most_similar = index
        # we shall remove the most similar item from the compared list, so it
        # doesn't match with any other item in list A.
        if likelihood >= likelihood_threshold:
            out2.append(lst2.pop(most_similar))
            out3.append(likelihood)
        else:
            out2.append(None)
            out3.append(likelihood)
    return lst1, out2, out3
