#!/usr/bin/python3
"""Function for a class_to_json """


def class_to_json(obj):
    """Returns the dictionary description with simple data
    Args:
        obj (class object): the object to be serialized
    """
    return obj.__dict__
