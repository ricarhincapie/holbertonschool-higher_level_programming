#!/usr/bin/python3
def multiply_by_2(a_dictionary):
        copy_list = a_dictionary.copy()
        for key, val in copy_list.items():
                copy_list[key] = val * 2
        return copy_list
