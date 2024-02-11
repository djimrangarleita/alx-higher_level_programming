#!/usr/bin/python3
"""
Module used to test the rectangle class
"""
from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
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

    def test_instantiation_with_invalid_width(self):
        """Test instantiation with invalid width should raise exception"""
        with self.assertRaises(TypeError):
            Rectangle('10', 3)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)

    def test_instantiation_with_valid_height(self):
        """Test instantiation with height works"""
        rec1 = Rectangle(12, 3)
        rec2 = Rectangle(11, 5)
        self.assertEqual(rec1.height, 3)
        self.assertEqual(rec2.height, 5)

    def test_instantiation_with_invalid_height(self):
        """Test instantiation with invalid height should raise exception"""
        with self.assertRaises(TypeError):
            Rectangle(10, '3')
        with self.assertRaises(ValueError):
            Rectangle(2, -1)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_instantiation_with_valid_x(self):
        """Test instantiation with x"""
        rec1 = Rectangle(12, 3)
        rec2 = Rectangle(12, 3, 50, 0, 9)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec2.x, 50)

    def test_instantiation_with_invalid_x(self):
        """Test instantiation with invalid width should raise exception"""
        with self.assertRaises(TypeError):
            Rectangle(10, 3, '12')
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -1)
        self.assertEqual(Rectangle(10, 4, 0).x, 0)

    def test_instantiation_with_valid_y(self):
        """Test instantiation with y"""
        rec1 = Rectangle(12, 3)
        rec2 = Rectangle(12, 3, 5, 50, 9)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec2.y, 50)

    def test_instantiation_with_invalid_y(self):
        """Test instantiation with invalid y should raise exception"""
        with self.assertRaises(TypeError):
            Rectangle(10, 3, 12, '10')
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 1, -1)
        self.assertEqual(Rectangle(10, 4, 2, 0).y, 0)

    def test_area_of_rectangle(self):
        """Test that area function works properly"""
        rec1 = Rectangle(10, 3)
        rec2 = Rectangle(5, 2)
        self.assertEqual(rec1.area(), 30)
        self.assertEqual(rec2.area(), 10)

    def test_rec_is_displayed_according_to_dimension(self):
        # please implement me
        pass

    def test_str_function_for_rectangle(self):
        """Test the string representation of a rectangle"""
        rec1 = Rectangle(4, 6, 2, 1, 12)
        rec2 = Rectangle(5, 5, 1, 0, 17)
        self.assertEqual(str(rec1), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(rec2), '[Rectangle] (17) 1/0 - 5/5')

    def test_update_function_changes_the_attrs(self):
        """Test random property updates"""
        rec1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rec1.id, 12)
        rec1.update(89)
        self.assertEqual(rec1.width, 4)
        self.assertEqual(rec1.height, 6)
        rec1.update(89, 2, 3, 4, 5)
        self.assertEqual(rec1.id, 89)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 3)
        self.assertEqual(rec1.x, 4)
        self.assertEqual(rec1.y, 5)

    def test_update_with_more_than_5_args_fail(self):
        """If we call update with more than 5 args it will raise an exception"""
        rec = Rectangle(12, 5)
        with self.assertRaises(ValueError):
            rec.update(89, 15, 7, 0, 0, 8)

    def test_update_args_with_wrong_type_or_val_fail(self):
        """If we call update with more than 5 args it will raise an exception"""
        rec = Rectangle(12, 5)
        with self.assertRaises(TypeError):
            rec.update(89, '15', 7, 0, 0)
        with self.assertRaises(ValueError):
            rec.update(89, 15, 0, 0, 0)

    def test_update_with_kwargs(self):
        """Test update with kwargs works as expected"""
        rec = Rectangle(12, 5)
        self.assertEqual(rec.width, 12)
        rec.update(x=1, height=2, y=3, id=49, width=4)
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.id, 49)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 3)

    def test_update_with_args_and_kwargs(self):
        rec = Rectangle(12, 5)
        rec.update(91, id=71, width=23)
        self.assertEqual(rec.id, 91)
        self.assertEqual(rec.width, 12)
        self.assertEqual(rec.height, 5)

    def test_to_dictionary_method(self):
        """Test the dictionary representation of a rectangle"""
        rec = Rectangle(12, 5)
        recdict = rec.to_dictionary()
        self.assertEqual(recdict.get('width'), 12)
        self.assertEqual(recdict.get('height'), 5)
        rec = Rectangle(21, 8, 3, 4, 89)
        recdict = rec.to_dictionary()
        self.assertEqual(recdict.get('id'), 89)
        self.assertEqual(recdict.get('x'), 3)
        self.assertEqual(recdict.get('y'), 4)
        self.assertEqual(recdict.get('width'), 21)
        self.assertEqual(recdict.get('height'), 8)
