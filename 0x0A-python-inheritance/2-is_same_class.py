#!/usr/bin/python3

"""module to check if objects are of the same class"""


def is_same_class(obj, a_class):
    """check if instance is for a specific class
    Args:
        obj(object): instance to be checked
        a_class(class): class to compare 
        """
    if obj.__class__ is a_class:
        return True
    return False
