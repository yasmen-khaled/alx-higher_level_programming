#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    j = 0;

    for a in range(x):
    try:
    print("{}".format(my_list=[a], end="")
    j += 1
    except IndexErorr:
    break
    print("")

    return (j)
}
