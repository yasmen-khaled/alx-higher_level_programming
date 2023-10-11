#!/usr/bin/python

def number_keys(a_dictionary):

    numbers = 0
    keys = list(a_dictionary.keys())
    for x in keys:
        numbers += 1

    return (numbers)
