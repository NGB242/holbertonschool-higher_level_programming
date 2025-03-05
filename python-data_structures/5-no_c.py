#!/usr/bin/python3
"""
 a function that removes all characters c and C from a string.
"""


def no_c(my_string):
    return "".join(char for char in my_string if char != 'c' and char != 'C')
