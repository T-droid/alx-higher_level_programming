#!/usr/bin/python3

import json
"""module to define  a from_json_string"""


def from_json_string(my_str):
    """returns an object represented by a JSON string
    Args:
        my_string: string to be translated
    Return: JSON string
    """
    return json.loads(my_str)
