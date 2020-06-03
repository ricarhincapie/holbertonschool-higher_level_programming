#!/usr/bin/python3
"""This module creates a function"""


def lookup(obj):
        """
        lookup function to return a list with attributes and methods
                :param obj:
        """
        return list(dir(obj))
