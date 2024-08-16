#!/usr/bin/python3
"""
locked boxes
"""


def canUnlockAll(boxes):
    n = len(boxes)
    vis = [False] * n

    def dfs(at):
        if at >= n or vis[at]:
            return 0

        cnt = 1
        vis[at] = 1

        for neg in boxes[at]:
            cnt += dfs(neg)

        return cnt

    if dfs(0) == n:
        return True
    return False
