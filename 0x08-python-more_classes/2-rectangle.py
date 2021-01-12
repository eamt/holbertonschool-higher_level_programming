#!/usr/bin/python3
'''Module to create a rectangle'''


class Rectangle:
    '''Rectangle class'''

    def __init__(self, width=0, height=0):
        '''
            setup attributes
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        '''setter width'''
        if type(value) is not int:
            raise typeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for heihgt property'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """finding the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """finding the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
