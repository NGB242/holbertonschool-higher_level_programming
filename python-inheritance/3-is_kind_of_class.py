#!/usr/bin/python3
"""
Defines the function is_kind_of_class that checks if an object
is an instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
        """
        Determines if an object is an instance of a given class or a subclass.

        Args:
            obj: The object to check.
            a_class: The class to compare against.

        Returns:
            True if obj is an instance of a_class or inherits from it, otherwise False.
        """
        return isinstance(obj, a_class)
