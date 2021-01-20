#!/usr/bin/python3
"""Function to save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """This Function Write an object to a text file
    Args:
        my_obj (class object): The object to convert to JSON string
        filename (str): The file to write to
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
