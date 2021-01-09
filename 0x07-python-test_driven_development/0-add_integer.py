#!/usr/bin/python3
"""this is the addition module"""

def add_integer(a, b=98):
    """
    Return teh additon of 2 numbers (a + b)
    a must be int or float
    b must be int of float
    any other case will raise a TypeError
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
