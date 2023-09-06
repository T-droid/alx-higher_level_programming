#!/usr/bin/python3

"""module to define addition function"""


def add_integer(a, b=98):
    """function to add two integers
    Args:
        a(int): first integer
        b(int): second integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
