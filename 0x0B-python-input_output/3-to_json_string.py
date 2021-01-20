#!/usr/bin/python3
"""Module for a to_json_string function"""


import json


def to_json_string(my_obj):
    """Returns the JSON repr of an object
    Args:
        my_obj (class object): the object to converto to JSON string
    Returns:
        The JSON string representation of the object
    """
    return json.dumps(my_obj)
