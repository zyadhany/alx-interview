#!/usr/bin/python3

"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Given a 2D grid map of 1s (land) and 0s (water).
    Compute the perimeter of the island.
    """

    n = len(grid)
    m = len(grid[0])
    perimeter = 0

    for i in range(n):
        for j in range(m):
            if not grid[i][j]:
                continue
            perimeter += 4
            if i > 0 and grid[i - 1][j]:
                perimeter -= 2
            if j > 0 and grid[i][j - 1]:
                perimeter -= 2

    return perimeter
