#!/usr/bin/python3
"""Module to create a function"""


def add_attribute(obj, name, value):
    """
    Adds an attribute to a given object
        :param obj:
        :param name:
        :param value:
    """
    return setattr(obj, name, value)
