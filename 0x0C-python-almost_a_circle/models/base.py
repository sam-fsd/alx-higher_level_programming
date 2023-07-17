#!/usr/bin/python3
"""defines base class"""

class Base:
    """Parent class
    
    Attribute(s):
        __nb_objects (int): tracks number of instances
    """
    __nb_objects = 0 

    def __init__(self, id=None):
        """initilizes object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
