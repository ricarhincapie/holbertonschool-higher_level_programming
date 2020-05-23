#!/usr/bin/python3
"""This module creates a function that prints
the strings given as arguments."""


def say_my_name(first_name, last_name=""):
    """
    Function say_my_name
        :param first_name: string
        :param last_name="": optional string
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    if last_name == "":
        print(first_name)
    else:
        print(first_name + " " + last_name)
