#!/usr/bin/python3

import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif count == 1:
        print("Number of argument(s): 1.")
        print("1: {}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {}.".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
