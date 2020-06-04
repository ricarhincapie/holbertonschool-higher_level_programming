#!/usr/bin/python3
"""This module creates a function"""
import json


def from_json_string(my_str):
    """
    from_json_string
            :param my_str:
    """

    return json.loads(my_str)
