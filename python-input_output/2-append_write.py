#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF-8) and returns;
 the number of characters added.
If the file doesn't exist, it should be created.
"""


def append_write(filename, text):
    """
    Appends a string at the end of a text file (UTF-8) and returns;
     the number of characters added.
    If the file doesn't exist, it should be created.

    param filename: The name of the file to append to.
    param text: The string to append to the file.
    return: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
