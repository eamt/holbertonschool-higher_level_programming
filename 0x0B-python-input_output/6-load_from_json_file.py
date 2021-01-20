#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file:
    Args:
        filename (str): The file where the file load will
    Returns:
        The JSON object represented by the string in the file
    """
    with open(filename) as f:
        json_obj = json.load(f)
    return json_obj
