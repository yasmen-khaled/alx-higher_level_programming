#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        print("{}{}".format(digit1, digit2), end=", ")
