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

    def area(self):
        """method to calculate the area"""
        return self.__width * self.__height

    def __str__(self):
        """return readable representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """class square from rectangle"""
    def __init__(self, size):
        """initialisation method
        Args:
            size(int): size of the square
            """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """method to calculate the area"""
        return self.__size ** 2
    
    def __str__(self):
        """return a readable represantation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
