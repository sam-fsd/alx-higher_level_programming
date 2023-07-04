#!/usr/bin/python3
"""Defining a class named Rectangle"""

class Rectangle:
    """ This class defines a rectangle with width and height"""

    def __init__(self, width=0, height=0):
        """This method intilizes the object with these private attributes
        
        Args:
            width (int): a positive integer
            height (int): a positive integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

