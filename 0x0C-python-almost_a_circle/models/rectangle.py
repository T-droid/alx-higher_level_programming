#!/usr/bin/python3

"""model to define a rectangle"""

from models.base import Base


class Rectangle(Base):
    """class to define a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialisation method
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
            x, y: values
        """
        if not isinstance(width, int):
            raise TypeError("width must be an interger")

        if not isinstance(height, int):
            raise TypeError("height must be an interger")

        if not isinstance(x, int):
            raise TypeError("x must be an interger")

        if not isinstance(y, int):
            raise TypeError("y must be an interger")
        
        if width <= 0:
            raise ValueError("width must be > 0")

        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width
        Args:
            value: value to set"""
        if not isinstance(value, int):
            raise TypeError("value must be an interger")

        if value <= 0:
            raise ValueError("value must be > 0")

        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height
        Args:
            value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("value must be an interger")

        if value <= 0:
            raise ValueError("value must be > 0")

        self.__height = value

    @property
    def x(self):
        """gets the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value
        Args:
            value: value to set"""
        if not isinstance(value, int):
            raise TypeError("value must be an interger")

        if value < 0:
            raise ValueError("value must be >= 0")

        self.__x = value

    @property
    def y(self):
        """gets the value y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y
        Args:
            value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("value must be an interger")

        if value < 0:
            raise ValueError("value must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the rectangle"""
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """returns an informal representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """method to update all attributes
        Args:
            args: tuple
        """
        flag = 0
        arg_count = 1
        for arg in args:
            flag = 1
            if arg_count == 1:
                self.id = arg

            elif arg_count == 2:
                self.width = arg

            elif arg_count == 3:
                self.height = arg

            elif arg_count == 4:
                self.x = arg

            elif arg_count == 5:
                self.y = arg

            else:
                break

            arg_count += 1

        if flag == 0:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value

                elif key == "id":
                    self.id = value

                elif key == "height":
                    self.height = value

                elif key == "x":
                    self.x = value

                elif key == "y":
                    self.y = value

                else:
                    pass

    def to_dictionary(self):
        """return a dictionary representaion of a rectangle"""
        return {
                'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y
                }
