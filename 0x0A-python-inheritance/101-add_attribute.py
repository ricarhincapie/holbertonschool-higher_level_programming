#!/usr/bin/python3
"""Module to create a function"""


def add_attribute(obj, name, value):
    """
    Adds an attribute to a given object
        :param obj:
        :param name:
        :param value:
    """
    if type(obj) is str or type(obj) is int\
            or type(obj) is float or type(obj) is bool\
            or type(obj) is tuple:
        raise TypeError("can't add new attribute")
    return setattr(obj, name, value)
