#!/usr/bin/python3
"""
function that divides 2 integers and prints the result.
"""


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return
