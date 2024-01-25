#!/usr/bin/python3


"""This module contains the class Node and SinglyLinkedList to create linked
    lists
"""


class Node:
    """Node class that can create a node for a singly linked list
    """

    def __init__(self, data, next_node=None):
        """Init a node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the list, current instance"""
        return self.__data

    @data.setter
    def data(self, data):
        """Set the data of the list, current instance"""
        if type(data) is not int:
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        """Return the next node of the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """Set the next node of the list"""
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node


class SinglyLinkedList:
    """Singly linked list class to implement a list"""

    def __init__(self):
        """Initialize a singly linked list instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Try to insert a new node in the list, sorted"""
        tmp = self.get_next_node(value)
        if (self.__head == tmp) and ((tmp is None) or (tmp.data > value)):
            self.__head = Node(value, tmp)
        else:
            tmp.next_node = Node(value, tmp.next_node)

    def get_next_node(self, value):
        """Get the node where to insert the new node after"""
        tmp = self.__head
        while (tmp and tmp.next_node is not None):
            if value <= tmp.next_node.data:
                return tmp
            tmp = tmp.next_node
        return tmp

    def __repr__(self):
        """Build the string representation of the sll and return it to print"""
        sll = ''
        tmp = self.__head
        while tmp:
            sll += str(tmp.data)
            if tmp.next_node is not None:
                sll += '\n'
            tmp = tmp.next_node
        return sll
