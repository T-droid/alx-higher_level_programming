#!/usr/bin/python3

"""module to define a read file function"""
def read_file(filename=""):
    """function to open and read file
    Args:
        filename(str): name of the file too be opened
        """
    with open(filename, encoding="utf-8") as f:
        data_read = f.read()
    print(data_read, end="")
