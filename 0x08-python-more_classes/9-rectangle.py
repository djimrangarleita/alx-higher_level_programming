#!/usr/bin/python3


"""This module contains the class Rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instance initializer"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Destroy an instance of rectangle"""
        print("Bye rectangle...")
        if (type(self).number_of_instances > 0):
            type(self).number_of_instances -= 1

    @property
    def width(self):
        """Return the width of the current(instance) rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the current rectangle"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Return the height of the current(instance) rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the current rectangle"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Compute and return the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Compute and return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and return the biggest"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Make a new instance of rec with width==height==size"""
        return cls(size, size)

    def __str__(self):
        """Return string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ("")
        rec_str = ""
        for i in range(self.height):
            for j in range(self.width):
                rec_str += str(self.print_symbol)
            if i < self.height - 1:
                rec_str += '\n'
        return (rec_str)

    def __repr__(self):
        """Return the string representation of the current rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
