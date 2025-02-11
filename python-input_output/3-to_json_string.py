#!/usr/bin/python3
"""
Converts an object to a JSON-formatted string.
"""


import json


def to_json_string(obj):
    """
    Convert an object to its JSON string representation.
    Parameters:
    obj (any): The object to be converted to JSON string.
    Returns:
    str: JSON string representation of the object.
    """

    try:
        return json.dumps(obj)
    except (TypeError, ValueError) as e:
        return str(e)
