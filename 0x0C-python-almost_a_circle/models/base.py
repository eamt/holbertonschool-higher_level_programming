#!/usr/bin/python3
""" Base class"""


import os
import json


class Base:

    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation function for Base instance
        Args:
            id (int): the id of the instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dumps to Convert a dictionary or string to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
