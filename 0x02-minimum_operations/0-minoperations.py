#!/usr/bin/python3
"""
Minimum Operations
"""


from queue import Queue


def minOperations(n):
    """
        min opp to get n
    """

    if n <= 0:
        return 0

    if n % 2:
        return n

    que = Queue()
    que.put((1, 0))
    vis = {}
    vis[(1, 0)] = 0

    while not que.empty():
        m = que.get()

        if m[0] == n:
            return vis[m]

        ps = (m[0] + m[1], m[1])
        if ps not in vis and ps[0] <= n:
            que.put(ps)
            vis[ps] = vis[m] + 1

        cp = (m[0], m[0])
        if cp not in vis:
            que.put(cp)
            vis[cp] = vis[m] + 1

    return -1
