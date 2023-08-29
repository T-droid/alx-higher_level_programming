#!/usr/bin/python3

"""
module of a class that defines a square
"""


class Square:
    """
    class to define a square
    """
    def __init__(self, size=0):
        """
        constructor for my class
        :param size: size of the square
        :type size: int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        method to calculate the area of the object square
        """
        return self.__size ** 2
