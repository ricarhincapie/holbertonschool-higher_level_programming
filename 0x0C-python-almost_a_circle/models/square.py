#!/usr/bin/python3
"""This module creates the square class
"""

from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Square Class inherits from Rectangle Class

    Arguments:
        Rectangle {Class}
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ creates my string representation of the instance

        Returns:
            [str]
        """
        string = "[Square] ({}) {}/{} - {}\
            ".format(self.id, self.x, self.y, self.width)
        return string

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """size is setter for size

        Arguments:
            value {int}
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update implements two different ways to define or change
        the attributes of an instance

        Raises:
            ValueError
        """
        if args and len(args) > 0:
            lenght = len(args)
            counter = 0
            for ar in args:
                counter += 1
                if counter < 5:
                    if type(ar) is not int:
                        raise ValueError("arg must be an integer")
            if lenght >= 1:
                setattr(self, "id", args[0])
            if lenght >= 2:
                setattr(self, "size", args[1])
            if lenght >= 3:
                setattr(self, "x", args[2])
            if lenght >= 4:
                setattr(self, "y", args[3])
        else:
            for key, value in kwargs.items():
                if (hasattr(self, key)):
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary creates and returns the dictionary
        representation of the instance

        Returns:
            [dic]
        """
        attrs = ["id", "size", "x", "y"]
        new_dict = {key: getattr(self, key) for key in attrs}
        return new_dict
