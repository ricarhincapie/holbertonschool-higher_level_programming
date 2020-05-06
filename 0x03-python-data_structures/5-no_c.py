#!/usr/bin/python3
def no_c(my_string):
        my_space = ""
        for i in my_string:
                if i not in "Cc":
                        my_space = my_space + i
        return my_space
