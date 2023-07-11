#!/usr/usr/python3
"""Defines save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file in JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
