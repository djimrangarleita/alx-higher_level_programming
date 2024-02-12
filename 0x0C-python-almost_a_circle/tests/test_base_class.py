#!/usr/bin/python3
"""
Module used to test the base class
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBase(unittest.TestCase):
    """Test suite for base class"""

    def test_instantiation_with_id(self):
        """Test that class initialization with id return the same id"""
        self.assertEqual(Base(12).id, 12)

    def test_instantiation_with_none_int_id_will_raise_exception(self):
        """Never trust anyone, check that id passed by user has the correct
        type (int), otherwise raise exception TypeError"""
        with self.assertRaises(TypeError):
            Base('13')

    @unittest.skip('always skip this test, id is randomly generated')
    def test_instances_without_id(self):
        """Test that instanciation without id arg works and the private
        class attr __nb_objects is incremented correctly
        """
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_return_type_of_to_json_string_method(self):
        """Test that the static method to_json_string works properly"""
        json_str = Base.to_json_string([])
        self.assertIsInstance(json_str, str)
        json_str = Base.to_json_string(None)
        self.assertIsInstance(json_str, str)
        json_str = Base.to_json_string([{'id': 89, 'width': 25}])
        self.assertIsInstance(json_str, str)

    def test_return_value_of_to_json_string_method(self):
        """Test that the to_json_string method returns the right json data"""
        e_str = Base.to_json_string([])
        n_str = Base.to_json_string(None)
        json_str = Base.to_json_string([{'id': 89, 'width': 25}])
        self.assertEqual(e_str, "[]")
        self.assertEqual(n_str, "[]")
        self.assertEqual(json_str, '[{"id": 89, "width": 25}]')

    def test_save_to_file_class_method(self):
        """Test that a json file is created"""
        pass

    def test_from_json_string_return_type(self):
        """Test that the method can return a list of valid dicts
        Todo: *please implement me
        """
        pass

    def test_create_method_return_type(self):
        """Test the factory create method for its return type"""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        s1 = Square(3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)
        self.assertIsInstance(s2, Square)
        self.assertIsNot(s1, s2)

    def test_load_from_file_without_file(self):
        """Test that load form file returns an empty list if no file"""
        pass

    def test_save_file_csv_empty(self):
        """Test that empty csv file is create when arg is None or []"""
        pass

    def test_save_file_csv(self):
        """Test csv file is created file correct content"""
        pass

    def test_load_from_file_csv_empty(self):
        """Test empty list is returned when no csv or empty csv file"""
        pass

    def test_load_from_file_csv(self):
        """Test new instances are created when csv file is given"""
        pass
