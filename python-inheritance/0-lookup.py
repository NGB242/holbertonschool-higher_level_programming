#!/usr/bin/python3
"""
Module for the lookup function.
"""


def lookup(obj):
    """
    Returns the list of attributes and methods available for an object.
    """
    return dir(obj)
