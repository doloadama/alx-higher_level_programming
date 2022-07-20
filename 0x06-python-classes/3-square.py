#!/usr/bin/python3
"""Class square"""

class Square:
    """A class that represent a square"""


    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
    def area(self):
        """Calculates and returns the area of a square"""
        return self.__size ** 2