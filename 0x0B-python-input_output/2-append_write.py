#!/usr/bin/python3

"""module to define a function that appends a string"""


def append_write(filename="", text=""):
    """function to append a string
    Args:
        filename(str): name of the file
        text(str): text to append to the file
    Return: number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
