#!/usr/bin/python3

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, size):
        self.__validate_integer(size)
        self.__size = size
        super().__init__(size, size)

    def __validate_integer(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be a positive integer")

    def area(self):
        return self.__size ** 2
