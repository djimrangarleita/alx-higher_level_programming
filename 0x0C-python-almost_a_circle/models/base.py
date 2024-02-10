#!/usr/bin/python3
"""
Module for the class Base, used to manage all the ids this class
is used by all other classes in the project
"""


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
