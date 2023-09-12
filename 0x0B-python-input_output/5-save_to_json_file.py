#!/usr/bin/python3

import json
"""module to define a functio that write object to a text file"""


def save_to_json_file(my_obj, filename):
    """function to write object to text file using JSON representation
    Args:
        my_obj: the object
        filename: name of the file
    """
    x = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(x)
