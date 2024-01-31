#!/usr/bin/python3


"""Module that will create a looked class"""
class LockedClass(object):
    """This class is locked and accept only first_name as dynamic attr"""
    __slots__ = ['first_name']
