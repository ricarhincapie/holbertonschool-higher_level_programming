#!/usr/bin/python3
"""
Base module
"""
import json
import os


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method for Class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string Method to take a list of dictionaries
        and convert it to JSON format

        Arguments:
            list_dictionaries {list}

        Returns:
            [JSON] -- [Json format instances representation]
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        my_json = json.dumps(list_dictionaries)
        return my_json

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file Saves to a file a list of objects

        Arguments:
            list_objs {list} -- Ex: a = Rectangle(1, 2)
            b = Rectangle(3, 4)
            list_objs = [a, b]
        """
        my_list_objs = [x.to_dictionary() for x in list_objs]
        json_ready = cls.to_json_string(my_list_objs)
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w+') as my_file:
            my_file.write(json_ready)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string Takes a JSON string and
        converts it to a list of dictionaries to be
        used in instantiation

        Arguments:
            json_string {JSON} -- [<class 'str'>]
            [{"height": 4, "width": 10, "id": 89},
            {"height": 7, "width": 1, "id": 7}]

        Returns:
            [list] -- [<class 'list'>]
            [{'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}]
        """
        empty = []
        if json_string:
            convert = json.loads(json_string)
            return convert
        return empty

    @classmethod
    def create(cls, **dictionary):
        """create Creates a new instance based in a
        dictionary. It creates a dummy instance and
        then updates it with the dictionary info

        Returns:
            [New instance]
        """
        if (cls.__name__ == "Square"):
            dummy = cls(98)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(98, 89)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file takes a JSON file named the same as
        the class from where this method is being called, convert
        the file data to dictionary and creates a list of new
        instances based on the dictionaries.

        Returns:
            [list] -- list of instances
        """
        file_name = cls.__name__ + ".json"
        my_list = []
        if not os.path.isfile(file_name):
            return my_list
        with open(file_name) as my_file:
            data = cls.from_json_string(my_file.read())
            for instance in data:
                my_list.append(cls.create(**instance))
        return my_list
