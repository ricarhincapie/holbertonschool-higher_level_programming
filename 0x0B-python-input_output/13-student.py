#!/usr/bin/python3
""" My class module"""


class Student():
    """
    Student class
    """
    def __init__(self, first_name="", last_name="", age=None):
        """
        Init method
            :param self:
            :param first_name="":
            :param last_name="":
            :param age=None:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json method
            :param self:
            :param attrs=None:
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for i in attrs:
            if i in self.__dict__:
                my_dict[i] = self.__dict__[i]
        return my_dict

        def reload_from_json(self, json):
            """
            reload_from_json
                :param self:
                :param json:
            """
            for key, value in json.items():
                self.__dict__[key] = value
