#!/usr/bin/python3

"""
Making Change
"""

import numpy as np


def makeChange(coins, total):
    """
    Given a target amount n and a list coins.
    Return the fewest number of coins needed to make change for n.
    """

    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
