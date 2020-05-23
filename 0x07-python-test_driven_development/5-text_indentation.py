#!/usr/bin/python3
"""This module creates a function that prints
the strings given as arguments."""


def text_indentation(text):
    """
    Text_indentation
        :param text: a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if char == ":" or char == "?" or char == ".":
            print(char, end="\n\n")
            flag = 1
        else:
            if flag == 1:
                print("", end="")
                flag = 0
            else:
                print(char, end="")
