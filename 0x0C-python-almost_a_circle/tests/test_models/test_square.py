#!/usr/bin/python3

"""module to test case square"""

import unittest
from models.square import Square

class SquareTest(unittest.TestCase):
    """class to test the square class"""
    def test_square_valid_inputs(self):
        """tests if the class recieves correct inputs"""
        r = Square(4, 5, 2, 42)
        self.assertEqual(r.size, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 42)

    def test_constructor_invalid_x(self):
        """check for invalid x-coodinate"""
        with self.assertRaises(ValueError):
            r = Square(4, -1)

    def test_constructor_invalid_width(self):
        """tests for invalid width"""
        with self.assertRaises(ValueError):
            r = Square(-4)

    def test_area_calculation(self):
        """test the calculation of the area"""
        r = Square(4)
        self.assertEqual(r.area(), 16)

if __name__ == "__main__":
    unittest.main()
