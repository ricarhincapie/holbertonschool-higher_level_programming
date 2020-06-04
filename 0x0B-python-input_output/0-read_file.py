#!/usr/bin/python3
"""This module creates a function"""


def read_file(filename=""):
    """
    read_file reads a file
            :param filename="": file to read
    """
    with open(filename) as file:
        print(file.read())
