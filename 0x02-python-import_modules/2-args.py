#!/usr/bin/python3

if __name__ == "__main__":
import sys
    num = len(sys.argv) - 1
    if num == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif num == 1:
        print("Number of argument(s): 1.")
        print("1: {}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {}.".format(num))
        for i in range(num):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
