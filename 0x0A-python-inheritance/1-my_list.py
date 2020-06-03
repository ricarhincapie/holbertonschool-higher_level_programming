#!/usr/bin/python3
"""This module creates a function"""


class MyList(list):
        """
        Class MyList inherit from List class
                :param list:
        """
        def print_sorted(self):
                """
                print_sorted method
                        :param self:
                """
                print(sorted(self))
