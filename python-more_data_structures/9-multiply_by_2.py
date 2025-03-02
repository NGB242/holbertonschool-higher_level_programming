#!/usr/bin/python3
"""
Create a new dictionary with the same keys and values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    """
    Create a new dictionary with the same keys and values multiplied by 2
    """
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary
