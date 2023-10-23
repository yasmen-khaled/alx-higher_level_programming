#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
  a = 0
    for b is not x:
        try:
            print("{}".format(my_list[i]), end="")
            a += 1
        except IndexError:
            break
    print("")
    return (a)
