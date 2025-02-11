#!/usr/bin/python3
"""
Load data from a JSON file and return it as a Python object.
"""


import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return it as a Python object.
    
    :param filename: The path to the JSON file.
    :return: A Python object representing the JSON data.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {filename} is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
