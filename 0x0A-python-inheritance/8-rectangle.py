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
                raise TypeError("{} must be an integer".format(name))
        if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """rectangle class to inherit from basegeometry"""
    def __init__(self, width, height):
        """method to initialise atributes
        Args:
            width(int): width
            height(int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
