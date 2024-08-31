#!/usr/bin/python3
"""
Minimum Operations
"""


from queue import Queue


def minOperations(n):
    """
        min opp to get n
    """

    if n <= 1:
        return 0

    len = 1
    opp = 0
    next = 1

    while len < n:
        if n % len == 0:
            opp += 2
            next = len
            len *= 2
        else:
            opp += 1
            len += next

    return opp
