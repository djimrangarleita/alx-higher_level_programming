#!/usr/bin/python3
"""
Module used to test the base class
"""
from models.base import Base
import unittest


class TestBaseClass(unittest.TestCase):
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
