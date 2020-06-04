#!/usr/bin/python3
"""This module creates a function"""


def number_of_lines(filename=""):
    """
    number_of_lines
        :param filename="": file to count its lines
    """
    lines = 0
    with open(filename) as file:
        for line in file:
            lines += 1
    return lines
