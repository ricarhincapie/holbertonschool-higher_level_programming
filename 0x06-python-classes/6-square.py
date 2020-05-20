#!/usr/bin/python3
"""This module creates a class Square"""


class Square():
        """Square class
        """

        def __init__(self, size=0, position=(0, 0)):
                """Initialization of class square

                Args:
                        size: size of square (optional).
                """
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
                self.__position = position
                self.__size = size
        
        @property
        def position(self):
                """Getter to return position
                """
                return self.__position
        
        @position.setter
        def position(self, value):
                """Setter to position attribute
                """
                if (not isinstance(value, tuple) or
                        len(value) != 2 or
                        not isinstance(value[0], int) or
                        not isinstance(value[1], int) or
                        value[0] < 0 or
                        value[1] < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
                self.__position = value

        def area(self):
                """Method to return area of Square class

                Returns:
                        Area of the square
                """
                return self.__size ** 2

        @property
        def size(self):
                """Getter to return size of Square class
                """
                return self.__size

        @size.setter
        def size(self, size):
                """Setter size of square
                """
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
                self.__size = size

        def my_print(self):
                """Method to print the square class
                """
                size = self.__size
                if size == 0:
                        print()
                        return
                for i in range(size):
                        for j in range(size):
                                print("#", end="")
                        print()
