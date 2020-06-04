#!/usr/bin/python3
"""This module creates a function"""


class BaseGeometry():
    """
    BaseGeometry
    """
    def area(self):
            """
            Area
                    :param self:
            """
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
            """
            Integer_validator
                    :param self:
                    :param name:
                    :param value:
            """
            if type(value) != int:
                    raise TypeError("{} must be an integer".format(name))

            if value <= 0:
                    raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class, BassGeometry child
            :param BaseGeometry:
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    """
    Square class, Rectangle child
        :param Rectangle:
    """
    def __init__(self, size):
        self.__size = size
        BaseGeometry.integer_validator(self, "Square", size)

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
