#!/usr/bin/python3

"""module to check if the instance belong to a subclass"""


def inherits_from(obj, a_class):
    """function to check if an object if of a subclass
    Args:
        obj: object
        a_class: class
        """
    if isinstance(obj, a_class) and issubclass(obj.__class__, a_class):
        return True
    return False
