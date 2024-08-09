#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns the Pascal Triangle of n
    """

    if n <= 0:
        return []

    res = []
    for i in range(1, n + 1):
        tm = []
        for j in range(1, i + 1):
            if j == 1 or j == i:
                tm.append(1)
            else:
                tm.append(res[i - 2][j - 2] + res[i - 2][j - 1])
        res.append(tm)

    return res
