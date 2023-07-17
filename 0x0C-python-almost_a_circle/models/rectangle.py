#!/usr/bin/python3
"""
Defines rectangle class
"""

from models.base import Base



class Rectangle(Base):
    """
    class inherits from Base
    
    Attributes:
        width (int) : Hidth of the rectangle
        height (int) : Height of ther rectangle
        x (int) : Integer >= 0
        y (int) : Integer >= 0
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initilizes a rectangle instance

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int) : Integer >= 0
            y (int) : Integer >= 0

        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the private attribute value

        Returns:
            The value of the width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with a positive integer.

        Args:
            value (int): Height value to be set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with a positive integer.

        Args:
            value (int): Height value to be set

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets value to x

        Raises:
            TypeError: If x is not an integer
         ValueError: If x is less than 0

        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """returns value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets value to y

        Raises:
            TypeError: If y is not an integer
            ValueError: If y is less than 0

        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """calculates area the rectangle"""
        return self.width * self.height

    def display(self):
        """
        prints instance representation
        """
        for y_offset in range(self.y):
            print('')
        for row in range(0, self.height):
            for x_offset in range(self.x):
                print(' ', end='')
            for col in range(0, self.width):
                print('#', end='')
            print('')

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
