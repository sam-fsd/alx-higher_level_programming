#!/usr/bin/python3
"""
Module writes to a file
"""


def write_file(filename="", text=""):
    """Writes text to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
