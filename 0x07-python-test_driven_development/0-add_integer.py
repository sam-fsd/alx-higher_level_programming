#!/usr/bin/python3
"""
    This module defines the add function

"""

def add_integer(a, b=98):
    """ Returns the sum of a and b

        Raises:
            TypeError: If a or b is neither a  float nor integer

    """
    if (isinstance(a, int) is not True
        or isinstance(a, float) is not True):
        raise TypeError('a must be an integer')

    a = int(a)

    if (isinstance(b, int) is not True
        or isinstance(b, float) is not True):
        raise TypeError('b must be an integer')

    b = int(b)

    return a + b
