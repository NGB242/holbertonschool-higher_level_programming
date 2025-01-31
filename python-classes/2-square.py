#!/usr/bin/python3
"""
This is the Square module who initialize a square class,
with a private class attribute "size"
"""


class Square():
    """initialize a square's class with a private class atribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
