#!/usr/bin/python3
"""
Module used to test the rectangle class
"""
from models.rectangle import Rectangle
import unittest

class TestRectangleClass(unittest.TestCase):
    """Test suite for the Rectangle class"""

    def test_instantiation_with_id(self):
        """Test that the instantiation with id uses the id arg"""
        self.assertEqual(Rectangle(1, 3, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(4, 2, 1, 1, 15).id, 15)

    def test_instantiation_with_none_int_id_raises_exception(self):
        """Never trust anyone"""
        with self.assertRaises(TypeError):
            Rectangle(12, 3, 0, 0, '13')

    def test_instantiation_with_valid_width(self):
        """Test instantiation with width works"""
        rec1 = Rectangle(12, 3, 0, 0, 13)
        rec2 = Rectangle(11, 5)
        self.assertEqual(rec1.width, 12)
        self.assertEqual(rec2.width, 11)

    def test_instantiation_with_valid_height(self):
        """Test instantiation with height works"""
        rec1 = Rectangle(12, 3)
        rec2 = Rectangle(11, 5)
        self.assertEqual(rec1.height, 3)
        self.assertEqual(rec2.height, 5)

    def test_instantiation_with_valid_x(self):
        """Test instantiation with x"""
        rec1 = Rectangle(12, 3)
        rec2 = Rectangle(12, 3, 50, 0, 9)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec2.x, 50)

    def test_instantiation_with_valid_y(self):
        """Test instantiation with y"""
        rec1 = Rectangle(12, 3)
        rec2 = Rectangle(12, 3, 5, 50, 9)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec2.y, 50)
