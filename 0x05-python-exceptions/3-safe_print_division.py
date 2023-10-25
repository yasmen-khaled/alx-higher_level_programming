#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divid = a / b
    except (TypeError, ZeroDivisionError):
        divid = None
    finally:
        print("Inside result: {}".format(divid))
    return (divid)