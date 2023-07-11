#!/usr/bin/python3
"""
This module defines a read_file function

"""

def read_file(filename=""):
    """ This function reads a file and prints it to the stdout """
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        print(content, end='')
