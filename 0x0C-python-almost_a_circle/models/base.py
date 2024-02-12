#!/usr/bin/python3
"""
Module for the class Base, used to manage all the ids this class
is used by all other classes in the project
"""
import json
import csv


class Base:
    """This is the main base class that manages id assignement to objs"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instance initializer

        Args:
            id (int, optional): Identifier of the new instances
        """
        if id:
            if type(id) is not int or id < 1:
                raise TypeError('id of class must be an integer and id >= 1')
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json string representation of the args list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """List of instances of base type"""
        filename = cls.__name__ + '.json'
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(cls.to_dictionary(obj))

        json_data = cls.to_json_string(list_dicts)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_data if list_objs else '')

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionary representations of a json string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create new instance of class cls"""
        new_instance = cls(10, 10)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """This method creates new instances from file data"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_objs = cls.from_json_string(f.read())
                list_instances = []
                for obj in list_objs:
                    list_instances.append(cls.create(**obj))
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save object to csv file"""
        filename = cls.__name__ + '.csv'
        if not list_objs:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('')
            return
        if cls.__name__ == 'Rectangle':
            fields = ['id', 'width', 'height', 'x', 'y']
        else:
            fields = ['id', 'size', 'x', 'y']
        list_dict = []
        for obj in list_objs:
            list_dict.append(cls.to_dictionary(obj))
        with open(filename, 'w', encoding='utf-8') as csvfile:
            dwriter = csv.DictWriter(csvfile, fieldnames=fields)
            dwriter.writeheader()
            dwriter.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """Create new instances from a csv file"""
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                csvreader = csv.DictReader(csvfile)
                list_instances = []
                for row in csvreader:
                    row = {key: int(val) for key, val in row.items()}
                    list_instances.append(cls.create(**row))
                return list_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and windows"""
        pass
