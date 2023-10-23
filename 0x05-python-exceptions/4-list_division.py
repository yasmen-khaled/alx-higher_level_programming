#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
  _list = []
  for x in range(0, list_length):
    try:
      divid = my_list_1[x] / my_list_2[x]
    except TypeError:
      print("wrong type")
      divid = 0
    except ZeroDivisionError:
      print("division by 0")
      divid = 0
    except IndexError:
      print("out of range")
      divid = 0
    finally:
      _list.append(divid)
  return (_list)
