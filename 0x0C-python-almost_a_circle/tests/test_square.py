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

    def test_size_of_a_square(self):
        """Test the size of a Square"""
        s1 = Square(5)
        s2 = Square(2, 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 2)
        s1.size = 8
        self.assertEqual(s1.size, 8)

    def test_update_square_attrs_with_args(self):
        """Test that update function work propertly for square"""
        s = Square(50)
        self.assertEqual(s.size, 50)
        s.update(50, 20)
        self.assertEqual(s.id, 50)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 0)
        s.update(50, 20, 12, 1)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 1)

    def test_update_square_attrs_with_kwargs(self):
        """Test that update with kwargs works and kwargs is ignored if args
        exist"""
        s = Square(50)
        self.assertEqual(s.size, 50)
        self.assertEqual(s.x, 0)
        s.update(id=90, x=12)
        self.assertEqual(s.id, 90)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 0)
        s.update(21, id=89, size=18)
        self.assertEqual(s.id, 21)
        self.assertEqual(s.size, 50)

    def test_to_dictionary_method(self):
        """Test the dictionary representation of a square"""
        s = Square(50)
        sdict = s.to_dictionary()
        self.assertEqual(sdict.get('size'), 50)
        self.assertEqual(sdict.get('x'), 0)
        sdict = Square(30, 20, 10, 29).to_dictionary()
        self.assertEqual(sdict.get('size'), 30)
        self.assertEqual(sdict.get('x'), 20)
        self.assertEqual(sdict.get('y'), 10)
        self.assertEqual(sdict.get('id'), 29)
