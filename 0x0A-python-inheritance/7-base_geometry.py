#!/usr/bin/python3
"""
Create empty class BaseGeometry
"""


class BaseGeometry():
    """
    Class BaseGeometry with Exception
    """
    def area(self):
        """Is the area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This verify value and type"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
