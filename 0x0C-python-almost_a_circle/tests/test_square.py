#!/usr/bin/python3
"""Module used to test the Square class"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test Square class"""
    def test_str_function_for_square(self):
        """Test the return of str function for a Square"""
        s1 = Square(5, 0, 0, 20)
        s2 = Square(2, 2, 0, 19)
        self.assertEqual(str(s1), '[Square] (20) 0/0 - 5')
        self.assertEqual(str(s2), '[Square] (19) 2/0 - 2')

    def test_area_function_for_square(self):
        """Test the area of a Square"""
        s1 = Square(5)
        s2 = Square(2, 2)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
