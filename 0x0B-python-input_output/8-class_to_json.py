#!/usr/bin/python3

import json
"""module to return the dictionary description with simple data structure"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    Args:
        obj: class object
    Return: description with simple data structure
    """
    return vars(obj)
