#!/usr/bin/python3

"""module to define a square"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """class to define a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """method to initialise square attributes
        Args:
            size: size of the square
            x: x plane coordinate
            y: y plane cordinate
            id: class id
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.__size = value

    def __str__(self):
        """returns an informal string represntion of a square"""
        return f"[square] ({self.id}) {self._Rectangle__x}/{self._Rectangle__y} - {self.__size}"

    def update(self, *args, **kwargs):
        """method to update attributes
        Args:
            args: non keyworded arguments
            kwargs: key word arguments
        """
        flag = 0
        count = 1
        for arg in args:
            flag = 1
            if count == 1:
                self.id = arg
            elif count == 2:
                self.__size = arg
            elif count == 3:
                self.x = arg
            elif count == 4:
                self.y = arg
            else:
                pass
            count += 1

        if flag == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.__size = value
                elif key  == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    pass

    def to_dictionary(self):
        """returns a dictionary representation of the square"""
        return {
                'id': self.id, 'size': self.__size, 'x': self.x, 'y': self.y
                }
