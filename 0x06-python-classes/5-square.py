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

    @property
    def size(self):
        """
        getter for the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the value of size
        :param value: new value of size
        :type value: int
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        method to calculate the area of the object square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the object square
        """
        for _ in range(self.__size):
            print("#" * self.__size)
