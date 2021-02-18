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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objects into a json file"""
        json_string = "[]"
        if list_objs is not None and len(list_objs) > 0:
            to_save = []
            for obj in list_objs:
                to_save.append(cls.to_dictionary(obj))
            json_string = Base.to_json_string(to_save)

        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts json to string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """Create a new instance based on a class and dictionary"""
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)
        cls.update(new_instance, **dictionary)
        return new_instance
    
    def load_from_file(cls):
        """Create instances based on a list of instances from json file"""
        try:
            list_instances = []
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                json_string = f.read()
                list_attributes = Base.from_json_string(json_string)
            for dictionary in list_attributes:
                list_instances.append(cls.create(**dictionary))
            return list_instances
        except:
            return list_instances

    @classmethod
    def load_from_file_csv(cls):
        """Creates instances based on a list of instances from csv file"""
        list_instances = []
        try:
            with open(cls.__name__ + '.csv', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(row[key])
                    list_instances.append(cls.create(**row))
                return list_instances
        except:
            return list_instances
