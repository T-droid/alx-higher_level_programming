#!/usr/bin/python3

"""module of an empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """area method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """function to validate a value
        Args:
            name(str): string
            value(int): integer
            """
        if not isinstance(value, int):
                raise TypeError("{} must be an ineger".format(name))
        if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
