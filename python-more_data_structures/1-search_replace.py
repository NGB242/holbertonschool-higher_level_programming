#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Create a new list with replaced elements
    """
    new_list = [replace if elmnt == search else elmnt for elmnt in my_list]
    return new_list
