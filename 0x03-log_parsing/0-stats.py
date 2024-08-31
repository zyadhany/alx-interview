#!/usr/bin/python3
"""
locked boxes
"""

import signal
import sys


codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {k: 0 for k in codes}


def reportdata(filesize):
    print("File size: {:d}".format(filesize))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


def getStdidRead():
    filesize, count = 0, 0
    while True:
        try:
            ine = input()
            count += 1
            data = ine.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            try:
                filesize += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                reportdata(filesize)

        except KeyboardInterrupt:
            reportdata(filesize)


if __name__ == "__main__":
    getStdidRead()
