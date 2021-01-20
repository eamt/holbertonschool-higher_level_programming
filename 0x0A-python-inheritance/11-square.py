#!/usr/bin/python3
"""
This is the base_geometry class
"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    """
    The square class and inherts from Rectangle
    """

    def __init__(self, size):
        """
        Init of the square class
        """
        BaseGeometry.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
