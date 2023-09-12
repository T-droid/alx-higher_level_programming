#!/usr/bin/python3

"""module to definee a writing function"""


def write_file(filename="", text=""):
    """function to write text into a file
    Args:
        filename(str): name of the file
        text(str): text to input in the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
