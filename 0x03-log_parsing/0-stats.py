#!/usr/bin/python3
"""
locked boxes
"""

import signal
import sys
import re


codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {k: 0 for k in codes}


def reportdata(filesize):
    print("File size: {:d}".format(filesize))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


def getStdidRead():
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8
    filesize, count = 0, 0
    try:
        for line in sys.stdin:
            count += 1
            line = line.strip()
            match = regex.fullmatch(line)

            if match:
                code = match.group(1)
                filesize += int(match.group(2))

                if (code.isdecimal()):
                    stats[code] += 1

            if (count % 10 == 0):
                count = 0
                reportdata(filesize)
    finally:
        reportdata(filesize)


if __name__ == "__main__":
    getStdidRead()
