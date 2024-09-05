#!/usr/bin/python3
"""
validate
"""


def validUTF8(data):
    """
    check utf8 format
    """
    left = 0

    for ch in data:
        if left == 0:
            if ch >> 5 == 0b110:
                left = 1
            elif ch >> 4 == 0b1110:
                left = 2
            elif ch >> 3 == 0b11110:
                left = 3
            elif ch >> 7 != 0:
                return False
        else:
            if ch >> 6 != 0b10:
                return False
            left -= 1
    return True
