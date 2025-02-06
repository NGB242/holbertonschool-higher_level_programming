#!/usr/bin/python3
"""
Defines the function inherits_from that checks if an object
inherits directly or indirectly from a specified class.
"""


def inherits_from(obj, a_class):
        """
        Determines if an object is an instance of a class that inherited
        (directly or indirectly) from the specified class.

        Args:
            obj: The object to check.
            a_class: The class to compare against.

        Returns:
            True if obj is an instance of a subclass of a_class (but not a direct instance),
            otherwise False.
        """
        return isinstance(obj, a_class) and type(obj) is not a_class
