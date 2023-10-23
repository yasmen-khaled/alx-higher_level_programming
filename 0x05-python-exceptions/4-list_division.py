#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

  _list = []
  for x in range(0, list_length):
    try:
      i = my_list_1[x] / my_list_2[x]
    except TypeError:
      print("wrong type")
      i = 0
    except ZeroDivisionError:
      print("division by 0")
      i = 0
    except IndexError:
      print("out of range")
      i = 0
    finally:
      _list.append(i)
  return (_list)
