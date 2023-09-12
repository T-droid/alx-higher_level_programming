#!/usr/bin/python3

"""module to define a function that adds an attribute ti a class"""


def add_attribute(obj, attr_name, attr_value):
    """adds an attribute if possible
    Args:
        obj: object
        attr_name: attribute to be added
        attr_value: attribute value
        """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("Can't add new attribute")
