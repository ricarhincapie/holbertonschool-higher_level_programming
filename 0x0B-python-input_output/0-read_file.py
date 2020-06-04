#!/usr/bin/python3
"""This module creates a function"""


def read_file(filename=""):
    """
    read_file reads a file
            :param filename="": file to read
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
