#!/usr/bin/python3
"""This module creates a function"""


def write_file(filename="", text=""):
    """
    write_file writes in a file and returns the # of chars written
        :param filename="":
        :param text="":
    """
    with open(filename, 'w+', encoding='utf-8') as file:
        return file.write(text)
