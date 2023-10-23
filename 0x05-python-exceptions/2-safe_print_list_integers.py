#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    a = 0
    for a < x
        try:
            print("{:d}".format(my_list[a]), end="")
            z += 1
        except (ValueError, TypeError):
            continue
    print("")
    return(z)
