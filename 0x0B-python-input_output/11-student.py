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

    def to_json(self):
        """
        to_json method
            :param self:
            :param attrs=None:
        """
        return self.__dict__
