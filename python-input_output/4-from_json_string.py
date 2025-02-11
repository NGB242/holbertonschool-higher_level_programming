#!/usr/bin/python3
"""
Convert a JSON string into a Python dictionary.
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string into a Python dictionary.
    Parameters:
    my_str (str): A JSON formatted string.

    Returns:
    dict: A Python dictionary representing the JSON string.
    """
    try:
        return json.loads(my_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
