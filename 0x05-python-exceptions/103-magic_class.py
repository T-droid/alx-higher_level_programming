#!/usr/bin/python3

""" module reverse engineering"""


class MagicClass:
    """ Class to define a circle"""

    def __init__(self, radius):
        """ initialising instance attributes
        Args:
            radius(int/float): radius of the circles
        """

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """ area calculation method"""

        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """ circumference calculating method"""

        return 2 * math.pi * self._MagicClass__radius
