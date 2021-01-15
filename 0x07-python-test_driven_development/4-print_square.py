#!/usr/bin/python3
"""module to define the print_square function
"""


def print_square(size):
    """ Function to  print a square.
    Args:
        size (int): size of square
    """
    if type(size) != int or size != size:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
