#!/usr/bin/python3
"""
This module defines a read_file function
"""

def read_file(filename=""):
    """Open a file and prints its contents to the stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
