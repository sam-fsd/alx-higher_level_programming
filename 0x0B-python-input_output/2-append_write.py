#!/usr/bin/python3
"""
Module defines a function
that appends a text to file
"""


def append_write(filename="", text=""):
    """Appends text to the file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
