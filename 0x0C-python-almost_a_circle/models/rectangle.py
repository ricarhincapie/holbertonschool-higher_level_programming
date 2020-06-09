#!/usr/bin/python3
"""This module creates a class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class

    Args:
        Base (Parent): Keeps track of instances with a unique Id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method for the class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """__str__ defines my string representation
        of the object

        Returns:
            [str] -- A string
        """
        string = "[Rectangle] ({}) {}/{} - {}/{}\
            ".format(self.id, self.__x, self.__y, self.__width, self.__height)
        return string

    @property  # PROPERTY FOR HEIGHT
    def height(self):
        """height property
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height is a setter for the height

        Arguments:
            height {int}

        Raises:
            TypeError
            ValueError
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property  # PROPERTY FOR WIDTH
    def width(self):
        """Property width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """width setter

        Arguments:
            width {int}

        Raises:
            TypeError
            ValueError
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property  # PROPERTY FOR X
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x is a setter

        Arguments:
            x {int}

        Raises:
            TypeError
            ValueError
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property  # PROPERTY FOR Y
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y is setter

        Arguments:
            y {int}

        Raises:
            TypeError
            ValueError
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area calculates a rectangle's area

        Returns:
            [int] -- The area
        """
        return self.__width * self.__height

    def display(self):
        """display prints to stdout the rectangle taking
        account of all its attributes
        """
        sign = "#"
        for m in range(self.y):
                print("")
        for x in range(self.__height):
            for n in range(self.__x):
                    print(" ", end="")
            for y in range(self.__width):
                print(sign, end="")
            print("")

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
                if counter < 6:
                    if type(ar) is not int:
                        raise TypeError("arg must be an integer")
            if lenght >= 1:
                setattr(self, "id", str(args[0]))
            if lenght >= 2:
                self.__width = args[1]
            if lenght >= 3:
                self.__height = args[2]
            if lenght >= 4:
                self.__x = args[3]
            if lenght >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if (hasattr(self, key)):
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary creates and returns the dictionary
        representation of the instance

        Returns:
            [dict]
        """
        attrs = ["id", "width", "height", "x", "y"]
        new_dict = {key: getattr(self, key) for key in attrs}
        return new_dict
