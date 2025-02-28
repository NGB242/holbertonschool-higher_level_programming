#!/usr/bin/python3
"""
function adds all unique integers in a list
"""


def uniq_add(my_list):
    unique_integers = set(my_list)
    return sum(unique_integers)
