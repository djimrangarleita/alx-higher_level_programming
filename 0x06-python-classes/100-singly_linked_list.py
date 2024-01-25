#!/usr/bin/python3


"""This module contains the class Node and SinglyLinkedList to create linked
lists
"""


class Node:
    """Node class that can create a node for a singly linked list"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get the data of the list, current instance"""
        return self.__data

    @data.setter
    def data(self, data):
        """Set the data of the list, current instance"""
        if type(data) is not int:
            raise TypeError('data must be an integer')
        data = data

    @property
    def next_node(self):
        """Return the next node of the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """Set the next node of the list"""
        self.__next_node = next_node
