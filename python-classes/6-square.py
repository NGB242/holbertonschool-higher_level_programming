#!/usr/bin/python3
"""
This is the Square module who initialize a square class,
with a private class attribute "size"
"""


class Square():
    """initialize a square's class with a private class atribute"""
    def __init__(self, size=0, position=(0, 0)):
        """"initialize the size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """"getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """"setter for position"""
        if type(value) is not tuple or len(value) is not 2 or\
            not all(isinstance(numb, int) and numb >= 0 for numb in value):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for count in range(self.__position[1]):
                print("")
            for count in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
