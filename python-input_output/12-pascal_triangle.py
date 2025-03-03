#!/usr/bin/python3
"""
Generates Pascal's Triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    param n: The number of rows in Pascal's Triangle.
    return: A list of lists representing Pascal's Triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle
