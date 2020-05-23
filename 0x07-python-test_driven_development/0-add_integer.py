#!/usr/bin/python3
"""This module creates a function that adds two integers."""


def add_integer(a, b=98):
    """This function adds two integers
    Args:
            :param a: only an integer
            :param b=98: only an integer

    Returns:
            The sum of the integers
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
