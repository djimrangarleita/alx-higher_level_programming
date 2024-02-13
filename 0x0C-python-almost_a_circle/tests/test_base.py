#!/usr/bin/python3
"""
Module used to test the base class
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


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
        self.assertIsInstance(base1.id, int)
        self.assertIsInstance(base2.id, int)
        self.assertIsInstance(base3.id, int)

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
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertIsInstance(data, str)
        self.assertIsNot(data, '')

    def test_from_json_string_return_type(self):
        """Test that the method can return a list of valid dicts
        """
        json_string = '[{"height": 4, "width": 10, "id": 89}]'
        dict_rep = Rectangle.from_json_string(json_string)
        self.assertIsInstance(dict_rep, list)
        self.assertIsInstance(dict_rep[0], dict)
        self.assertIsInstance(Rectangle.from_json_string(None), list)
        self.assertIsInstance(Rectangle.from_json_string('[]'), list)

    def test_from_json_string_return(self):
        """Test method's return value"""
        json_string = '[{"height": 4, "width": 10, "id": 89}]'
        dict_rep = Rectangle.from_json_string(json_string)
        dict_rep2 = Rectangle.from_json_string('{"name": "Djimra", "stack":\
                "python, php, js, c"}')
        self.assertEqual(dict_rep, [{'height': 4, 'width': 10, 'id': 89}])
        self.assertEqual(dict_rep2, {'name': 'Djimra', 'stack':
                                     'python, php, js, c'})

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

    def test_create_method_return_new_rectangle(self):
        """Test that the methods creates a new instance with all values
        set and correct
        """
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r2.id, r1.id)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 0)

    def test_create_method_return_new_square(self):
        """Test that the methods creates a new instance of square with
        all values set and correct
        """
        s1 = Square(3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(s2.id, s1.id)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

    def test_create_with_empty_dictionary_raises_exception(self):
        """Test that an exception is raised when create is called with an
        empty dictionary
        """
        with self.assertRaises(ValueError):
            Square.create(**{})

    def test_load_from_file_without_file(self):
        """Test that load form file returns an empty list if no file"""
        try:
            os.rename('Rectangle.json', 'file')
        except IOError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])
        try:
            os.rename('file', 'Rectangle.json')
        except IOError:
            pass

    def test_load_from_file_return_type(self):
        """Test that load from file returns a new instance of cls"""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        rec = Rectangle.load_from_file()[0]
        s = Square(10, 2, 8)
        Square.save_to_file([s])
        sq = Square.load_from_file()[0]
        self.assertIsInstance(rec, Rectangle)
        self.assertIsInstance(sq, Square)

    def test_load_from_file(self):
        """Test that load from file returns a new instance correct of cls"""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        rec = Rectangle.load_from_file()[0]
        self.assertIsNot(rec, r1)
        self.assertEqual(rec.id, r1.id)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.width, r1.width)
        self.assertEqual(rec.height, r1.height)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, r1.y)

    def test_save_file_csv(self):
        """Test csv file is created file correct content"""
        r1 = Rectangle(10, 7, 2, 8, 12)
        Rectangle.save_to_file_csv([r1])
        stroutput = 'id,width,height,x,y\n12,10,7,2,8\n'
        with open('Rectangle.csv', 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertIsInstance(data, str)
        self.assertIsNot(data, '')
        self.assertEqual(len(data), len(stroutput))
        self.assertEqual(data, stroutput)

    def test_load_from_file_csv_empty(self):
        """Test empty list is returned when no csv or empty csv file"""
        try:
            os.rename('Rectangle.csv', 'csvfile')
        except IOError:
            pass
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        try:
            os.rename('csvfile', 'Rectangle.csv')
        except IOError:
            pass

    def test_load_from_file_csv_return_type(self):
        """Test new instances are created when csv file is given"""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file_csv([r1])
        rec = Rectangle.load_from_file_csv()[0]
        s = Square(10, 2, 8)
        Square.save_to_file_csv([s])
        sq = Square.load_from_file_csv()[0]
        self.assertIsInstance(rec, Rectangle)
        self.assertIsInstance(sq, Square)

    def test_load_from_file_csv(self):
        """Test that load from file csv returns new instance correct of cls"""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file_csv([r1])
        rec = Rectangle.load_from_file_csv()[0]
        self.assertIsNot(rec, r1)
        self.assertEqual(rec.id, r1.id)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.width, r1.width)
        self.assertEqual(rec.height, r1.height)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, r1.y)
