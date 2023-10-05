#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    ar = len(sys.argv) - 1
    if ar == 0:
        print("0 arguments.")
    elif ar == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ar))
    for i in range(ar):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
