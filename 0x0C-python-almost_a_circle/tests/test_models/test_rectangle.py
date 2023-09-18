#!/usr/bin/python3

"""test driven development"""


import unittest
from models.rectangle import Rectangle

class MyTestCase(unittest.TestCase):
    """class to test the Rectangle class"""
    def test_rectangle_valid_inputs(self):
        """tests if the class recieves correct inputs"""
        r = Rectangle(4, 5, 1, 2, 42)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 42)

    def test_constructor_invalid_x(self):
        """check for invalid x-coodinate"""
        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, -1)

    def test_constructor_invalid_width(self):
        """tests for invalid width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-4, 5)

    def test_area_calculation(self):
        """test the calculation of the area"""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

if __name__ == "__main__":
    unittest.main()
