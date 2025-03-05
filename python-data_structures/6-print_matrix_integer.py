#!/usr/bin/python3
"""
function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
