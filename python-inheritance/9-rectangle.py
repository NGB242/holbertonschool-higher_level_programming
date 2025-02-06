#!/usr/bin/python3
"""
Defines a base class BaseGeometry and a subclass Rectangle.
"""


class BaseGeometry:
    """
    A base class for geometric operations.
    """

    def area(self):
        """
        Raises an exception to indicate that the area method is not implemented.

        This method must be overridden in subclasses that provide
        a specific area calculation.

        Raises:
        Exception: Always raises an exception indicating the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the variable (used in error messages).
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a formatted string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """

        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns a formal string representation of the rectangle,
        which is identical to the __str__ method in this case.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """

        return self.__str__()
