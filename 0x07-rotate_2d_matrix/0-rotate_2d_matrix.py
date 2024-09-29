#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    """
    n = len(matrix)

    matt = [row[:] for row in matrix]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = matt[n - j - 1][i]
