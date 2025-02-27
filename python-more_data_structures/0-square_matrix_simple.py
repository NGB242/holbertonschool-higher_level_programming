#!/usr/bin/python3
"""
Create a new matrix with the same size as the input matrix
"""


def square_matrix_simple(matrix=[]):
    """Returns a new matrix with each value squared."""
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
