#!/usr/bin/python3
"""This module creates a function"""


import sys

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

my_list = sys.argv[1:]
my_file = 'add_item.json'

try:
    before = load_json(my_file)
except:
    before = []
save_json(before + my_list, my_file)
