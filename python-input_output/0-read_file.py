#!/usr/bin/python3
"""function that print in the output the content of a folder"""


def read_file(filename=""):
    """function that print in the output the content of a folder"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
