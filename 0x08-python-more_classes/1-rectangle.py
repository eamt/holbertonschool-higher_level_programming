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
        return self._width

    @width.setter
    def width(self, value):
        '''setter width'''
        if type(value) is not int:
            raise typeError("width is not integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for heihgt property'''
        return self._height

    @height.setter
    def height(self, value):
        '''setter height'''
        if type(value) is not int:
            raise TypeError("height is not an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

