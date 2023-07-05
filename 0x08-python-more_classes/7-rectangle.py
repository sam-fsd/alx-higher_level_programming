#!/usr/bin/python3
"""Defining a class named Rectangle"""

class Rectangle:
    """ This class defines a rectangle with width and height
    
    Attributes:
            number_of_instance (int): a varibale that keeps track of the
            instance created from this class.
            print_symbol (::obj) : Gives the type of string representaion of
            our Rectangle
    """
    
    number_of_instances = 0
    print_symbol = '#'


    def __init__(self, width=0, height=0):
        """This method intilizes the object with these private attributes
        
        Args:
            width (int): a positive integer
            height (int): a positive integer
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
    
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print(self.print_symbol, end="")

            if i != self.__height - 1:
                print("")

        return ("")

    def __repr__(self):
        return "Rectangle({self.width}, {self.height})".format(self=self)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
