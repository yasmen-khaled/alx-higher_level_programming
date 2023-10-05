#!/usr/bin/python3

if __name__ == "__main__":
    import sys

   numbers = len(sys.argv) - 1
    if numbers == 0:
        print("0 arguments.")
    elif numbers == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numbers))
    for i in range(numbers):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
