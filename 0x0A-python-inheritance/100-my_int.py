#!/usr/bin/python3
"""
This module create a class MyInt
"""


class MyInt(int):
    """
    This is the class MyInt
    """

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
