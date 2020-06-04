#!/usr/bin/python3
"""This module creates a function"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines prints the # of lines specified from a file
        :param filename="":
        :param nb_lines=0:
    """
    if nb_lines <= 0:
        with open(filename, encoding='utf-8') as file:
            print(file.read())
            return

    num_lines = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            num_lines += 1
            if num_lines <= nb_lines:
                print(line, end="")
        return
