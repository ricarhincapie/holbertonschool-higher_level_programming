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
