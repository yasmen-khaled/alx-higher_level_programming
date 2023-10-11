#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sort_num = list(a_dictionary.keys())
    sort_num.sort()
    for x in sort_num:
        print("{}: {}".format(x, a_dictionary.get(x)))

