#!/usr/bin/python3
"""
Writes a string to a text file in UTF-8 encoding and returns the number of characters written.

param filename: The name of the file to write to.
param text: The string to write to the file.
return: The number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file in UTF-8 encoding and returns the number of characters written.

    :param filename: The name of the file to write to.
    :param text: The string to write to the file.
    :return: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)