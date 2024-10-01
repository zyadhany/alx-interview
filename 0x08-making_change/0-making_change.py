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

    coins = sorted(coins)
    dp = np.zeros(total + 1) + 123456789
    dp[0] = 1

    for i in range(total):
        if dp[i] == 123456789:
            continue
        for coin in coins:
            if i + coin > total:
                break
            dp[i + coin] = min(dp[i + coin], dp[i] + 1)
    if dp[total] == 123456789:
        return -1
    return int(dp[total] - 1)
