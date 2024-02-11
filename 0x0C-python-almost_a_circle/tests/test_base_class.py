#!/usr/bin/python3
"""
Module used to test the base class
"""
from models.base import Base
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
