#!/usr/bin/python3
"""
Check if the key exists in the dictionary
"""


def simple_delete(a_dictionary, key=""):
    """
    Check if the key exists in the dictionary
    """
    if key in a_dictionary:
        """
        Delete the key from the dictionary
        """
        del a_dictionary[key]
    return a_dictionary
