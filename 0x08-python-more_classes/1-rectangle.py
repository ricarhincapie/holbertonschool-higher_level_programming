#!/usr/bin/python3
"""This module creates a class Rectangle."""


class Rectangle:
    """This module creates a class Rectangle.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        """
        Instantiation of class Rectangle
            :param self:
            :param width=0:
            :param height=0:
        """
    @property
    def width(self):
        """
        Class rectangle width property
            :param self:
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
            :param self:
            :param value:
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Class rectangle height property
            :param self:
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
            :param self:
            :param value:
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
