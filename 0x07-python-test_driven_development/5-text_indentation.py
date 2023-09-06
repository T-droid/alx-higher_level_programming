#!/usr/bin/python3

"""module to format text"""


def text_indentation(text):
    """function to print formated text
    Args:
        text(str): text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_list = list(text)

    for idx, i in enumerate(my_list):
        if i == '.' or i == '?' or i == ':':
            my_list.pop(idx + 1)
            my_list.insert(idx + 1, '\n\n')

    print("".join(my_list))
