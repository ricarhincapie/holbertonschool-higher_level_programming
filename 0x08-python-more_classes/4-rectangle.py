#!/usr/bin/python3
"""This module creates a class Rectangle."""


class Rectangle:
    """Class that creates a Rectangle.
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

    def area(self):
        """
        Public method to get the area of the Rectangle class
            :param self:
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Public method to get the perimeter of the Rectangle class
            :param self:
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        Instance method __str__ to return a string representing the object
            :param self:
        """
        if self.__width == 0 or self.height == 0:
            return ""
        my_str = ""

        for i in range(self.__height):
            my_str += "#" * self.__width
            my_str += "\n"
        return my_str[:-1]

    def __repr__(self):
        """
        Instance method __repr__ to return a string representing that
        holds a printable representation of the object to be reproduced
            :param self:
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
