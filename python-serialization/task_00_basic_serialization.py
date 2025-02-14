#!/usr/bin/python3
"""
Serialize a Python dictionary to a JSON file.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    Parameters:
    data (dict): A Python Dictionary with data
    filename (str): The filename of the output JSON file.
     If the output file already exists it should be replaced.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file
    to recreate the Python Dictionary.
    Parameters:
    filename (str): The filename of the input JSON file
    Returns:
    dict: A Python Dictionary with the deserialized JSON data from the file
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
