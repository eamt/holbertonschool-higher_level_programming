#!/usr/bin/python3
"""module to create a class square"""


class Square:
    """class square with attributes:
        size
        some attributes are protected from input.
    """

    def __init__(self, size=0):
        """initialization function for the square class
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate the area of the square
        """

        return self.__size ** 2
