#!/usr/bin/python3
"""
Object instance of a class that inherited from class
"""


def inherits_from(obj, a_class):
    """
    Return True if the object (obj) is an instance
    of a class that inherited (directly or indirectly)
    from the specified class (a_class); otherwise is False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
