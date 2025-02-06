#!/usr/bin/python3
"""
Defines a Rectangle class and a Square class that inherits from it.
"""


class Rectangle:
    """
    A class that represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square with a given size.

        Args:
            size (int): The side length of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.
        """
        self.__validate_integer(size)
        self.__size = size
        super().__init__(size, size)

    def __validate_integer(self, value):
        """
        Validates that the given value is a positive integer.

        Args:
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be a positive integer")

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
