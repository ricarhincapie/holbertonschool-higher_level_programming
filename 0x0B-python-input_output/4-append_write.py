#!/usr/bin/python3
"""This module creates a function"""


def append_write(filename="", text=""):
    """
    append_ write appends texto to a file and returns the # of chars written
        :param filename="":
        :param text="":
    """
    with open(filename, 'a+', encoding='utf-8') as file:
        return file.write(text)
