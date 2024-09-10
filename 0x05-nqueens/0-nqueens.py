#!/usr/bin/python3
"""
n-queens problem
"""

import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, pos):
    """Solve n-queens problem"""
    if col == n:
        print(pos)
        return

    for i in range(n):
        if is_safe(board, i, col):
            pos.append([col, i])
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, pos)
            pos.pop()
            board[i][col] = 0


n = int(sys.argv[1])
pos = []
board = [[0 for j in range(n)] for i in range(n)]
solve_nqueens(board, 0, n, pos)
