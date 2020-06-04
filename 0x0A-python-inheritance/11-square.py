#!/usr/bin/python3
"""This module creates a function"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, Rectangle child
        :param Rectangle:
    """
    def __init__(self, size):
        super().integer_validator("Square", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return '[Square] {}/{}'.format(self.__size, self.__size)
