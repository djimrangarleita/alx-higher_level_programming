#!/usr/bin/python3
"""Module my int that, a rebel"""


class MyInt(int):
    """Rebel class that override __eq__ and __ne__ of int class"""
    def __eq__(self, other):
        return not int.__eq__(self, other)

    def __ne__(self, other):
        return not int.__ne__(self, other)
