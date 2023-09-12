#!/usr/bin/python3

import json
"""module to define function that creates an object from json"""


def load_from_json_file(filename):
    """function to create an object from json file
    Args:
        filename: name of the json file
    Return: the created object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
