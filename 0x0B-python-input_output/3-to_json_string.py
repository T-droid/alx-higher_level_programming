#!/usr/bin/python3

import json
"""module to define a function that impliments the JSON"""


def to_json_string(my_obj):
    """function that returns the JSON represantaion
    Args:
        my_obj: object to be translated to JSON
    Return: JSON representation of the object
    """
    return json.dumps(my_obj)
