#!/usr/bin/python3
""" check if an object is exactly an instance of specified class"""

def is_same_class(obj, a_class):
    """ checking is obj typy is same than a_class"""
    if type(obj) == a_class:
        return True
    else:
        return False
