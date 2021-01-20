#!/usr/bin/python3
"""Functioa from_json_string function"""


import json


def from_json_string(my_str):
    """Return an object represened by JSON string
    Args:
        my_str (seralized str): the string to convert to object
    Returns:
        the deserialized string
    """
    return json.loads(my_str)
