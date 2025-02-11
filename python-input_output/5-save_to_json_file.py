#!/usr/bin/python3
"""
Writes an object to a text file using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    :param my_obj: The object to be written to the file.
    :param filename: The name of the file where the object will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file, indent=4)
