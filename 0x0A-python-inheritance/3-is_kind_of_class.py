#!/usr/bin/python3
""" checking is an object is an istance of"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of or an instance of a class that
       inherited from a specified class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
