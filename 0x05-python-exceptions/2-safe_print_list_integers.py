#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    z = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            z += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (z)
