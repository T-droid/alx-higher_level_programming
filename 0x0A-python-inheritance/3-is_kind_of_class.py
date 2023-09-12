#!/usr/bin/python3

"""module to check if instance is of inherited class"""


def is_kind_of_class(obj, a_class):
    """function to check if instance is of inherited class
    Args:
        obj: object to be checked
        a_class: class to be checked
        """
    if isinstance(obj, a_class) and issubclass(type(obj), a_class):
        return True
    return False
