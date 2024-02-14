#!/usr/bin/python3
"""Module used to test the Square class"""
from models.square import Square
from unittest.mock import patch
from io import StringIO
import unittest


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

    def test_size_of_a_square_with_valid_data(self):
        """Test the size of a Square"""
        s1 = Square(5)
        s2 = Square(2, 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 2)
        s1.size = 8
        self.assertEqual(s1.size, 8)

    def test_size_of_a_square_with_invalid_data(self):
        """Test that invalid Square size raises exception"""
        with self.assertRaises(TypeError):
            Square('5')
        with self.assertRaises(ValueError):
            Square(-10)
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_of_a_square_with_valid_data(self):
        """Test the x arg of a Square"""
        s1 = Square(5, 2)
        s2 = Square(2, 0)
        s3 = Square(2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s3.x, 0)

    def test_x_of_a_square_with_invalid_data(self):
        """Test that invalid Square x raises exception"""
        with self.assertRaises(TypeError):
            Square(1, '5')
        with self.assertRaises(ValueError):
            Square(3, -10)

    def test_y_of_a_square_with_valid_data(self):
        """Test the y arg of a Square"""
        s1 = Square(5, 2)
        s2 = Square(2, 0, 9)
        s3 = Square(2, 10, 19)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.y, 9)
        self.assertEqual(s3.y, 19)

    def test_y_of_a_square_with_invalid_data(self):
        """Test that invalid Square y raises exception"""
        with self.assertRaises(TypeError):
            Square(1, 5, '7')
        with self.assertRaises(ValueError):
            Square(3, 10, -9)

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

    def test_save_to_file_class_method(self):
        """Test that a json file is created"""
        s1 = Square(10)
        s2 = Square(2, 4, 0, 2)
        Square.save_to_file([s1, s2])
        with open('Square.json', 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertIsInstance(data, str)
        self.assertIsNot(data, '')

    def test_save_to_file_without_data(self):
        """Test that a json file is created with empty array"""
        Square.save_to_file([])
        with open('Square.json', 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertIsInstance(data, str)
        self.assertEqual(data, '[]')
        Square.save_to_file(None)
        with open('Square.json', 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertIsInstance(data, str)
        self.assertEqual(data, '[]')

    def test_display_square_according_to_dimension(self):
        """Test that rectangle get displayed according to dimensions"""
        s1 = Square(2)
        s2 = Square(2, 2)
        s3 = Square(2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(),
                             '##\n##\n')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(),
                             '  ##\n  ##\n')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s3.display()
            self.assertEqual(fake_out.getvalue(),
                             '\n  ##\n  ##\n')
