#!/usr/bin/python3
"""This module creates a class Square"""


class Square():
        """Square class
        """

        def __init__(self, size=0):
                """Initialization of class square

                Args:
                        size: size of square (optional).
                """
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
                self.__size = size
