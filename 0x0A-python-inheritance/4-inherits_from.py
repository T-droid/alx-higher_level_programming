#!/usr/bin/python3

"""module to check if the instance belong to a subclass"""


def inherits_from(obj, a_class):
    """function to check if an object if of a subclass
    Args:
        obj: object
        a_class: class
    Return: True or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
