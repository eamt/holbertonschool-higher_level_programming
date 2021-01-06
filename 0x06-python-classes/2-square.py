#!/usr/bin/python3
"""This is my first project with  Documentation in python"""


class Square:
    """We need to  set a size and set up some exceptions
    """

    def __init__(self, size=0):
        """method class with size value"""

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
