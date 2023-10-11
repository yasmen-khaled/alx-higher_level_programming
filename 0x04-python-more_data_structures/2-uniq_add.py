#!/usr/bin/python3

def uniq_add(my_list=[]):

    numbers = set(my_list)
    n = 0
    for x in numbers:
        n += x
    return (n)
