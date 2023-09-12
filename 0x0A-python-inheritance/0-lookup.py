#!/usr/bin/python3

"""module to define a class"""


def lookup(obj):
    """ returns that list of attributes and methods
    Args:
        obj: object to look into
        """
    return dir(obj)
