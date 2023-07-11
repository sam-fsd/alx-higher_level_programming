#!/usr/bin/python3
""" 
Module imports json and defines
a function that returns JSON
representation of a object
"""
import json


def to_json_string(my_obj):
    """Converts obj to JSON"""
    return json.dumps(my_obj)

