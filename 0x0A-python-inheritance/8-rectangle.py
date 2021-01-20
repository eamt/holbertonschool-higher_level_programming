#!/usr/bin/python3
"""Module to create a Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a Rectangle object"""

    def __init__(self, width, height):
        """
        initialize the Rectangle object
        
        Attributes:
            attr1(width): width of rectangle
            attr2(height): height of rectangle
        """
    
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
