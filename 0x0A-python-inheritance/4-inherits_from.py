#!/usr/bin/python3
"""This module creates a function"""


def inherits_from(obj, a_class):
        """
        inherits_from
                :param obj:
                :param a_class:
        """
        return isinstance(obj, a_class) and type(obj) != a_class
