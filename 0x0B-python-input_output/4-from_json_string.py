#!/usr/bin/python3
""" 
Module defines a function
that returns an object
"""
import json


def from_json_string(my_str):
    """Returns an object"""
    return json.loads(my_str)

