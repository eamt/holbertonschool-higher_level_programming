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
   
    """
    Printing the Rectangle
    """
    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += "#" * self.__width
            if i < (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}({}, {})".format(class_name, self.__width, self.__height)

    """
        Print the message "Bye rectangle..." when a instance of Rectangle is deleted.
    """
    def __del__(self):
        print("Bye rectangle...")
