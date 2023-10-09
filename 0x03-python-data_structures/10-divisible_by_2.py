#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mul = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)
            return (mul)
