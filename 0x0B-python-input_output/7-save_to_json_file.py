#!/usr/bin/python3
"""This module creates a function"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
            :param my_obj:
    """
    with open(filename, 'w+') as my_file:
        json.dump(my_obj, my_file)
