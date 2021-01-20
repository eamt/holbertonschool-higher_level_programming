#!/usr/bin/python3
"""Module to  create a Rectangle class from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a Rectangle object"""

    def __init__(self, width, height):
        """
        Initialize the Rectangle object
        
        Attributes:
            attr1(width): width of rectangle
            attr2(height): height of rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of the instance"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
