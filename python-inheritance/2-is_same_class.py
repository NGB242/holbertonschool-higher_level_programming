#!/usr/bin/python3
"""
This script contains a function that checks if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
        """
        Check if an object is exactly an instance of a specified class.
        """
        return type(obj) is a_class
