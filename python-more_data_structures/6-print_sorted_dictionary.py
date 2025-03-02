#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Get the keys of the dictionary and sort them
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys and print each key-value pair
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
