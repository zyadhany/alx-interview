#!/usr/bin/python3
"""
validate
"""


def leadOne(num):
    tmp = (1 << 7)
    cnt = 0
    while tmp & num:
        tmp >>= 1
        cnt += 1
    return cnt


def validUTF8(data):
    left = 0

    for ch in data:
        ch &= (1 << 8) - 1
        if left:
            lf = (ch >> 6)
            if lf != 2:
                return False
        else:
            left = leadOne(ch)
            if left == 1 or left > 4:
                return False
            if left == 0:
                continue
        left -= 1
    return True
