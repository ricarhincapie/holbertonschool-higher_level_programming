#!/usr/bin/python3
"""This module creates a function that prints
the strings given as arguments."""


def print_square(size):
    """
    print_square
        :param size: size of the square
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for x in range(size):
            print("#", end="")
        print()
