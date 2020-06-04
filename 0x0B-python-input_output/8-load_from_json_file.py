#!/usr/bin/python3
"""This module creates a function"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file
            :param my_obj:
    """
    with open(filename) as my_file:
        return json.load(my_file)
