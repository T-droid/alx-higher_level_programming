#!/usr/bin/python3

""" module to define a rectangle """


class Rectangle:
    """ class to define a square object """
    def __init__(self, width=0, height=0):
        """constructor to initialize instance attributes
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter for the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """method to set width
        Args:
            value(int): value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """method to set height
        Args:
            value(int): value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
