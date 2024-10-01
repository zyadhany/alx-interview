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

    dp = np.zeros(total + 1) + 23456789
    dp[0] = 0

    for i in range(total):
        for coin in coins:
            if i + coin <= total:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)
    if dp[total] == 23456789:
        return -1
    return int(dp[total])
