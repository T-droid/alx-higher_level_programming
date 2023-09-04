#!/usr/bin/python3

""" module to define a rectangle """


class Rectangle:
    """ class to define a square object """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor to initialize instance attributes
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        Rectangle.number_of_instances += 1

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

    def area(self):
        """method to calculate area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method to calculate the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ method to draw the rectangle """
        rows = self.__height
        cols = self.__width
        myList = []

        for i in range(rows):
            for j in range(cols):
                myList.append(str(self.print_symbol))
            myList.append('\n')
        myList.pop()
        return "".join(myList)

    def __repr__(self):
        """method to return a formal represntaion of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """method just before deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to compute the largest rectangle
        Args:
            rect_1(object): first object
            rect_2(object): second object
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to create a new instance"""
        return cls(size, size)
