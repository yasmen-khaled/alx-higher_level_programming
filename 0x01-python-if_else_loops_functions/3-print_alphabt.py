#!/usr/bin/python3
for alphabet in range(97, 123):
    if chr(alphabet) is not 'q' and chr(alphabet) is not 'e':
        print("{}".format(chr(alphabet)), end="")
