#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer() function"""

    def test_should_return_4_or_none(self):
        """Test that given an array returns are:
            [1, 2, 3, 4] => 4
            [1, 3, 4, 2] => 4
            [] => None
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)
        self.assertEqual(max_integer([]), None)

    def test_can_return_max_char_with_str(self):
        """Test that giving a string:
            'Bonjour le monde' => 'u'
            'Salut' => 'u'
        """
        self.assertEqual(max_integer('Bonjour le monde'), 'u')
        self.assertEqual(max_integer('Salut'), 'u')

    def test_can_return_max_str_with_array_of_strs(self):
        """Test that giving an array of strings:
            ['I am', 'a software', 'developer']
            ['u', 'z', 'star'] => 'star'
        """
        self.assertEqual(
            max_integer(['I am', 'a software', 'developer']), 'developer')
        self.assertEqual(max_integer(['u', 'z', 'star']), 'z')
        self.assertEqual(max_integer(['0', '3', '4']), '4')

    def test_should_raise_exception_for_not_supported_types(self):
        """Complex in list or single int numbers not supported"""
        with self.assertRaises(TypeError):
            max_integer([1j, 3, 4, 5])
        with self.assertRaises(TypeError):
            max_integer(6)
        with self.assertRaises(KeyError):
            max_integer({'first_name': 'Djimra',
                         'last_name': 'NGARLEITA',
                         'age': 200})

    def test_can_return_max_list_with_2d_list(self):
        """Test with 2d list"""
        self.assertEqual(max_integer([[1, 18, 2], [3, 4, 12]]), [3, 4, 12])
        self.assertEqual(max_integer([[1, 18, 2, 3, 4, 12]]),
                         [1, 18, 2, 3, 4, 12])
