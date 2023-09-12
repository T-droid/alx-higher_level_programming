#!/usr/bin/python3

"""module to define myInt"""


class MyInt(int):
    """class inheriting from int"""
    def __init__(self, value):
        """initialisation
        Args:
            value(int): value
            """
        self.value = value

    def __eq__(self, other):
        """checks for equality"""
        if self.value == other:
            return False
        return True

    def __ne__(self, other):
        """checks for inequality"""
        if self.value != other:
            return False
        return True
